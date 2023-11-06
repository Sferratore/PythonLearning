from flask import Flask
from flask import request 

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the '/hello' URL
@app.route('/hello')
def hello():
    # Retrieve the 'name' query parameter from the request; default to 'Nobody' if not provided
    name = request.args.get('name', 'Nobody')
    
    # Construct a greeting message using the retrieved 'name'
    greeting = f"Hello, {name}!"
    
    return greeting

# Run the Flask app when executed as the main script
if __name__ == "__main__":
    app.run()

