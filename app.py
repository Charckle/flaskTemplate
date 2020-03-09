from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import models

app = Flask(__name__)    #reference to this file
app.config.from_object("config.DevelopmentConfig")
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
