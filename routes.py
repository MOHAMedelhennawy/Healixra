import models
from flask import Flask, render_template, flash, redirect, url_for, request, jsonify
from flask_login import login_user, current_user, logout_user, login_required
from models.registration import Registration
from models.specialization import Specialization
from models.appointment import Appointment
from models.login import Login, updateProfile
from models.login import Login
from models.patient import Patient
from models.search import Search
from models.review import Review, Add_review
from models.doctor import Doctor
from models.location import Location
from models.base_model import db
from datetime import datetime
from __init__ import app, bcrypt
from utils import search_doctors


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
    doctors = Doctor.query.limit(10)
    if request.method == 'POST':
        specialization_input = form.specialization.data
        location_input = form.location.data
        name_input = form.name.data

        if specialization_input == 'All specializations' and location_input == 'All locations':
            if name_input:
                return redirect(url_for('search_all', name=name_input))
            else:
                return redirect(url_for('search_all'))
        elif specialization_input == 'All specializations' and location_input != 'All locations':
            if name_input:
                return redirect(url_for('search_by_location', location=location_input, name=name_input))
            else:
                return redirect(url_for('search_by_location', location=location_input))
        elif specialization_input != 'All specializations' and location_input == 'All locations':
            if name_input:
                return redirect(url_for('search_by_specialization', specialization=specialization_input, name=name_input))
            else:
                return redirect(url_for('search_by_specialization', specialization=specialization_input))
        else:
            if name_input:
                return redirect(url_for('search', specialization=specialization_input, location=location_input, name=name_input))
            else:
                return redirect(url_for('search', specialization=specialization_input, location=location_input))
    return render_template("home.html", search_form=form, doctors=doctors)

@app.route('/search', defaults={'name': None})
@app.route('/search/<name>')
def search_all(name):
    """
    Return all doctors
    """
    all_doctors = search_doctors(name)
    lenght = len(all_doctors)
    return render_template('search_results.html', doctors=all_doctors, lenght=lenght)


# don't forget remove the space between words in the uri 'South Siani'
@app.route('/search/location/<location>', defaults={'name': None})
@app.route('/search/location/<location>/<name>')
def search_by_location(location, name):
    """
    Filter doctors by location.
    
    Keyword arguments:
        location -- The location name to filter doctors by.
    
    Returns:
        Rendered HTML template displaying all doctors in the specified location.
    """
    if name:
        name = name.title()
        first_name, last_name = name.split() if ' ' in name else (name, None)
    location_obj = Location.query.filter_by(location_name=location).first()
    if not location_obj:
        return redirect(url_for('search_all', name=name))
    if name:
        if last_name:
            matched_doctors = Doctor.query.filter(
                Doctor.location_id == location_obj.id,
                Doctor.first_name.ilike(f'%{first_name}%'),
                Doctor.last_name.ilike(f'%{last_name}%')
            ).all()
        elif first_name:
            matched_doctors = Doctor.query.filter(
                Doctor.location_id == location_obj.id,
                Doctor.first_name.ilike(f'%{first_name}%')
            ).all()
    else:
        matched_doctors = Doctor.query.filter_by(location_id=location_obj.id).all()
    return render_template('search_results.html', doctors=matched_doctors, length=len(matched_doctors))

@app.route('/search/specialization/<specialization>', defaults={'name': None})
@app.route('/search/specialization/<specialization>/<name>')
def search_by_specialization(specialization, name):
    """
    Filter doctors by specialization

    Keyword arguments:
        specialization -- The specialization name to filter doctors by.

    Return:
        Rendered HTML template displaying all doctors with specified specialization.
    """
    if name:
        name = name.title()
        first_name, last_name = name.split() if ' ' in name else (name, None)
    specialization_obj = Specialization.query.filter_by(specialization_name=specialization).first()
    if name:
        if last_name:
            matched_doctors = Doctor.query.filter(
                Doctor.specialization_id == specialization_obj.id,
                Doctor.first_name.ilike(f'%{first_name}%'),
                Doctor.last_name.ilike(f'%{last_name}%')
            ).all()
        elif first_name:
            matched_doctors = Doctor.query.filter(
                Doctor.specialization_id == specialization_obj.id,
                Doctor.first_name.ilike(f'%{first_name}%')
            ).all()
    else:
        matched_doctors = Doctor.query.filter_by(specialization_id=specialization_obj.id).all()
    return render_template('search_results.html', doctors=matched_doctors)

@app.route('/search/<specialization>/<location>', defaults={'name': None})
@app.route('/search/<specialization>/<location>/<name>')
def search(specialization, location, name):
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
    if name:
        name = name.title()
        first_name, last_name = name.split() if ' ' in name else (name, None)
        if last_name:
            matched_doctors = Doctor.query.filter(
                Doctor.specialization_id == specialization_obj.id,
                Doctor.location_id == location_obj.id,
                Doctor.first_name.ilike(f'%{first_name}%'),
                Doctor.last_name.ilike(f'%{last_name}%')
            ).all()
        elif first_name:
            matched_doctors = Doctor.query.filter(
                Doctor.specialization_id == specialization_obj.id,
                Doctor.location_id == location_obj.id,
                Doctor.first_name.ilike(f'%{first_name}%')
            ).all()
    else:
        matched_doctors = Doctor.query.filter(
            Doctor.location_id == location_obj.id,
            Doctor.specialization_id == specialization_obj.id
        ).all()
    return render_template('search_results.html', doctors=matched_doctors)

