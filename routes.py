from flask import Flask, render_template, flash, redirect
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
        flash(f"Accoun created successfully for {form.username.data}", "success")
        return redirect('homePage')
    return render_template("register.html", title="Register", form=form)


@app.route("/login")
def login():
    form = Login()
    return render_template("login.html", title="Login", form=form)



if __name__ == "__main__":
    app.run(debug=True)