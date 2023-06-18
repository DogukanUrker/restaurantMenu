from flask import Flask, render_template, redirect
from json import load

app = Flask(__name__)


@app.route("/")
def index():
    return render_template(
        "index.html",
        foods=load(open("products/foods.json")),
        drinks=load(open("products/drinks.json")),
        desserts=load(open("products/desserts.json")),
    )


if __name__ == "__main__":
    app.run(debug=True)
