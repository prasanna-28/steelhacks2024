from flask import Blueprint, send_from_directory, current_app, render_template
import os

# Create a Blueprint
main = Blueprint('main', __name__)

@main.route('/')
def home():
    return "test"

@main.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    pdf_directory = os.path.join(current_app.root_path, 'pdfs')
    return send_from_directory(pdf_directory, filename, as_attachment=True)