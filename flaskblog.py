from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'secretkey'

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

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
    	flash('Accound created for {}! success'.format(form.username.data))
    	return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


# Runs in debug mode only if the script is run directly
# This is for development purposes so I don't have to constantly restart the flask server

if __name__ == '__main__':
	app.run(debug=True)