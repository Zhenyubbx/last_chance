from flask import Blueprint, render_template, request, jsonify

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def test():
    return jsonify({"status_code": "success", "message":"server is running!"}), 200

@main.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    return jsonify({"status_code": "success"}), 200
