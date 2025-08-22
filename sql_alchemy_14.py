from flask import Flask,render_template,session,request
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)

# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/myflaskdb'
app.config['SQLALCHEMY_MODUFICATIONS'] = True
# Creating an SQLAlchemy instance
db = SQLAlchemy(app)

class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True,autoincrement=True)
    username = db.Column(db.String(80), unique=True,nullable=False)
    email = db.Column(db.String(120), unique=True,nullable=False)

@app.route('/')
def databasess():
    number=11
    fname="deepbhanji"
    var_mail="bhanji@1gmail.com"
    entry= Contacts(sno=number,username=fname,email=var_mail)
    db.session.add(entry)
    db.session.commit()
    return "succesfully inserted data using sqlalchemy"

if __name__ == "__main__":
    app.run(debug=True)