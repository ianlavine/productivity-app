from site import app
from flask import render_template, redirect, url_for, flash, request
from site.models import User
from site.forms import RegisterForm, LoginForm
from site import db
from flask_login import login_user, logout_user, login_required, current_user

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/signup')
def signup_page():
    form = RegisterForm
    if form.validate_on_submit():  #checks if user has pressed the submit button
        user_to_create = User(name=form.name.data, 
                            email_address=form.email_address.data,
                            password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        
        login_user(user_to_create)
        flash(f'Account created successfully! You are logged in as {user_to_create.name}', category='success')
        return redirect(url_for('home_page'))

    if form.errors != {}: #If there are errors from validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')

    return render_template('signup.html', form=form)

@app.route('/login')
def login_page():
    form = LoginForm
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(email_address=form.email_address.data).first()
        if attempted_user and attempted_user.check_password_correction(
            attempted_password=form.password.data
        ):
            login_user(attempted_user)
            flash(f'Success! You are logged in as {attempted_user.name}', category='success')
            return redirect(url_for('market_page'))
        else:
            flash('Username or password is not valid. Please try again', category='danger')

    return render_template('login.html', form=form)