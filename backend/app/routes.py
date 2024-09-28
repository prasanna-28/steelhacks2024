from flask import Blueprint, render_template, Flask, request, jsonify, send_from_directory, current_app
from app import gemini
import uuid
import os

DATABASE = dict()
DATABASE_textbook = dict()

app = Flask(__name__)

# Assume DATABASE_textbook is a pre-existing dictionary
# DATABASE_textbook = {
#     "course_name": {
#         "content": "CONTENTS\nPreface xi\n1 Vector Analysis 1\n...",
#         "url": "http://example.com/course_name"
#     },
#     # Add more courses as needed
# }

#Assume DATABASE is a pre-existing dictionary 
# DATABASE = {
#     <uuid>: {
#         "latex": <latex file>
#         "messages": <message history>
#         "course_info": <course_info>
#     }
# }



@app.route('/get_pdf', methods=['POST'])
def get_pdf():
    file = request.files['file']
    uuid = str(uuid.uuid4())
    return gemini.get_pdf(DATABASE[uuid]['latex'])

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    pdf_directory = os.path.join(current_app.root_path, 'pdfs')
    return send_from_directory(pdf_directory, filename, as_attachment=True)


@app.route('/get_quizzes', methods=['POST'])
def get_quizz():
    # uuid = request.args['uuid']
    uuid = request.get_json()['uuid']
    return gemini.make_quiz(DATABASE[uuid]['latex'])


@app.route('/get_response', methods=['GET'])
def get_respone():
    uuid = request.get_json()['uuid']
    message = request.get_json()['message']
    return gemini.post_question(message, DATABASE[uuid]['latex'], DATABASE[uuid]['message_history'])


@app.route('/get_textbook', methods=['POST'])
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
        course_data = DATABASE_textbook[course]
        if not course_data:
            return jsonify({"error": f"Course '{course}' not found."}), 404

        content = course_data.get('content')
        base_url = course_data.get('url')

        if not content or not base_url:
            return jsonify({"error": f"Incomplete data for course '{course}'."}), 500

        # Interact with Gemini API to find the closest page number
        page_number = gemini.get_page_number_from_gemini(content, description)

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


