from flask import Flask

# create the Flask application object
app = Flask(__name__)

# a simple in‑memory list to represent available car models
existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']


@app.route('/')
def index():
    """Default route.

    When a user visits the root URL the server returns a short welcome
    message.  The tests expect a 200 status code and the exact phrase
    "Welcome to Flatiron Cars".
    """

    return "Welcome to Flatiron Cars"


@app.route('/<model>')
def model_route(model):
    """Model-specific route.

    The URL variable ``model`` is compared against ``existing_models``.
    If the name is found we confirm that the car is in the fleet, otherwise
    we return a polite failure message.  The function name was changed from
    ``model`` to ``model_route`` to avoid shadowing the parameter and to
    keep linters happy.
    """

    if model in existing_models:
        return f"Flatiron {model} is in our fleet!"
    else:
        return f"No models called {model} exists in our catalog"

if __name__ == '__main__':
    app.run(debug=True)