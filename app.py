from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)    #reference to this file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('map.html')


@app.route("/<name>")
def home(name):
    return f"Hello {name}!"

@app.route("/admin/")
def admin():
    return redirect(url_for("home", name="Admin!"))


@app.route('/sdfsfd')
def indexx():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return "There was a problem adding your task"
    else:
        tasks = Todo.querry.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)

if __name__ == "__main__":
    app.run(debug=True)
