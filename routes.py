from flask import Flask, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = '4d297f88daf6623e4fe0df5f62d1e152c2076978af7ae82c4f77006340f256f1'

# Use environment variables to configure your MySQL connection
HBNB_MYSQL_USER = os.getenv('HBNB_MYSQL_USER', 'Name')
HBNB_MYSQL_PWD = os.getenv('HBNB_MYSQL_PWD', 'Password')
HBNB_MYSQL_HOST = os.getenv('HBNB_MYSQL_HOST', 'localhost')
HBNB_MYSQL_DB = os.getenv('HBNB_MYSQL_DB', 'Healixra')

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{HBNB_MYSQL_USER}:{HBNB_MYSQL_PWD}@{HBNB_MYSQL_HOST}/{HBNB_MYSQL_DB}'
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)


@app.route("/")
@app.route("/home")
def homePage():
    return render_template("home.html")

@app.route("/about")
def aboutPage():
    return render_template("about.html")

@app.route("/doctors")
def doctorsPage():
    return render_template("doctors.html")

@app.route("/pages")
def pagesPage():
    return render_template("pages.html")

@app.route("/content")
def contentPage():
    return render_template("content.html")


@app.route("/register", methods=['GET', 'POST'])
def register():
    from models.registration import Registration
    from models.patient import Patient

    form = Registration()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        patient = Patient(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            password=hashed_password
        )
        # save not working if you didn't run the server in the 'db' mode
        patient.save()

        name = form.first_name.data + ' ' + form.last_name.data
        flash(f"Accoun created successfully for {name}", "success")
        return redirect(url_for('login'))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    from models.login import Login
    from models.patient import Patient
    form = Login()
    if form.validate_on_submit():
        patient = Patient.query.filter_by(email=form.email.data).first()
        if patient and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('homePage'))
        else:
            flash('Please check your email or password', 'danger')
    return render_template("login.html", title="Login", form=form)



if __name__ == "__main__":
    app.run(debug=True)
