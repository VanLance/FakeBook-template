from flask import render_template, flash, redirect
from app import app
from app.forms import RegisterUserForm

@app.route('/')
def index():
    cdn={
        'instructors':('lucas','dylan'),
        'students':['connor','blane','martin']
    }
    return render_template('index.jinja', title='home', 
        instructors=cdn['instructors'], students=cdn['students'])

@app.route('/about')
def about():
    return render_template('about.jinja')

@app.route('/register', methods=['GET',"POST"])
def register():
    form = RegisterUserForm()
    if form.validate_on_submit():
        print('test')
        flash(f'Register Requested for {form.email} {form.username}')
        return redirect('/')
    return render_template('register.jinja', form=form, title='Register')

@app.route('/login')
def login():
    return render_template('login.jinja')
