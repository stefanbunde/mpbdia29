import requests
from flask import Flask, jsonify


app = Flask(__name__)


ICANHAZDADJOKE_HEADERS = {'Accept': 'application/json'}
ICANHAZDADJOKE_URL = 'https://icanhazdadjoke.com'


def get_joke():
    response = requests.get(ICANHAZDADJOKE_URL, headers=ICANHAZDADJOKE_HEADERS)
    return response.json().get('joke', '')


@app.route('/get_jokes/<int:number_of_jokes>')
def get_jokes(number_of_jokes):
    jokes = [f'{i+1}. {get_joke()}' for i in range(number_of_jokes)]
    return '<br>'.join(jokes)
