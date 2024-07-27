from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Email, DataRequired, Length, Regexp, EqualTo, ValidationError
from models.patient import Patient
from models.base_model import db
from __init__ import app

class Registration(FlaskForm):
    first_name = StringField(
        'First Name',
        validators=[DataRequired(), Length(min=5, max=128)],
        render_kw={"placeholder": "First Name"}
    )
    last_name = StringField(
        'Last Name',
        validators=[DataRequired(), Length(min=5, max=128)],
        render_kw={"placeholder": "Last Name"}
    )
    email = StringField(
        'Email',
        validators=[DataRequired(), Email()],
        render_kw={"placeholder": "Email"}
    )
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Regexp("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&_])[A-Za-z\d@$!%*?&_]{8,32}$")
        ],
        render_kw={"placeholder": "Password"}
    )
    confirm_password = PasswordField(
        'Confirm Password',
        validators=[DataRequired(), EqualTo("password")],
        render_kw={"placeholder": "Confirm Password"}
    )

    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign Up')

    def validate_email(self, email):

        with app.app_context():
            patient_email = Patient.query.filter_by(email=email.data).first()
            print(patient_email)
            print(email.data)
            if patient_email:
                raise ValidationError('Email already exist! Please try another one')
