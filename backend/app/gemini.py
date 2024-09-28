import google.generativeai as genai
import json
import dotenv
import os 

dotenv.load_dotenv()

GEMINI_API = os.environ['GEMINI_API_KEY']

genai.configure(api_key=GEMINI_API)
model = genai.GenerativeModel("gemini-1.5-pro")

def make_summary(latex_file):
    prompt = '''The following is a latex file that compiles notes and references for some class. 
    Give me two things which should be separated by a newline. I want you to make a glossary of
    key definitions. Then make a summary of the content and key ideas
    '''
    response = model.generate_content(prompt + latex_file)
    print(response.text)


def make_quiz(latex_file):
    prompt = r'''The following is a latex file that compiles notes and references for some class. 
    I am taking this class and I want you to be a TA. Make me a small quiz on this material. 
    Give me questions on each line. Start with definitions. Then give me a few harder problems. 
    Return this all in a json format. Do not include any control characters that json.loads
    cannot understand (\n, \t)
    '''
    response = model.generate_content(prompt + latex_file)
    text = response.text
    text = text.splitlines()
    text.pop(0)
    text.pop()
    # print(text)
    text = '\n'.join(text)
    print(text)
    quiz_json = make_json(text)

def make_json(quiz):
    file = json.loads(quiz) 

def send_file():
    pass
