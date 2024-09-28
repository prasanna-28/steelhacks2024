from flask import Flask, request, jsonify
import requests
import os
import dotenv
from database import DATABASE

dotenv.load_dotenv()

app = Flask(__name__)

# Assume DATABASE is a pre-existing dictionary
# DATABASE = {
#     "course_name": {
#         "content": "CONTENTS\nPreface xi\n1 Vector Analysis 1\n...",
#         "url": "http://example.com/course_name"
#     },
#     # Add more courses as needed
# }

# Configuration for Gemini API
GEMINI_API_URL = "https://api.gemini.example.com/v1/query"  # Replace with actual Gemini API endpoint
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")  # Ensure your API key is set as an environment variable

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
    if not GEMINI_API_KEY:
        raise Exception("Gemini API key is not configured.")

    prompt = (
        "Given the following table of contents:\n"
        f"{content}\n\n"
        f"Description: {description}\n\n"
        "Please provide only the page number that is most relevant to the description. DO NOT INCLUDE ANY OTHER TEXT IN YOUR RESPONSE."
        "EXAMPLE: content = water - 5 fire - 10 ice - 15 Description: cold things YOUR RESPONSE: 15"
    )

    headers = {
        "Authorization": f"Bearer {GEMINI_API_KEY}",
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
        response = requests.post(GEMINI_API_URL, headers=headers, json=payload)
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

@app.route('/get_page_link', methods=['POST'])
def get_page_link():
    """
    Endpoint to retrieve the page link for a course section closest to the provided description.

    Expects a JSON payload with 'course' and 'description'.
    """
    try:
        data = request.get_json()

        # Validate input
        if not data:
            return jsonify({"error": "Invalid or missing JSON payload."}), 400

        course = data.get('course')
        description = data.get('description')

        if not course or not description:
            return jsonify({"error": "Both 'course' and 'description' fields are required."}), 400

        # Retrieve course data from DATABASE
        course_data = DATABASE.get(course)
        if not course_data:
            return jsonify({"error": f"Course '{course}' not found."}), 404

        content = course_data.get('content')
        base_url = course_data.get('url')

        if not content or not base_url:
            return jsonify({"error": f"Incomplete data for course '{course}'."}), 500

        # Interact with Gemini API to find the closest page number
        page_number = get_page_number_from_gemini(content, description)

        # Construct the final link
        final_link = f"{base_url}#page={page_number}"

        return jsonify({
            "course": course,
            "description": description,
            "page_number": page_number,
            "link": final_link
        }), 200

    except Exception as e:
        # Log the exception details if logging is set up
        # app.logger.error(f"Error in /get_page_link: {e}")

        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

