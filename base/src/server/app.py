from flask import Flask, request, jsonify
from flask_cors import CORS

from modules.las.las_handler import LAS_Handler

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Set max content length to 16 MB
CORS(app, origins=['http://localhost:3000'])

las_handler = None

@app.route('/process-las', methods=['POST'])
def process_las():
    file = request.files['file']
    try:
        # Process the file here, e.g. save it to disk, parse it, etc.
        las_handler = LAS_Handler(file)
        las_handler.test_las_file()
        # Send a response back to the client
        response = {'status': 'success'}
    except Exception as e:
        response = {'status': 'fail'}
        print(f"Unhandled exception of type {type(e)}\n{e}")

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
