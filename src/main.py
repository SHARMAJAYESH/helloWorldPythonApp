from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Web App with Python Flask - Dummy one for GCP cloud run test!'

app.run(port=81)