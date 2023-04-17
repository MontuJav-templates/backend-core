from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=['http://localhost:3000'])

@app.route('/process-las', methods=['POST'])
def process_las():
    file = request.files['file']
    # Process the file here, e.g. save it to disk, parse it, etc.
    print(f"Processed file\n{file}")
    # Send a response back to the client
    response = {'status': 'success'}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
