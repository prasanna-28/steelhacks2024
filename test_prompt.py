import google.generativeai as genai
import googleapiclient.discovery
from PIL import Image
from env import GEMINI_KEY, YOUTUBE_KEY
import time
import subprocess
import os
import isodate

def create_model():
    genai.configure(api_key=GEMINI_KEY)
    return genai.GenerativeModel("gemini-1.5-pro")

def notes_to_latex(model, filepath: str) -> str: 
    LATEX_PROMPT = """
    Convert these lecture notes to latex.
    Add headers and sections, so that the notes are easy to read.
    Center important equations and italicize key terms.
    Don't indent the first line of each paragraph.
    Reduce margins.
    Don't include any graphics or images in your response.
    Make sure to include all the necessary packages (amsmath, amsfonts). 
    Return just the latex code, nothing else.
    """

    sample_file = genai.upload_file(filepath)
    response = model.generate_content(
        [sample_file, "\n\n", LATEX_PROMPT]
    )
    return response.text

def compile_latex(latex_str: str, filename: str) -> None:
    with open(filename, "w") as file:
        file.write(latex_str)
    try:
        subprocess.run(
            ["pdflatex", "-output-directory=media/pdf", filename],
            check=True
        )
        print(f"Successfully compiled tex file")
    except subprocess.CalledProcessError as e:
        print(f"Error compiling tex file: {e}")

def get_youtube_queries(model, latex: str) -> str:
    YT_PROMPT = """Provide three youtube search queries that effectively recaps the content of this latex document.
    Provide each search query separated by newline characters. Do not include any other text in your response.
    Focus on section titles, key terms, and methods.
    Stick to one topic per youtube query.

    Some examples of good queries are:
    - "completing the square to solve quadratic equations"
    - "how to choose the right cost function for neural networks"
    - "properties of alkaline metals"
    """

    response = model.generate_content(
        [latex, "\n\n", YT_PROMPT]
    )
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


if __name__ == "__main__":
    model = create_model()

    t1 = time.time()
    latex = notes_to_latex(model, "media/prelim_short.pdf")

    t2 = time.time()
    compile_latex(latex, "test")

    t3 = time.time()
    queries = get_youtube_queries(model, latex)
    # print(queries)
    for q in queries.splitlines():
        # print("query:", q)
        results = youtube_search(q)
        print(results)

    t4 = time.time()
    print("API response time:", t2 - t1)
    print("Latex compilation:", t3 - t2)
    print("YT search time:   ", t4 - t3)
    print("Total time:       ", t4 - t1)
