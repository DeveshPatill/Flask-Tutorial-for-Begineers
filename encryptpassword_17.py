"""
from flask import Flask, request, redirect, url_for, session,flash
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from passlib.hash import sha256_crypt
from werkzeug.utils import redirect


app = Flask(__name__)
app.secret_key = "your_secret_key"

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database Configuration (MySQL)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/flask_encryption'
app.config['SQLALCHEMY_MODIFICATIONS'] = True

db = SQLAlchemy(app)

# Define Contact Model
class Contact(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(256))



@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method=='POST':
        email=request.form['email']
        password=request.form['password']
        try:
            user=Contact.query.filter_by(email=email).first()
            pas=user.password
            if(sha256_crypt.verify(password,pas)):
                session['email']=email
                return render_template('new17.html')
            else:
                flash("invalid username or password")
                return redirect(url_for('login'))
        except:
            flash("try , again")
            return redirect(url_for('login'))


    return render_template("login_17.html")

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method=='POST':
        email=request.form['email']
        nam=request.form['name']
        password=request.form['password']
        encpassword=sha256_crypt.encrypt(password)
        entry=Contact(name=nam,email=email,password=encpassword)
        try:
            db.session.add(entry)
            db.session.commit()
            flash("regestration done")
            return redirect(url_for('login'))
        except:
            flash("try again")
            return redirect(url_for('register'))

    return render_template("register_17.html")



@app.route('/logout')
def logout():
    session.pop('email',None)
    return render_template('login_17.html')


if __name__ == '__main__':
    #db.create_all()  # Create tables if not exist
    app.run(debug=True)

"""

from flask import Flask, request, redirect, url_for, session, flash, render_template
from flask_sqlalchemy import SQLAlchemy
from passlib.hash import sha256_crypt
import pymysql

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Database Configuration (MySQL)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/flask_encryption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define Contact Model
class Contact(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = Contact.query.filter_by(email=email).first()

        if user and sha256_crypt.verify(password, user.password):
            session['email'] = email
            return render_template('new17.html')
        else:
            flash("Invalid username or password")
            return redirect(url_for('login'))

    return render_template("login_17.html")

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        nam = request.form['name']
        password = request.form['password']
        encpassword = sha256_crypt.encrypt(password)

        entry = Contact(name=nam, email=email, password=encpassword)
        
        try:
            db.session.add(entry)
            db.session.commit()
            flash("Registration successful")
            return redirect(url_for('login'))
        except:
            flash("Email already registered or error occurred. Try again.")
            return redirect(url_for('register'))

    return render_template("register_17.html")

@app.route('/logout')
def logout():
    session.pop('email', None)
    return render_template('login_17.html')

if __name__ == '__main__':
    # Uncomment this line to create the database tables if they don't exist
    # db.create_all()
    app.run(debug=True)
