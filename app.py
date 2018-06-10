from flask import Flask, jsonify

import db

app = Flask(__name__)

conn = db.connect('sensors.sql')

@app.route('/')
def home():
    return 'it works!'

@app.route('/ir', methods=['GET'])
def ir():
    return jsonify(db.get_latest(conn, 'ir', 12))


app.run(host='0.0.0.0', port=5000)