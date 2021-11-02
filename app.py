from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

from pymongo import MongoClient
import requests

client = MongoClient('3.36.69.145', 27017, username="아이디", password="비밀번호")
db = client.dbsparta_plus_week2

@app.route('/')
def home():
    return render_template('index.html')

## 로그인 페이지
@app.route('/api/main/<id>')
def login(id):
    return render_template('main.html',Userid=id)

## 회원가입 페이지
@app.route('/api/signup')
def signup():
    return render_template('signup.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)


