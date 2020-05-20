from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)

bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)
    # return render_template('user.htm', name=name)


@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'), 500

'''
Could just create 2 new templates for 404.html and 500.html based on user.html
and just change header to display the error message. But there will
be a lot of duplicated code. Instead we can define our own base template base.html
still derived from (iherits from) bootstrap/base.html, with uniform page layout,
nav bar etc, and leave the page content to be defined in more derived templates.
So the new templates/base.html is the base for other templates such as templates/user.html
templates/404.html and templates/500.html

'''