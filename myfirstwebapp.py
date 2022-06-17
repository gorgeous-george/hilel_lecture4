from flask import Flask, request, url_for, abort, redirect, jsonify
from markupsafe import escape
from faker import Faker
import requests

app = Flask(__name__)
fake = Faker()

@app.route('/')
def index():
    return redirect(url_for('static', filename='hello.txt'))

@app.route('/requirements/')
def requirements():
    with open("requirements.txt", encoding='utf-8') as f:
        result = [line[:-1] for line in f]
    return jsonify(result)

@app.route('/generate-users/', methods=['GET'])
def generate_users():
    result = {}
    count = request.args.get('count',type=int)
    if not count:
        count = 100
    for _ in range(count):
        name = fake.unique.first_name()
        mail = fake.email()
        result[name] = mail
    return result

@app.route('/mean/')
def generate():
    return 'converted weight and height'

@app.route('/space/')
def space():
    return 'number of astronauts'
