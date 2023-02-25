from flask import render_template
from app import app

@app.route('/')
def index():
    cdn={
        'instructors':('lucas','dylan'),
        'students':['connor','blane','martin']
    }
    return render_template('index.jinja',title='home', instructors=cdn['instructors'], students=cdn['students'])