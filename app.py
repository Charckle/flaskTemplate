from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)    #reference to this file
app.config.from_object("config.DevelopmentConfig")
db = SQLAlchemy(app)



@app.route('/')
def index():
    return render_template('index.html')

# Set the route and accepted methods
@app.route('/login/', methods=['GET', 'POST'])
def login():

    # If sign in form is submitted
    form = LoginForm(request.form)

    # Verify the sign in form
    if form.validate_on_submit():

        user = User.query.filter_by(username=form.username_or_email.data).first()
        if not user:
            user = User.query.filter_by(email=form.username_or_email.data).first()

        if user and user.check_password(form.password.data):

            session['user_id'] = user.id

            flash('Welcome %s' % user.name, 'success')
            
            return redirect(url_for('app.index'))

        flash('Wrong email or password', 'error')
    
    try:
        if(session['user_id']):
            return redirect(url_for("app.index"))
    
    except:
        return render_template("/auth/login.html", form=form)
        

@app.route('/logout/')
def logout():
    session.pop("user_id", None)
    
    flash('You have been logged out. Have a nice day!', 'success')

    return redirect(url_for("app.login"))

# Set the route and accepted methods
@app.route('/register/', methods=['GET', 'POST'])
def register():
    #insert check, if the user is already logged in
    form = RegisterForm(request.form)
    print(form.username.data)
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password = form.password.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        
        flash('Congratulations, you are now a registered user!', 'success')
        
        return redirect(url_for('app.login'))
    return render_template('auth/register.html', title='Register', form=form)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

if __name__ == "__main__":
    db.create_all()
    app.run()
