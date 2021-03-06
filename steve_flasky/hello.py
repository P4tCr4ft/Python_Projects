from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NameForm(FlaskForm) :
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

app.config['SECRET_KEY'] = 'some secret key'


@app.route('/', methods=['GET', 'POST'])
def index() :
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'), current_time=datetime.utcnow())
    # return render_template('index.html', form=form, name=name)


@app.route('/user/<name>')
def user(name) :
    return render_template('user.html', name=name)


# return render_template('user.htm', name=name)


@app.errorhandler(404)
def page_not_found(e) :
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e) :
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
