from flask import Flask, render_template, request, redirect, session
from json import load
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(32)


@app.route("/")
def index():
    return render_template(
        "index.html",
        foods=load(open("products/foods.json")),
        drinks=load(open("products/drinks.json")),
        desserts=load(open("products/desserts.json")),
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


if __name__ == "__main__":
    app.run(debug=True)
