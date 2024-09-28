import os
import uuid
import json
from flask import Blueprint, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
from utils import (
    process_pdf,
    check_status,
    generate_response,
    fetch_textbook_links,
    generate_quizzes
)

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}
DATA_FOLDER = 'data'

# Ensure upload and data directories exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(DATA_FOLDER, exist_ok=True)

# Initialize Blueprint
main_bp = Blueprint('main', __name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@main_bp.route('/get_pdf', methods=['POST'])
def get_pdf():
    """
    Handle PDF file uploads along with course number.
    Expects:
        - 'file': PDF file uploaded via form-data.
        - 'course': Course number as a string.
    Returns:
        - JSON containing a unique 'uuid' to track the file processing.
    """
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request.'}), 400

    file = request.files['file']
    course = request.form.get('course')

    if not file or file.filename == '':
        return jsonify({'error': 'No file selected for uploading.'}), 400

    if not course:
        return jsonify({'error': 'Course number is required.'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        unique_id = str(uuid.uuid4())
        saved_filename = f"{unique_id}_{filename}"
        file_path = os.path.join(UPLOAD_FOLDER, saved_filename)
        file.save(file_path)

        # Initialize processing status
        status_data = {
            'status': 'processing',
            'results': None
        }
        with open(os.path.join(DATA_FOLDER, f"{unique_id}_status.json"), 'w') as f:
            json.dump(status_data, f)

        # Start processing (this could be asynchronous in a real app)
        process_pdf(unique_id, file_path, course)

        return jsonify({'uuid': unique_id}), 200
    else:
        return jsonify({'error': 'Allowed file types are pdf.'}), 400

@main_bp.route('/status', methods=['GET'])
def status():
    """
    Check the processing status of the uploaded PDF.
    Expects:
        - 'file_id': UUID as a query parameter.
    Returns:
        - JSON containing 'status' and 'results' if processing is done.
    """
    file_id = request.args.get('file_id')
    if not file_id:
        return jsonify({'error': 'file_id query parameter is required.'}), 400

    status_file = os.path.join(DATA_FOLDER, f"{file_id}_status.json")
    if not os.path.exists(status_file):
        return jsonify({'error': 'Invalid file_id.'}), 404

    with open(status_file, 'r') as f:
        status_data = json.load(f)

    return jsonify(status_data), 200

@main_bp.route('/get_response', methods=['POST'])
def get_response():
    """
    Handle chat questions from the student.
    Expects (JSON):
        - 'question': The user's question as a string.
        - 'uuid': UUID to identify the session.
    Returns:
        - JSON containing the 'answer'.
    """
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid JSON.'}), 400

    question = data.get('question')
    file_id = data.get('uuid')

    if not question or not file_id:
        return jsonify({'error': 'Both question and uuid are required.'}), 400

    # Validate UUID
    status_file = os.path.join(DATA_FOLDER, f"{file_id}_status.json")
    if not os.path.exists(status_file):
        return jsonify({'error': 'Invalid uuid.'}), 404

    # Generate response (this could involve AI processing)
    answer = generate_response(question, file_id)

    return jsonify({'answer': answer}), 200

@main_bp.route('/get_textbook', methods=['POST'])
def get_textbook():
    """
    Fetch relevant textbook links based on course number.
    Expects (JSON):
        - 'course': Course number as a string.
        - 'uuid': UUID to identify the session.
    Returns:
        - JSON containing textbook links categorized by chapters.
    """
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid JSON.'}), 400

    course = data.get('course')
    file_id = data.get('uuid')

    if not course or not file_id:
        return jsonify({'error': 'Both course and uuid are required.'}), 400

    # Validate UUID
    status_file = os.path.join(DATA_FOLDER, f"{file_id}_status.json")
    if not os.path.exists(status_file):
        return jsonify({'error': 'Invalid uuid.'}), 404

    # Fetch textbook links
    links = fetch_textbook_links(course, file_id)

    return jsonify({'links': links}), 200

@main_bp.route('/get_quizzes', methods=['POST'])
def get_quizzes():
    """
    Provide quizzes based on the processed PDF content.
    Expects (JSON):
        - 'uuid': UUID to identify the session.
    Returns:
        - JSON containing multiple choice and free response quizzes.
    """
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid JSON.'}), 400

    file_id = data.get('uuid')

    if not file_id:
        return jsonify({'error': 'uuid is required.'}), 400

    # Validate UUID
    status_file = os.path.join(DATA_FOLDER, f"{file_id}_status.json")
    if not os.path.exists(status_file):
        return jsonify({'error': 'Invalid uuid.'}), 404

    # Check if processing is done
    with open(status_file, 'r') as f:
        status_data = json.load(f)

    if status_data.get('status') != 'done':
        return jsonify({'error': 'Processing not completed yet.'}), 400

    # Generate or fetch quizzes
    quizzes = generate_quizzes(file_id)

    return jsonify(quizzes), 200

