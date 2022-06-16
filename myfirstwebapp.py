from flask import Flask, request, url_for, abort, redirect
from markupsafe import escape
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('static', filename='hello.txt'))

@app.route('/requirements/')
def requirements():
    return redirect(url_for('static', filename='requirements.txt'))

@app.route('/generate-users/int<count>')
def generate_users(count):
    return 'fake users list'

@app.route('/mean/')
def generate():
    return 'converted weight and height'

@app.route('/space/')
def space():
    return 'number of austronauts'
