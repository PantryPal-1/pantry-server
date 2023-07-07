"""API"""
from flask import Flask, request
import pandas as pd

app = Flask(__name__)


# @app.route("/rec", methods=["GET"])
# def rec_recipe():
#     # run model
#     return "result", 200


@app.route("/rec", methods=["POST"])
def rec_recipe():
    res = []
    only_ingr = request.args.get("onlyi", type=bool)
    ingredients_input = request.json["ingredients"]
    # ingredients = ingredients["ingredients"]
    if only_ingr:
        df = pd.read_csv("input/df_parsed.csv")
        pattern = "(?:" + " ".join([f"(?i){i}" for i in ingredients_input])
        print(type(df["ingredients_parsed"].str.lower()))
        # print(df[df["ingredients"].str.contains(pattern)])
        res = df[df["ingredients"].str.contains(pattern)]
    return res.to_json(), 200
