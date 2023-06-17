from flask import Flask, render_template, redirect
from json import load

app = Flask(__name__)


@app.route("/")
def index():
    data = load(open("products.json"))
    return render_template(
        "index.html",
        cato=data,
        foods=data["foods"],
        drinks=data["drinks"],
        desserts=data["desserts"],
        foodsPrice=data["desserts"].values(),
        drinksPrice=data["drinks"].values(),
        dessertsPrice=data["desserts"].values(),
    )

if __name__ == "__main__":
    app.run(debug=True)
