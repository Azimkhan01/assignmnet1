
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/new-feature')
def new_feature():
    return "This is a new feature!"

if __name__ == "__main__":
    app.run(debug=True)
