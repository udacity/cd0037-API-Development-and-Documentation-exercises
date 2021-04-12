# Import your dependencies
from flask import Flask, jsonify

# Define the create_app function
def create_app(test_config=None):
    # Create and configure the app
    # Include the first parameter: Here, __name__is the name of the current Python module.
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return jsonify({'message':'HELLO, WORLD!'})

    @app.route('/smiley')
    def smiley():
        return ':)'

    return app