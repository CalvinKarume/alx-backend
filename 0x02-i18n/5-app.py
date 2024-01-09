#!/usr/bin/env python3
"""
Flask app with user handling, Babel configuration for language support, and dynamic locale selection.
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel

# User data dictionary
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

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

def get_user():
    """
    Returns user dictionary or None if ID value is not found or 'login_as' URL parameter is missing.
    """
    user_id = request.args.get('login_as', None)
    if user_id is not None and int(user_id) in users.keys():
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
    Selects and returns the best language based on user preference or the request's language header.
    """
    selected_locale = request.args.get('locale')
    if selected_locale in app.config['LANGUAGES']:
        return selected_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/', strict_slashes=False)
def handle_root_route() -> str:
    """
    Handles the root route.
    """
    return render_template('5-index.html')

if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)

