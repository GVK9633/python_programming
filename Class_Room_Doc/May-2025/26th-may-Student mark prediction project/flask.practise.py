from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello, World!'
app.run(debug=True, host='127.0.1', port=5000)
# To run this Flask application, save the code in a file named `flas.practise.py`