"""API"""
from flask import Flask

app = Flask(__name__)


@app.route("/rec", methods=["GET"])
def rec_recipe():
    # run model
    return "result", 200
