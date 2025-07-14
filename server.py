from flask import Flask, request, jsonify
from fileRouter import FileRouter
from flask_cors import CORS, cross_origin
import os

from gemini_interface import GeminiInterface

app = Flask(__name__)
CORS(app, origins=["https://legal-whisper-translate.lovable.app"])

file_key = "file"

translate_prompt_key = ""
translate_response_key = ""

@app.route('/upload', methods=['POST', 'OPTIONS'])
@cross_origin(origins=["https://legal-whisper-translate.lovable.app"])
def upload_file():
    if request.method == "OPTIONS":
        return '', 204
    else:
        print(f"Request: {request.method}")
        print(f"Trying to access files: {file_key}")
        file = request.files[file_key]
        print(f"File accessed: {file}")
        if type(file.filename) != str or len(file.filename) <= 0:
            print(f"No file found")
            return jsonify({"error": 'No file selected'}), 400
        print("Running Sentence extractor")
        sentences = FileRouter.run(file)
        print(f"Sentences: {sentences}")
        if os.path.exists(file.filename):
            os.remove(file.filename)
        return jsonify({"sentences": sentences}), 200
    
@app.route('/translate', methods=['POST', 'OPTIONS'])
@cross_origin(origins=["https://legal-whisper-translate.lovable.app"])
def translate():
    if request.method == "OPTIONS":
        return '', 204
    else:
        prompt = request.form.get(translate_prompt_key)
        retList = GeminiInterface.run(prompt)
        ret_data = {}
        ret_data[] = retList
        return jsonify(ret_data), 200

if __name__ == '__main__':
    app.run(debug=True)