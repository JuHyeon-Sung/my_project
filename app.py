from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.my_project


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/drawHobby', methods=['POST'])
def write_hobby():
    hobby_receive = request.form['date', 'hobby_give', 'img_url']

    hobby = {
        'hobby': hobby_receive

    }

    db.hobby.insert_one(hobby)
    return jsonify({'result': 'success', 'msg': '취미가 선정되었습니다.'})


@app.route('/drawHobby', methods=['GET'])
def read_hobby():
    hobby = list(db.hobby.find({}, {'_id': 0}))

    return jsonify({'result': 'success', 'hobby': hobby})


@app.route('/drawHobby/mention', methods=['POST'])
def mention_hobby():
    mention_receive = request.form['hobby_mention']

    mention = {
        'mention': mention_receive
    }

    db.hobby.insert_one(mention)
    return jsonify({'result': 'success', 'mention': mention})


@app.route('/drawHobby/mention', methods=['GET'])
def give_mention():
    mention = list(db.hobby.find({}, {'_id': 0}))

    return jsonify({'result': 'success', 'mention': mention})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
