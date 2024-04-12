from flask import render_template, flash, redirect, url_for
from pustak_bhandar.forms import RegistrationForm, LoginForm
from pustak_bhandar.models import User
from pustak_bhandar import app, db, bcrypt

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/store')
def store():
    return render_template('store.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hash_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hash_password)
        db.session.add(user)
        db.session.commit()
        flash(f"Account created for {form.username.data}! You are now able to log in.", "success")
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data=='aman@gmail.com' and form.password.data=='1234':
            flash(f"Login successful for {form.email.data}", "success")
            return redirect(url_for('account'))
        else:
            flash(f"Login unsuccessful for {form.email.data}", "danger")
            return redirect(url_for('login'))
    return render_template('login.html', form=form)

@app.route('/account')
def account():
    return render_template('account.html')
