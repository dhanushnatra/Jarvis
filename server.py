from flask import Flask,url_for, request, jsonify, send_from_directory
from flask_cors import CORS
from flask import render_template

app = Flask(__name__)

CORS(app)

@app.route('/')
def index():
    return render_template('jarvis.html')


@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

