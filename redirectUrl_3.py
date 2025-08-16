from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def welcome():
    return "welcome to redirect url section topic........."

@app.route('/student')                               # localhost/port/user/student ---> localhost/port/student
def student():
    return "My name is devesh and i am a devloper"

@app.route('/faculty')                               # localhost/port/user/faculty ---> localhost/port/faculty
def faculty():
    return "Department of Information technology MU"

@app.route('/user/<name>')
def user(name):
    if name == 'student':
        return redirect(url_for('student'))
    if name == 'faculty':
        return redirect(url_for('faculty'))

app.run(host='0.0.0.0',port=8000,debug=True)