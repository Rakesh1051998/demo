# importing flask module
from flask import Flask

# initializing a variable of Flask
app = Flask(__name__)


# decorating index function with the app.route
@app.route('/')
def index():
   return "WELCOME!!! This is the home page"

@app.route('/home')
def home():
    # Render the page
    return "This Is Home Page"


@app.route('/chkurl')
def chkurl():
    # Render the page
    return "This Is chkurl Page"

if __name__ == "__main__":
   app.run()