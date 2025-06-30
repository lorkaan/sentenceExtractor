from flask import Flask, request, jsonify
from fileRouter import FileRouter
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, origins=["https://legal-whisper-translate.lovable.app"])

file_key = "file"

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
        return jsonify({"sentences": sentences}), 200

if __name__ == '__main__':
    app.run(debug=True)