"""API"""
from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)


@app.route("/rec", methods=["POST"])
def rec_recipe():
    """recommends recipe based on ingredients list.

    Query parameters:
        - onlyi, checks if the user wants the recipe recommendation to only have their inputed ingredients
    """
    res = []
    only_ingr = request.args.get("onlyi", type=bool)
    ingredients_input = request.json["ingredients"]
    if only_ingr:
        df = pd.read_csv("input/recipes.csv")
        pattern = "(?:" + " ".join([f"(?i){i}" for i in ingredients_input]) + ")"
        res = df[df["ingredients"].str.contains(pattern)]
    else:
        df = pd.read_csv("input/recipes.csv")
        pattern = "|".join([f"(?i){i}" for i in ingredients_input])
        res = df[df["ingredients"].str.contains(pattern)]
    return res.to_json(), 200
