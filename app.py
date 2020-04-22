import os
from flask import flask

app = flask(__name__)

@app.route("/")

def main():
    return "Welcome"

if __name__ ==  "__main":
    app.run()
