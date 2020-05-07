from flask import Flask
from flask import  jsonify
from flask import request
import random
from flask_sqlalchemy import SQLAlchemy
from ML_module import get_rez
import psycopg2
from conf import db,app

db.create_all()
print('started')
@app.route('/')
def hello_world():
    print(1)
    return 'Hello, World!'

@app.route('/get_prob/url',methods=['GET', 'POST'])
def get_prob_url():
    url=request.args.get('url')
    app.logger.debug(url)
    return jsonify(get_rez(url)
    ), 200


@app.route('/get_prob/url/<url>')
def get_prob_url1(url):
    return jsonify(
        get_rez(url)
    ), 200




@app.route('/get_prob/text',methods=['GET', 'POST'])
def get_prob_text():
    return jsonify(
        {
            "text":request.args.get('text'),
            "prob": random.random()
        }
    ), 200

@app.route('/get_prob/text/<text>')
def get_prob_text1(text):
    return jsonify(
        {
            "text":text,
            "prob": random.random()
        }
    ), 200

if __name__ == "__main__":
    app.run(port='8080', host='0.0.0.0')