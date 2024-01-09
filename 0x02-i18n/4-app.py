#!/usr/bin/env python3
"""
Flask application with Babel configuration for language support and dynamic locale selection.
"""
from flask import Flask, render_template, request
from flask_babel import Babel

class BabelConfiguration(object):
    """
    Configuration settings for Babel localization.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(BabelConfiguration)
babel = Babel(app)

@babel.localeselector
def determine_best_locale():
    """
    Selects and returns the best language based on user preference or the request's language header.
    """
    selected_locale = request.args.get('locale')
    if selected_locale in app.config['LANGUAGES']:
        return selected_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/', strict_slashes=False)
def handle_root_route() -> str:
    """
 
