from flask import Flask, request, jsonify
from fileRouter import FileRouter
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

file_key = "file"

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files[file_key]
    if type(file.filename) != str or len(file.filename) <= 0:
        return jsonify({"error": 'No file selected'}), 400
    sentences = FileRouter.run(file)
    return jsonify({"sentences": sentences})

if __name__ == '__main__':
    app.run(debug=True)