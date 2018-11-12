import sqlite3

conn = sqlite3.connect('data.db')
from flask import Flask

app = Flask(__name__)

@app.route('/post/lots')
def post_lots():
    content = request.get_json()
    return content

