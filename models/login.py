from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length, ValidationError
from models.patient import Patient
from flask_login import current_user
from __init__ import app

class Login(FlaskForm):
    email = StringField(
        'Email',
        validators=[DataRequired(), Email()],
        render_kw={'placeholder': 'Email'}
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired()],
        render_kw={'placeholder': 'Password'}
    )
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class updateProfile(FlaskForm):
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
        render_kw={
            "placeholder": "Email",
            "readonly": True
        }
    )
    image = FileField(
        "Update Profile Picture", validators=[FileAllowed(["jpg", "png"])]
    )
    submit = SubmitField('Update')

    def validate_email(self, email):
        with app.app_context():
            if email.data != current_user.email:
                patient_email = Patient.query.filter_by(email=email.data).first()
                if patient_email:
                    raise ValidationError('Email already exists! Please try another one')
