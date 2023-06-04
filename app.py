from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb+srv://cgj0079:00791004@cluster0.p6xynpw.mongodb.net/')
db = client['science']
collection = db['name']


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/save', methods=['POST'])
def save_value():
    value = request.form['value']
    # 여기에서 받은 값을 MongoDB에 저장하거나 다른 처리를 수행합니다.
    collection.insert_one({'value': value})
    return '값이 성공적으로 저장되었습니다.'


if __name__ == '__main__':
    app.run()
