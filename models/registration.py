from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Email, DataRequired, Length, Regexp, EqualTo

class Registration(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=5, max=128)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=5, max=128)])
    username = StringField('User Name', validators=[DataRequired(), Length(min=5, max=128)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Regexp("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&_])[A-Za-z\d@$!%*?&_]{8,32}$")
            ])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo("password")])


    submit = SubmitField('Sign Up')