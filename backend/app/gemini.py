import google.generativeai as genai
import googleapiclient.discovery
import json
import requests
import subprocess
import asyncio
import isodate
from env import GEMINI_API, YOUTUBE_KEY
from flask import jsonify

# DATABASE_textbook = {
#     "PHYS 2373": {
#         "content": """
#                 """,
#         "url"    : "https://msashigri.wordpress.com/wp-content/uploads/2016/11/methods-of-mathemacial-for-physicists.pdf"
#     }
# }
from database import DATABASE_textbook

UPLOAD_FOLDER = "app/static/uploads"
PDF_FOLDER = "app/static/pdf"

genai.configure(api_key=GEMINI_API)
model = genai.GenerativeModel("gemini-1.5-flash")

chats = {}

def get_youtube_queries(file_id) -> str:
    YT_PROMPT = """Provide four youtube search queries that effectively recaps the content of this latex document.
    Provide each search query separated by newline characters. Do not include any other text in your response.
    Focus on section titles, key terms, and methods.
    Stick to one topic per youtube query.

    Some examples of good queries are:
    - "completing the square to solve quadratic equations"
    - "how to choose the right cost function for neural networks"
    - "properties of alkaline metals"
    """

    chat = chats[file_id]
    response = chat.send_message(YT_PROMPT)
    return response.text

def get_video_details(video_id):
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=YOUTUBE_KEY)
    request = youtube.videos().list(
        part="contentDetails,player",
        id=video_id
    )
    response = request.execute()
    video_details = response.get('items', [])[0]
    duration_iso = video_details['contentDetails']['duration']
    duration_parsed = isodate.parse_duration(duration_iso)
    embed_html = video_details['player']['embedHtml']
    return {
        'duration': str(duration_parsed),
        'embedHtml': embed_html
    }

def youtube_search(query, max_results=1):
    # api_key = os.getenv("YOUTUBE_API_KEY")
    # if not api_key:
    #     raise ValueError("API Key not found in environment.")
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=YOUTUBE_KEY)
    request = youtube.search().list(
        part="snippet",
        maxResults=max_results,
        q=query,
        type="video"
    )
    search_response = request.execute()
    results = []
    for item in search_response.get('items', []):
        video_info = {
            'title': item['snippet']['title'],
            'videoId': item['id']['videoId'],
            'description': item['snippet']['description'],
        }
        details = get_video_details(item['id']['videoId'])
        video_info['duration'] = details['duration']
        results.append(video_info)
    return results

def notes_to_latex(file_id: str) -> str:
    LATEX_PROMPT = """
    Convert these lecture notes to latex.
    Add headers and sections, so that the notes are easy to read.
    Center important equations and italicize key terms.
    Don't indent the first line of each paragraph.
    Reduce margins.
    Don't include any graphics or images in your response.
    Make sure to include all the necessary packages (amsmath, amsfonts).
    Use only plain text characters, no unicode characters.
    Return just the latex code, nothing else.
    """

    chat = chats[file_id]
    response = chat.send_message(LATEX_PROMPT)
    return response.text

def save_latex(latex: str, filepath: str):
    with open(filepath, "w") as file:
        file.write(latex)

def compile_latex(filepath: str) -> None:
    try:
        subprocess.run(
            ["pdflatex", f"-output-directory={PDF_FOLDER}", filepath],
            check=True
        )
        print(f"Successfully compiled tex file")
    except subprocess.CalledProcessError as e:
        print(f"Error compiling tex file: {e}")

def upload_latex(latex_fp: str) -> str:
    return genai.upload_file(latex_fp)

def make_glossary(file_id):
    GLOSSARY_PROMPT = r"""
    Make a glossary of key definitions in the latex file.
    Return your glossary as a JSON string in plain text (do not use \n or \t, markdown, or latex).

    EXAMPLE: "\begin{document} A natural number is a whole number greater than 0. \end{document}" -> {"natural number": "a whole number greater than 0"}
    """
    chat = chats[file_id]
    response = chat.send_message(GLOSSARY_PROMPT)
    return json.loads(response.text)

def make_summary(file_id):
    SUMMARY_PROMPT = r"""
    Make a summary of the content and key ideas in the latex file in 2-3 sentences.
    Return your summary in plain text (without any markdown elements).

    EXAMPLE: "\begin{document} The function $f$ maps $x \in \mathbb{R}$ to $\sqrt{x}$. \end{document}" -> "f maps x to the square root of x."
    """
    chat = chats[file_id]
    response = chat.send_message(SUMMARY_PROMPT)
    return response.text

def make_quiz(file_id):
    # prompt = r'''The following is a latex file that compiles notes and references for some class. 
    # I am taking this class and I want you to be a TA. Make me a small quiz on this material. 
    # Give me questions on each line. Start with definitions in a multiple choice question format. 
    # There should be 3 wrong answers and 1 right answer. Then give me a few harder problems.
    # Return this all in a json format. Do not include any control characters that json.loads
    # cannot understand (\n, \t).
    # '''

    QUIZ_PROMPT = r"""
    Here is a latex document of lecture notes.
    You are a teaching assistant for this course. 
    Make a quiz of five multiple choice problems on this material.
    Each multiple choice question should have three wrong answers and one correct answer.
    Return your glossary as a JSON string in plain text (do not use \n or \t, markdown, or latex).

    EXAMPLE: 
        "\begin{document} A natural number is a whole number greater than 0. \end{document}" ->
        "{
            "problem1": {
                "question": "Which of the following is a natural number?"
                "wrong_answers": ["0.1", "-2", "pi"]
                "correct_answer": "4"
            }
        }"
    """
    chat = chats[file_id]
    response = chat.send_message(QUIZ_PROMPT)
    return json.loads(response.text)

