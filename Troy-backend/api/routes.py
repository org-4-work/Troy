# -*- encoding: utf-8 -*-
"""
Copyright (c) 2023 - present TroyTeam
"""
import os
from app.kfsdoc.reviewer import Reviewer
from flask import send_file, jsonify
from flask_restx import Api, Resource
from werkzeug.datastructures import FileStorage
from .config import ALLOWED_EXTENSIONS, UPLOAD_FOLDER
from collections import deque
import uuid

rest_api = Api(version="1.2", title="Troy APIs")

upload_parser = rest_api.parser()
upload_parser.add_argument('file', location='files',
                           type=FileStorage, required=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

"""
    Flask-Restx routes
"""


# Maintain deques to store the last uploaded Chinese and English filenames
uploaded_chinese_files = deque(maxlen=1)
uploaded_english_files = deque(maxlen=1)



## /api/upload/english
@rest_api.route("/api/upload/english")
@rest_api.expect(upload_parser)
class EnglishFileUpload(Resource):
    def post(self):
        args = upload_parser.parse_args()
        file = args.get('file')
        unique_filename = str(f"{uuid.uuid4()} _ { file.filename}")
        file.save(os.path.join(UPLOAD_FOLDER, unique_filename))
        uploaded_english_files.append(unique_filename)
        return "English Document Uploaded"


# /api/upload/chinese
@rest_api.route("/api/upload/chinese")
@rest_api.expect(upload_parser)
class ChineseFileUpload(Resource):
    def post(self):
        args = upload_parser.parse_args()
        file = args.get('file')
        unique_filename = str(f"{uuid.uuid4()} _ { file.filename}")
        file.save(os.path.join(UPLOAD_FOLDER, unique_filename))
        uploaded_chinese_files.append(unique_filename)
        return "Chinese Document Uploaded"


# /api/review
@rest_api.route('/api/review')
class Review(Resource):
    def get(self):
        if not uploaded_chinese_files or not uploaded_english_files:
            return 'No uploaded files to download', 404
        english_file_path = os.path.join(UPLOAD_FOLDER, uploaded_english_files[0])
        chinese_file_path = os.path.join(UPLOAD_FOLDER, uploaded_chinese_files[0])
        
        if not os.path.exists(english_file_path) or not os.path.exists(chinese_file_path):
            return 'Uploaded files not found', 404
        
        kfs = Reviewer(english_file_path, chinese_file_path)
        try:
            highlited_file = kfs.start_review()
            return {"docx_file": highlited_file}
        except Exception as e:
            return str(e), 500
    
# /api/download/filename 
@rest_api.route('/api/download/<string:filename>')
class Download(Resource):
    def get(self, filename):
        app_path = os.path.abspath(os.path.dirname(__file__))
        parent_folder = os.path.dirname(app_path)
        file_path = os.path.join(parent_folder, "uploads/output/", filename)
        if os.path.exists(file_path):
            try:
                return send_file(file_path, as_attachment=True)
            except Exception as e:
                return jsonify({"error": f"Error sending the file: {e}"}), 500
        else:
            return jsonify({"error": "File not found"}), 404