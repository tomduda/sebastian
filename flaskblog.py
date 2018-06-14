from flask import Flask, render_template
app = Flask(__name__)

posts = [
	{
		'author': 'Thomas Duda',
		'title': 'Blog Poast 1',
		'content': 'First post content',
		'date_posted': 'June 14, 2018'
	},
	{
		'author': 'Sabastian Duda',
		'title': 'Blog Poast 2',
		'content': 'Second post content',
		'date_posted': 'June 15, 2018'
	}

]

# Routing

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title="About")

# Runs in debug mode only if the script is run directly
# This is for development purposes so I don't have to constantly restart the flask server

if __name__ == '__main__':
	app.run(debug=True)