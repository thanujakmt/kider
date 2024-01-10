
from Application import app
from flask import render_template

@app.route("/", methods = ["POST","GET"])
def home():
    return render_template("home.html")

@app.route("/aboutus", methods = ["POST","GET"])
def aboutus():
    return render_template("about_us.html")

@app.route("/classes", methods = ["POST","GET"])
def classes():
    return render_template("classes.html")

@app.route("/pages", methods = ["POST","GET"])
def pages():
    return render_template("pages.html")

@app.route("/contactus", methods = ["POST","GET"])
def contactus():
    return render_template("contactus.html")