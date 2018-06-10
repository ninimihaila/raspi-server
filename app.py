from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'it works!'

@app.route('/ir', methods=['GET'])
def ir():
    return 'ir!'


app.run(host='0.0.0.0', port=5000)