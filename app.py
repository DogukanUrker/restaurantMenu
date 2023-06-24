from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    foods = []
    drinks = []
    desserts = []
    for i in open("products/foods.txt", "r"):
        foods.append(i.strip("\n").split("//"))
    for i in open("products/drinks.txt", "r"):
        drinks.append(i.strip("\n").split("//"))
    for i in open("products/desserts.txt", "r"):
        desserts.append(i.strip("\n").split("//"))
    return render_template("index.html", foods=foods, drinks=drinks, desserts=desserts)


if __name__ == "__main__":
    app.run()
