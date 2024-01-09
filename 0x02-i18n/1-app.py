#!/usr/bin/env python3
"""
Flask app with Babel configuration for language support.
"""
from flask import Flask, render_template
from flask_babel import Babel

# Configuration class for Babel
class BabelConfig(object):
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(BabelConfig)
babel = Babel(app)

# Route for the home page
@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Renders the template for the home page.
    """
    return render_template('1-index.html')

if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)

