#!/usr/bin/env python3
"""Flask app"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def index():
    """Render the template"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