def get_response(message, file_id):
    RESPONSE_PROMPT = r"""
    You are a teaching assistant for this course, and these are my notes.
    Respond to the following prompt in 2-3 sentences.
    Do not include any control sequences (\t or \n), latex, or markdown.
    """
    chat = chats[file_id]
    response = chat.send_message([RESPONSE_PROMPT, message])
    return response.text

def get_page_number_from_gemini(content, file_id):
    """
    Interact with the Gemini API to find the page number closest to the description.

    Args:
        content (str): The table of contents as a large text string.
        description (str): The description provided in the POST request.

    Returns:
        int: The page number closest to the description.

    Raises:
        Exception: If the API call fails or returns an invalid response.
    """
    if not GEMINI_API:
        raise Exception("Gemini API key is not configured.")

    prompt = (
        "Given the following table of contents:\n"
        f"{content}\n\n"
        "Please provide only the page number that is most relevant to the uploaded latex. DO NOT INCLUDE ANY OTHER TEXT IN YOUR RESPONSE."
    )

    headers = {
        "Authorization": f"Bearer {GEMINI_API}",
        "Content-Type": "application/json"
    }

    payload = {
        "prompt": prompt,
        "max_tokens": 10,  # Adjust based on Gemini API specifications
        "temperature": 0.0,  # For deterministic output
        "top_p": 1,
        "n": 1,
        "stop": None  # Define stop sequences if necessary
    }

    try:
        chat = chats[file_id]
        response = chat.send_message(prompt)
        # response.raise_for_status()  # Raise an HTTPError if the HTTP request returned an unsuccessful status code

        # page_number = 

        # # Parse the page number from Gemini's response
        # # This parsing logic may need to be adjusted based on Gemini API's actual response format
        # page_number_str = data.get("choices", [{}])[0].get("text", "").strip()

        # # Validate that the response is a number
        # if not page_number_str.isdigit():
        #     raise Exception(f"Invalid page number received from Gemini API: '{page_number_str}'")

        # page_number = int(page_number_str)
        return int(response.text)

    except requests.exceptions.RequestException as req_err:
        raise Exception(f"Error communicating with Gemini API: {req_err}")
    except ValueError:
        raise Exception("Received non-integer page number from Gemini API.")
    except Exception as e:
        raise Exception(f"An error occurred while processing Gemini API response: {e}")

def get_page_link(course, genai_file):
    """
    Endpoint to retrieve the page link for a course section closest to the provided description.

    Expects a JSON payload with 'course' and 'description'.
    """
    try:
        # data = request.get_json()

        # # Validate input
        # if not data:
        #     return jsonify({"error": "Invalid or missing JSON payload."}), 400

        # course = data.get('course')
        # description = data.get('description')

        # if not course or not description:
        #     return jsonify({"error": "Both 'course' and 'description' fields are required."}), 400

        # # Retrieve course data from DATABASE
        # course_data = DATABASE_textbook[course]
        # if not course_data:
        #     return jsonify({"error": f"Course '{course}' not found."}), 404

        # content = course_data.get('content')
        # base_url = course_data.get('url')

        # if not content or not base_url:
        #     return jsonify({"error": f"Incomplete data for course '{course}'."}), 500

        # Interact with Gemini API to find the closest page number
        content = DATABASE_textbook[course]['content']
        base_url = DATABASE_textbook[course]['url']
        page_number = get_page_number_from_gemini(content, genai_file)
        page_number += DATABASE_textbook[course]['page_buffer']

        return f"{base_url}#page={page_number}"

    except Exception as e:
        # Log the exception details if logging is set up
        # app.logger.error(f"Error in /get_page_link: {e}")
        print(e)

        return jsonify({"error": str(e)}), 500

async def start_processing(course, file_id):
    file = f"{UPLOAD_FOLDER}/{file_id}.pdf"
    genai_file = genai.upload_file(file)
    chat = model.start_chat()
    chat.send_message(genai_file)
    chats[file_id] = chat
    
    latex = notes_to_latex(file_id)
    latex_fp = f"{PDF_FOLDER}/{file_id}.txt"
    save_latex(latex, latex_fp)
    print("latex saved")
    genai_file = upload_latex(latex_fp)
    glossary = make_glossary(file_id)
    summary = make_summary(file_id)
    compile_latex(latex_fp)
    print("compiled latex")
    queries = get_youtube_queries(file_id)
    # print(queries)
    vids = []
    i = 0
    for q in queries.splitlines():
        if i == 4**(1/2) + ((5 * 5 == 27 - 2) + 1) ** 2 / 2: break
        else: i += (True != False)
        vids.append(youtube_search(q))
    link = get_page_link(course, file_id)

    return {
        "filepath": f"{file_id}.pdf",
        "glossary": glossary,
        "summary": summary,
        "link": link,
        "videos": vids,
    }

def quiz_processing(file_id):
    return make_quiz(file_id)


if __name__ == "__main__":
    name = "prelim_short"
    with app.app_context():
        ret = quiz_processing(name)
    print(ret)
    # print(ret["filepath"], ret["glossary"], ret["summary"], ret["link"], sep="\n")
    # print(make_glossary(genai_file))
    # print(make_summary(genai_file))
    