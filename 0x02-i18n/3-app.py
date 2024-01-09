#!/usr/bin/env python3
"""
Flask application with internationalization support through Babel.
"""
from flask import Flask, render_template, request
from flask_babel import Babel

class BabelConfigurations(object):
    """
    Configuration settings for Babel localization.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(BabelConfigurations)
babel = Babel(app)

@babel.localeselector
def determine_best_locale():
    """
    Selects and returns the most appropriate language based on supported options.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/', strict_slashes=False)
def handle_root_route() -> str:
    """
    Processes the root route and renders the associated template.
    """
    return render_template('3-index.html')

if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)

