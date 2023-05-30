from flask import Flask, redirect, url_for, render_template
import configparser
import requests
app = Flask(__name__)

@app.route("/")
def hello_world():
    for i in range(10):
        return render_template("base.html")

@app.route("/about")
def ab():
    return "<h1> this is the about page <h1>"


if __name__ == "__main__" :
    app.run(host="0.0.0.0", port=5000)