"""API"""
from flask import Flask, request
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
        df = pd.read_csv("input/df_parsed.csv")
        pattern = "(?:" + " ".join([f"(?i){i}" for i in ingredients_input])
        print(type(df["ingredients_parsed"].str.lower()))
        res = df[df["ingredients"].str.contains(pattern)]
    return res.to_json(), 200
