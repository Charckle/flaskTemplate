from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Lenght

class NewLocation(FlaskForm):
    username     = StringField('Username', [Length(min=4, max=25)])
    email        = StringField('Email Address', [Length(min=6, max=35)])
    accept_rules = BooleanField('I accept the site rules', [InputRequired()])