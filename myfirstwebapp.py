from flask import Flask, request, url_for, redirect, jsonify
from faker import Faker
import requests
import csv

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
    count = request.args.get('count', type=int)
    if not count:
        count = 100
    for _ in range(count):
        name = fake.unique.first_name()
        mail = fake.email()
        result[name] = mail
    return result


@app.route('/mean/')
def average():
    result = {}
    with open('static/hw.csv') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        h_sum = 0
        w_sum = 0
        rows_count = 0
        for row in reader:
            h_sum += float(row[' "Height(Inches)"'])
            w_sum += float(row[' "Weight(Pounds)"'])
            rows_count += 1
        result['height_average(cm)'] = h_sum / rows_count * 2.54
        result['weight_average(kg)'] = w_sum / rows_count / 2.205
    return result


@app.route('/space/')
def space():
    return 'number of astronauts'
