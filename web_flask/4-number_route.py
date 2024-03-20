#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_holberton():
    """Returns Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Returns HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def cisfun(text):
    """Returns C, followed by the value of the text variable"""
    text = text.replace("_", " ")
    return "C " + text


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythoniscool(text="is cool"):
    """Returns Python, followed by the value of the text variable"""
    text = text.replace("_", " ")
    return "Python " + text


@app.route("/number/<int:n>", strict_slashes=False)
def nisint(n):
    """Returns n is a number, only if n is an integer"""
    return "%d is a number" % n


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
