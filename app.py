from flask import Flask,render_template,redirect
from json import load

app = Flask(__name__)



def fetchMenu():
    products = load(open("products.json"))
    return products["foods"],products["drinks"],products["desserts"]


@app.route("/")
def index():
    return render_template("index.html",menu = fetchMenu())


if __name__ == "__main__":
    app.run(debug=True)