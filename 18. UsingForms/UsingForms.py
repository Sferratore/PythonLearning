from flask import Flask
from flask import render_template 
from flask import request 

# Create a Flask application instance and specify the template folder as the current directory
app = Flask(__name__, template_folder=".")

# Define a route for the '/hello' URL that accepts both GET and POST requests
@app.route("/hello", methods=["GET", "POST"])
def index():
    # Check the request method
    if request.method == "POST":
        # If it's a POST request, return a personalized greeting based on the 'name' field in the form
        return f"Hello, {request.form['name']}"
    else:
        # If it's a GET request, render the HTML template "index.html"
        return render_template("index.html")
    
# Run the Flask app when executed as the main script
if __name__ == "__main__":
    app.run()