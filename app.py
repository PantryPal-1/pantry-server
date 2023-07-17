"""API"""
from flask import Flask, request, jsonify
import pandas as pd
import pickle

app = Flask(__name__)


@app.route("/rec", methods=["POST"])
def rec_recipe():
    """recommends recipe based on ingredients list.

    Query parameters:
        - onlyi, checks if the user wants the recipe recommendation to only have their inputed ingredients
    """
    res = []
    only_ingr = request.args.get("onlyi", type=bool)
    use_rec = request.args.get("use_rec", type=bool)
    n_recs = request.args.get("n", type=int)
    if not n_recs:  # set default
        n_recs = 10
    ingredients_input = request.json["ingredients"]
    if only_ingr:
        df = pd.read_csv("input/recipes.csv")
        pattern = "(?:" + " ".join([f"(?i){i}" for i in ingredients_input]) + ")"
        res = df[df["ingredients"].str.contains(pattern)]
    elif use_rec:
        i_list_str = " ".join((ingredients_input))
        cosine_rec = pickle.load(open("input/rec.pkl", "rb"))
        input_df = pd.DataFrame(
            list(zip([i_list_str], [i_list_str])),
            columns=["ingredients", "recipe_names"],
        )
        pipeline = pickle.load(open("input/pipeline.pkl", "rb"))
        input = pipeline.transform(input_df)
        output = cosine_rec.predict(input, n_recs)
        print(n_recs, flush=True)
        res = output
    else:
        df = pd.read_csv("input/recipes.csv")
        pattern = "|".join([f"(?i){i}" for i in ingredients_input])
        res = df[df["ingredients"].str.contains(pattern)]
    return res.to_json(), 200
