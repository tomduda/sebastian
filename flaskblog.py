from flask import Flask
app = Flask(__name__)

# Routing

@app.route("/")
@app.route("/home")
def home():
    return "<h1>Sebastian's Homepage</h1>"

@app.route("/about")
def about():
    return "<h1>Sebastian's About Page</h1>"

# Runs in debug mode only if the script is run directly
# This is for development purposes so I don't have to constantly restart the flask server

if __name__ == '__main__':
	app.run(debug=True)