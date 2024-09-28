import google.generativeai as genai
import json
import dotenv
import requests
import os 
from flask import Flask, request, jsonify, send_file
app = Flask(__name__)

dotenv.load_dotenv()

GEMINI_API = os.environ['GEMINI_API_KEY']

genai.configure(api_key=GEMINI_API)
model = genai.GenerativeModel("gemini-1.5-pro")

def get_pdf():
    pass
    # get from owen

def make_summary(latex):
    prompt = '''The following is a latex file that compiles notes and references for some class. 
    Give me two things which should be separated by a newline. I want you to make a glossary of
    key definitions. Then make a summary of the content and key ideas
    '''
    response = model.generate_content(prompt + latex)
    print(response.text)


def make_quiz(latex):
    prompt = r'''The following is a latex file that compiles notes and references for some class. 
    I am taking this class and I want you to be a TA. Make me a small quiz on this material. 
    Give me questions on each line. Start with definitions in a multiple choice question format. 
    There should be 3 wrong answers and 1 right answer. Then give me a few harder problems. 
    Return this all in a json format. Do not include any control characters that json.loads
    cannot understand (\n, \t).
    '''
    response = model.generate_content(prompt + latex)
    text = response.text
    text = text.splitlines()
    text.pop(0)
    text.pop()
    # print(text)
    text = '\n'.join(text)
    # print(text)
    quiz_json = json.loads(text)
    return quiz_json

def get_response(message, latex, message_history):
    prompt = '''The compiled notes and chat history are all for context:
    This is a compiled version of my notes. 
    {latex}
    This is the chat history we have: 
    {message_history}
    This is my question:
    {question}'''
    response = model.generate(message)
    return response.txt

def get_textbook(latex):
    pass
    # get from prasanna

def get_page_number_from_gemini(content, description):
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
        f"Description: {description}\n\n"
        "Please provide only the page number that is most relevant to the description. DO NOT INCLUDE ANY OTHER TEXT IN YOUR RESPONSE."
        "EXAMPLE: content = water - 5 fire - 10 ice - 15 Description: cold things YOUR RESPONSE: 15"
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
        response = model.generate_content(prompt)
        response.raise_for_status()  # Raise an HTTPError if the HTTP request returned an unsuccessful status code

        data = response.json()

        # Parse the page number from Gemini's response
        # This parsing logic may need to be adjusted based on Gemini API's actual response format
        page_number_str = data.get("choices", [{}])[0].get("text", "").strip()

        # Validate that the response is a number
        if not page_number_str.isdigit():
            raise Exception(f"Invalid page number received from Gemini API: '{page_number_str}'")

        page_number = int(page_number_str)
        return page_number

    except requests.exceptions.RequestException as req_err:
        raise Exception(f"Error communicating with Gemini API: {req_err}")
    except ValueError:
        raise Exception("Received non-integer page number from Gemini API.")
    except Exception as e:
        raise Exception(f"An error occurred while processing Gemini API response: {e}")

