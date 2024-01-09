#!/usr/bin/env python3
"""
Flask app with Babel configuration for language support, user handling, and dynamic locale selection.
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Dict, Union

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

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user() -> Union[Dict, None]:
    """
    Returns user dictionary or None if ID value is not found or 'login_as' URL parameter is missing.
    """
    user_id = request.args.get('login_as', None)
    if user_id and int(user_id) in users.keys():
        return users.get(int(user_id))
    return None

@app.before_request
def before_request():
    """
    Adds user to flask.g if user is found.
    """
    user = get_user()
    g.user = user

@babel.localeselector
def determine_best_locale():
    """
    Selects and returns the best language based on user preference, request headers, or the language header.
    """
    selected_locale = request.args.get('locale')
    if selected_locale and selected_locale in app.config['LANGUAGES']:
        return selected_locale
    if g.user:
        user_locale = g.user.get('locale')
        if user_locale and user_locale in app.config['LANGUAGES']:
            return user_locale
    header_locale = request.headers.get('locale', None)
    if header_locale and header_locale in app.config['LANGUAGES']:
        return header_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/', strict_slashes=False)
def handle_root_route() -> str:
    """
    Handles the root route.
    """
    return render_template('5-index.html')

if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)

