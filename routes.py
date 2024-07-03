import models
from flask import Flask, render_template, flash, redirect, url_for, request
from flask_login import login_user, current_user, logout_user, login_required
from models.registration import Registration
from models.specialization import Specialization
from models.login import Login, updateProfile
from models.login import Login
from models.patient import Patient
from models.search import Search
from models.doctor import Doctor
from models.location import Location
from models.base_model import db
from __init__ import app, bcrypt

@app.route("/")
@app.route("/home", methods=['GET', 'POST'])
def homePage():
    """
    Render the home page and handle form submissions for filtering doctors.

    Explanation:
        - IF the request method is 'GET', The browser send get request to get the html and css files.
        - IF the request method is 'POST', The user sends filtration data to the server,
          and the server processes this data to return the appropriate response.

    Returns:
        - Home page if type of request method is GET,
        - A redirection to the appropriate search method if the request method is 'POST'.
    """
    form = Search()
    if request.method == 'POST':
        specialization_input = form.specialization.data
        location_input = form.location.data


        if specialization_input == 'All specializations' and location_input == 'All locations':
            return redirect(url_for('search_all'))

        elif specialization_input == 'All specializations' and location_input != 'All locations':
            return redirect(url_for('search_by_location', location=location_input))

        elif specialization_input != 'All specializations' and location_input == 'All locations':
            return redirect(url_for('search_by_specialization', specialization=specialization_input))

        else:
            return redirect(url_for('search', specialization=specialization_input, location=location_input))
    return render_template("home.html", search_form=form)

@app.route('/search')
def search_all():
    """
    Return all doctors
    """

    all_doctors = models.storage.all(Doctor).values()
    lenght = len(all_doctors)
    return render_template('search_results.html', doctors=all_doctors, lenght=lenght)


# don't forget remove the space between words in the uri 'South Siani'
@app.route('/search/location/<location>')
def search_by_location(location):
    """
    Filter doctors by location.
    
    Keyword arguments:
        location -- The location name to filter doctors by.
    
    Returns:
        Rendered HTML template displaying all doctors in the specified location.
    """
    location_odj = Location.query.filter_by(location_name=location).first()
    matched_doctors = Doctor.query.filter_by(location_id=location_odj.id).all()
    return render_template('search_results.html', doctors=matched_doctors)

@app.route('/search/specialization/<specialization>')
def search_by_specialization(specialization):
    """
    Filter doctors by specialization

    Keyword arguments:
        specialization -- The specialization name to filter doctors by.

    Return:
        Rendered HTML template displaying all doctors with specified specialization.
    """

    specialization_obj = Specialization.query.filter_by(specialization_name=specialization).first()
    matched_doctors = Doctor.query.filter_by(specialization_id=specialization_obj.id).all()
    return render_template('search_results.html', doctors=matched_doctors)

@app.route('/search/<specialization>/<location>', methods=['GET'])
def search(specialization, location):
    """
    Filter doctors by location and specialization

    Keyword arguments:
        specialization -- The specialization name to filter doctors by.
        location -- The location name to filter doctors by.

    Return:
        Rendered HTML template displaying all doctors
        with specified specialization in the specified location.
    """

    specialization_obj = Specialization.query.filter_by(specialization_name=specialization).first()
    location_obj = Location.query.filter_by(location_name=location).first()
    matched_doctors = Doctor.query.filter(
        Doctor.location_id == location_obj.id,
        Doctor.specialization_id == specialization_obj.id
    ).all()
    return render_template('search_results.html', doctors=matched_doctors)

@app.route('/doctor/<int:doctor_id>')
def doctor_profile(doctor_id):
    doctors = Doctor.query.filter_by(doctor_id=doctor_id)
    doctor = next((doc for doc in doctors), None)
    if doctor:
        return render_template('doctor_profile.html', doctor=doctor)
    else:
        return "Doctor not found", 404 

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
    image_filename = current_user.images.decode() if isinstance(current_user.images, bytes) else current_user.images
    image_file = url_for('static', filename=f'user_images/{image_filename}') if image_filename else None
    return render_template("profile.html", title='Profile', image_file=image_file)

@app.route('/settings', methods=['GET', 'POST'])
@login_required
def settings(): 
    form = updateProfile()
    if form.validate_on_submit():
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        db.session.commit()
        flash("Your profile has been updated", "success")
        return redirect(url_for('profile'))
    elif request.method == 'GET':
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.email.data = current_user.email
    image_filename = current_user.images.decode() if isinstance(current_user.images, bytes) else current_user.images
    image_file = url_for('static', filename=f'user_images/{image_filename}') if image_filename else None
    return render_template("settings.html", title='settings', form=form, image_file=image_file)


if __name__ == "__main__":
    app.run(debug=True)
