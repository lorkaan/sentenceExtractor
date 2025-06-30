from flask import Flask, request, jsonify
from fileRouter import FileRouter
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["https://legal-whisper-translate.lovable.app"])

file_key = "file"

@app.route('/upload', methods=['POST', 'OPTIONS'])
@cross_origin(origins=["https://legal-whisper-translate.lovable.app"])
def upload_file():
    if request.method == "OPTIONS":
        return '', 204
    else:
        file = request.files[file_key]
        if type(file.filename) != str or len(file.filename) <= 0:
            return jsonify({"error": 'No file selected'}), 400
        sentences = FileRouter.run(file)
        return jsonify({"sentences": sentences}), 200

if __name__ == '__main__':
    app.run(debug=True)