from flask import Flask, render_template,request
from flask_wtf import FlaskForm  
from wtforms import StringField, SubmitField ,validators,stringField
from flask_wtf import Form
from wtforms import ValidationError

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ydevesh'  

class ContactForm(FlaskForm):  
    name = stringField("Your Name",[validators.DataRequired("plz enter ur name")])  
    submit = SubmitField("Submit")

@app.route('/')
def my_function():
    form = ContactForm()
    return render_template("wtform_16.html", form=form)

@app.route('/loginkr',methods=['POST'])
def info():
    form=ContactForm()
    if request.method=='POST':
        if form.validate==False:
            name=form.name.data
            return name
        
    return render_template("wtform_16.html",form=form)

if __name__ == '__main__':
    app.run(debug=True)
