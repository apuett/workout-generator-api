from dotenv import load_dotenv
import os

from flask import Flask

load_dotenv()
Mongo_URI = os.getenv("MONGO_URI")

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"
