from flask import Flask, render_template,request,redirect,session,get_flashed_messages
from flask_sqlalchemy import SQLAlchemy
from flask import  flash , jsonify
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user,logout_user,login_manager,LoginManager
from flask_login import login_required,current_user
from flask_mail import Mail
import json


local_server =True
app = Flask(__name__)
app.secret_key='nandi'

# app.config ['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:localhost : 3306/eweb'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:3306/eweb'

# app.static_folder = 'static'
db=SQLAlchemy(app)

class Auth(db.Model):
    id =db.Column(db.Integer, primary_key= True)
    Username = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))

# Initialize the database
# db.create_all()

@app.route("/")
def Home():
    return "home"

@app.route("/login")
def login():
    return render_template('login.html')


@app.route('/signup',methods=['POST','GET'])
def signup():
    if request.method == "POST":
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        repassword = request.form.get('repassword')

        user = Auth.query.filter_by(email = email).first()
        if user:
            flash("Email Already Exist","warning")
            return render_template('/signup.html')
        encpassword=generate_password_hash(password)

        # new_user=db.engine.execute(f"INSERT INTO `auth` (`username`,`email`,`password`) VALUES ('{username}','{email}','{encpassword}')")
        # flash("Signup Succes Please Login","success")
        # return render_template('login.html')

        if password ==repassword:
            new_user=db.engine.execute(f"INSERT INTO `auth` (`username`,`email`,`password`) VALUES ('{username}','{email}','{encpassword}')")
            flash("Signup Succes Please Login","success")
            return render_template('login.html')
        else:
            return "password doesnt match"
    return render_template('signup.html')

@app.route("/forgot")
def forgot():
    # return render_template('forgotpass.html')
    return "forgot"

if __name__ == "__main__":
    app.run(debug=True)
