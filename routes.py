from flask import Flask, render_template, flash, redirect, url_for, request
from models.registration import Registration
from models.login import Login
from models.patient import Patient
from models.search import Search
from models.doctor import Doctor
from models.location import Location
from flask_login import login_user, current_user, logout_user, login_required
from __init__ import app, bcrypt

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
    if current_user.is_authenticated:
        return redirect(url_for('homePage'))
    colours = ['Male', 'Female']
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
    return render_template("register.html", title="Register", form=form, colours=colours)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('homePage'))

    form = Login()
    if form.validate_on_submit():
        with app.app_context():
            patient = Patient.query.filter_by(email=form.email.data).first()
            if patient and bcrypt.check_password_hash(patient.password, form.password.data):
                login_user(patient, remember=form.remember.data)
                next_page = request.args.get('next')
                flash('You have been logged in successfully!', 'success')
                return redirect((next_page) if next_page else url_for('homePage'))
            else:
                flash('Please check your email or password', 'danger')
    return render_template("login.html", title="Login", form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('homePage'))

@app.route('/profile')
@login_required
def profile():
    return render_template("profile.html", title='Profile')

@app.route('/settings')
@login_required
def settings():
    form = Login()
    return render_template("settings.html", title='settings', form=form)

@app.route('/search')
def search():
    form = Search()
    specialization = form.specialization.data
    location = form.location.data
    location_id = Location.query.filter_by(location=location)
    matched_doctors = Doctor.query.filter_by(specialization=specialization, location_id=location_id)
    return render_template('search_results.html', doctors=matched_doctors)

@app.route('/doctor/<int:doctor_id>')
def doctor_profile(doctor_id):
    doctors = Doctor.query.filter_by(doctor_id=doctor_id)
    doctor = next((doc for doc in doctors), None)
    if doctor:
        return render_template('doctor_profile.html', doctor=doctor)
    else:
        return "Doctor not found", 404 

if __name__ == "__main__":
    app.run(debug=True)