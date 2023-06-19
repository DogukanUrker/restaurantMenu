from flask import Flask, render_template, request, redirect, session
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(32)


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


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form["username"] == "admin" and request.form["password"] == open(
            "adminPassword.txt", "r"
        ).read().strip("\n"):
            session["admin"] = True
            return redirect("/admin")
    return render_template("login.html")


@app.route("/admin")
def admin():
    if "admin" in session:
        return render_template("admin.html")
    return redirect("/login")


if __name__ == "__main__":
    app.run(debug=True)
