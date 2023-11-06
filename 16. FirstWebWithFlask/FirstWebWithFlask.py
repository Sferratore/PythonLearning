# Import the Flask class from the flask module
from flask import Flask

# Create a Flask web application instance and give it the name of the current module
app = Flask(__name__)

# Define a route for the root URL ('/') that responds with "Hello, world!"
@app.route('/')
def hello_world():
    return "Hello, world!"

# Define another route for '/sayhi' that responds with "Hi!"
@app.route('/sayhi')
def sayhi():
    return "Hi!"

# Check if this script is the main program being run (not imported as a module)
if __name__ == '__main__':
    # Start the Flask application on the built-in development server
    app.run()
