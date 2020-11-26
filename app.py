from flask import Flask, request, redirect, render_template

app = Flask(__name__)


@app.route("/me")
def about_me():
    return render_template("strona1.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("strona2.html")
    elif request.method == "POST":
        print(request.form)
        return redirect("/contact")
