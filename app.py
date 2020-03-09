from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from wtforms import Form, BooleanField, StringField, validators
import db

app = Flask(__name__)    #reference to this file

db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/nova_lokacija')
def nova_lokacija():
    
    
    return render_template('nova_lokacija.html')


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
