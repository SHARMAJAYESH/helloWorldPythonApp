from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p> Hello, World! </p>"

@app.route("/jayesh")
def hello_jayesh():
    return "<p> Hello, World! . Jayesh this side </p>"