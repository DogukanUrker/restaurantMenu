from flask import Flask, render_template

app = Flask(__name__)


def loadData():
    foods = []
    drinks = []
    desserts = []
    for i in open("products/food.txt", "r"):
        foods.append(i.strip("\n").split("//"))
    for i in open("products/drink.txt", "r"):
        drinks.append(i.strip("\n").split("//"))
    for i in open("products/dessert.txt", "r"):
        desserts.append(i.strip("\n").split("//"))
    return foods, drinks, desserts


@app.route("/")
def index():
    return render_template(
        "index.html", foods=loadData()[0], drinks=loadData()[1], desserts=loadData()[2]
    )


if __name__ == "__main__":
    app.run(debug=True)
