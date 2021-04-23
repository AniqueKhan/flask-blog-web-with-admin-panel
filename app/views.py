from app import app
from flask import render_template,request,flash,redirect,url_for
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import current_user,login_user
from models import *
from app import *
@app.route("/")
def index():
    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


@app.route("/sign-up",methods=['GET','POST'])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = user_datastore.create_user(email=email,password=password)
        db.session.add(user)
        db.session.commit()
        flash("Account Created Successfully",category="success")
        return render_template("index.html")
    return render_template("sign-up.html")

