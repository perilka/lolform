from app import app
from flask import render_template, request, redirect, url_for

@app.route('/')
def form():
    return render_template("form.html")

@app.route("/submit", methods=["POST", "GET"])
def submit():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        return render_template("result.html", name=name, email=email)
    else:
        return redirect(url_for("form"))