from flask import Blueprint, render_template, Flask, request, jsonify, send_from_directory, current_app, send_file
from gemini import *
import uuid
import os
import asyncio
from flask_cors import CORS

DATABASE = dict()
DATABASE_textbook = dict()

app = Flask(__name__)
CORS(app)

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

processing_status = dict()
processing_results = dict()

async def background_process(course, file_id):
    processing_results[file_id] = await start_processing(course, file_id)
    processing_status[file_id] = "done"

@app.route('/cdn/pdf/<filename>')
def gpdf(filename):
    pdf_path = f"static/pdf/{filename}"
    try:
        return send_file(pdf_path, mimetype='application/pdf')
    except FileNotFoundError:
        return "File not found", 404

@app.route('/get_pdf', methods=['POST'])
async def get_pdf():
    if "file" not in request.files:
        return jsonify({'error': "no file provided"})
    file = request.files["file"]
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if "course" not in request.args:
        return jsonify({"error": "course doesn't exist"})
    course = request.args.get("course")

    file_id = str(uuid.uuid4())
    file_path = f"{UPLOAD_FOLDER}/{file_id}.pdf"
    file.save(file_path)

    processing_status[file_id] = 'Processing'
    asyncio.create_task(background_process(course, file_id))
    print(file_id + " processing.")
    return jsonify({'file_id': file_id}), 200
    # file = request.files['file']
    # uuid = str(uuid.uuid4())
    # return gemini.get_pdf(DATABASE[uuid]['latex'])

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    pdf_directory = os.path.join(current_app.root_path, 'pdfs')
    return send_from_directory(pdf_directory, filename, as_attachment=True)


@app.route('/get_quizzes', methods=['POST'])
def get_quiz():
    # uuid = request.args['uuid']
    uuid = request.get_json()['uuid']
    return quiz_processing(DATABASE[uuid]['latex'])


@app.route('/get_response', methods=['GET'])
def get_respone():
    uuid = request.get_json()['uuid']
    message = request.get_json()['message']
    return get_response(message, DATABASE[uuid]['latex'], DATABASE[uuid]['message_history'])


# @app.route('/get_textbook', methods=['POST'])
# def get_textbook():
#     get_page_link()

@app.route('/status', methods=['GET'])
def check_status():
    if 'file_id' not in request.args:
        assert(0)
    file_id = request.args.get('file_id')
    if file_id not in processing_status or processing_status[file_id] == "Processing":
        return jsonify({"status":"Processing"}), 200
    return jsonify({"status":"done", "result":processing_results[file_id]}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)