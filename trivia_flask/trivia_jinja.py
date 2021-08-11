#!/usr/bin/python3
from flask import Flask
from flask import redirect
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/answer/<answer>")
          #"/<string: answer>" <-- this is what you had.
                                  #I took away <string: because it's not needed and was causing the error.
                                  #let me confirm, but if you don't specify <int: or <float:, the variable will always be a string

def answer_question(answer):
    if answer == 4:
        return render_template("trivia.html", choice = answer)
    else:
        return render_template(


def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
