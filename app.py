import uuid

import requests
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


ICANHAZDADJOKE_HEADERS = {'Accept': 'application/json'}
ICANHAZDADJOKE_URL = 'https://icanhazdadjoke.com'


class JokeSet(db.Model):
    id = db.Column(db.String(32), primary_key=True)
    jokes = db.Column(db.Text)


def get_joke():
    response = requests.get(ICANHAZDADJOKE_URL, headers=ICANHAZDADJOKE_HEADERS)
    return response.json().get('joke', '')


def get_jokes_as_string(number_of_jokes):
    jokes = [f'{i+1}. {get_joke()}' for i in range(number_of_jokes)]
    return '<br>'.join(jokes)


@app.route('/get_jokes/<int:number_of_jokes>')
def get_jokes(number_of_jokes):
    return get_jokes_as_string(number_of_jokes)


@app.route('/save_jokes/<int:number_of_jokes>')
def save_jokes(number_of_jokes):
    jokeset_id = uuid.uuid4().hex
    jokes = get_jokes_as_string(number_of_jokes)
    db.session.add(JokeSet(id=jokeset_id, jokes=jokes))
    db.session.commit()
    return jokeset_id


if __name__ == '__main__':
    db.create_all()
