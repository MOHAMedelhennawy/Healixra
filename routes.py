from flask import Flask, render_template, flash, redirect, url_for
from models.registration import Registration
from models.login import Login


app = Flask(__name__)


app.config['SECRET_KEY'] = '4d297f88daf6623e4fe0df5f62d1e152c2076978af7ae82c4f77006340f256f1'



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
    form = Registration()
    if form.validate_on_submit():
        name = form.first_name.data + ' ' + form.last_name.data
        flash(f"Accoun created successfully for {name}", "success")
        return redirect(url_for('homePage'))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = Login()
    if form.validate_on_submit():
        if form.email.data == "elhennawy@ex.com" and form.password.data == "PASS!!!word123":
            flash('You have been logged in successfully!', 'success')
            return redirect(url_for('homePage'))
        else:
            flash('Please check your email or password', 'danger')
    return render_template("login.html", title="Login", form=form)



if __name__ == "__main__":
    app.run(debug=True)