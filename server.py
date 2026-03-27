from flask import Flask,url_for, request, jsonify, send_from_directory
from flask_cors import CORS
from flask import render_template

app = Flask(__name__)

CORS(app)

error_codes=[(400,"Bad Request"), (404,"Not Found"), (500,"Internal Server Error"),(401,"Unauthorized"),(403,"Forbidden")]

for code, message in error_codes:
    @app.errorhandler(code)
    def handle_error(error, code=code, message=message):
        return render_template('error.html', error_code=code, error_message=message), code

@app.route('/')
def index():
    return render_template('jarvis.html')

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