from flask import render_template, jsonify, request, redirect, url_for
from datetime import datetime, timedelta

@app.route('/doctor/<doctor_id>', methods=['GET'])
def doctor_profile(doctor_id):
    """Display HTML file of doctor

    Keyword arguments:
        argument -- doctor_id
    Return:
        Returned HTML tmeplete displaying doctor page
    """
    form = Add_review()
    doctor = Doctor.query.filter_by(id=doctor_id).first()
    reviews = Review.query.filter_by(doctor_id=doctor.id).join(Patient).order_by(Review.updated_at.desc()).all()

    if doctor:
        # Calculate the next 7 days
        today = datetime.today().date()
        # next_7_days = [(today + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(7)]
        next_7_days = []
        for i in range(7):
            day = (today + timedelta(days=i))
            if day.strftime("%A") in doctor.schedule:
                next_7_days.append(day.strftime('%Y-%m-%d'))
        return render_template('doctor_profile.html', doctor=doctor, next_7_days=next_7_days, reviews=reviews, form=form)
    else:
        return "Doctor not found", 404

@app.route('/doctor/<doctor_id>/appointments/<date>', methods=['GET'])
def get_appointments(doctor_id, date):
    doctor = Doctor.query.filter_by(id=doctor_id).first()
    if doctor:
        valid_appointments = doctor.get_valid_appointments(date)
        return jsonify({'valid_appointments': valid_appointments.get(date, [])})
    else:
        return jsonify({'error': 'Doctor not found'}), 404

@app.route('/doctor/<doctor_id>/book', methods=['POST'])
@login_required
def book_appointment(doctor_id):
    doctor = Doctor.query.filter_by(id=doctor_id).first()
    if doctor:
        selected_date = request.form.get('selected_date')
        appointment_time = request.form.get('appointment_time')
        if selected_date and appointment_time:
            appointment_datetime = datetime.strptime(f"{selected_date} {appointment_time}", '%Y-%m-%d %H:%M')
            new_appointment = Appointment(patient_id=current_user.id ,doctor_id=doctor.id, appointment_date=appointment_datetime.date(), appointment_time=appointment_datetime.time())
            db.session.add(new_appointment)
            db.session.commit()
            return redirect(url_for('homePage'))
        else:
            return "Invalid data", 400
    else:
        return "Doctor not found", 404

@app.route('/profile/appointment/<appointment_id>/delete', methods=["GET", "DELETE"])
@login_required
def delete_appointment(appointment_id):
    """Delete appointment passed on id
    
    Keyword arguments:
        argument -- appointment_id
    Return:
        Returned HTML templete of all existing appointments in user profile
    """
    
    appointment = Appointment.query.filter_by(id=appointment_id).first()
    db.session.delete(appointment)
    db.session.commit()
    return redirect(url_for('profile'))

@app.route('/doctor/<doctor_id>/add_review', methods=['POST'])
@login_required
def add_review(doctor_id):
    form = Add_review()
    if form.validate_on_submit() and form.text.data:
        try:
            rating = int(form.rating.data)
            if rating < 1 or rating > 5:
                return jsonify({'success': False, 'error': 'Rating must be between 1 and 5.'}), 400

            review = Review(
                patient_id=current_user.id,
                doctor_id=doctor_id,
                review_text=form.text.data,
                rating=rating
            )
            db.session.add(review)
            db.session.commit()
            
            # Assuming you have a to_dict method to serialize the review object
            review_data = {
                'Patient': {
                    'first_name': current_user.first_name,
                    'last_name': current_user.last_name
                },
                'rating': review.rating,
                'review_text': review.review_text
            }

            return jsonify({'success': True, 'review': review_data}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'success': False, 'error': str(e)}), 500
    return jsonify({'success': False, 'error': 'Invalid form data'}), 400

@app.route("/doctors")
def doctorsPage():
    """Returned all doctors
    """
    return redirect(url_for('search_all'))

@app.route("/register", methods=['GET', 'POST'])
def register():
    """Registeration form
    """
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
    """Login form
    """
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

@app.route('/profile')
@login_required
def profile():
    """List all appointments

    Return:
        Returned HTML templete of all existing and unexpired appointments in user profile
    """
    
    user_appointments = Appointment.query.filter(
        Appointment.patient_id == current_user.id,
       (Appointment.appointment_date > datetime.now().date()) |
       (Appointment.appointment_date == datetime.now().date()) &
       (Appointment.appointment_time > datetime.now().time())).join(Doctor).all()

    image_filename = current_user.images.decode() if isinstance(current_user.image, bytes) else current_user.image
    image_file = url_for('static', filename=f'user_images/{image_filename}') if image_filename else None
    return render_template("profile.html", title='Profile', image_file=image_file, user_appointments=user_appointments)

@app.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    """Update user information
    """
    
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
    image_filename = current_user.image.decode() if isinstance(current_user.image, bytes) else current_user.image
    image_file = url_for('static', filename=f'user_images/{image_filename}') if image_filename else None
    return render_template("settings.html", title='settings', form=form, image_file=image_file)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('homePage'))

if __name__ == "__main__":
    app.run(debug=True)
