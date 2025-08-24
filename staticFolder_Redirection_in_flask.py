from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def redirection():
    return render_template('static_folder.html')

@app.route('/pageredirecting/')
def fun():
    return render_template('pure.html')

@app.route('/page<username>/')
def func(username):
    return "welcome" + username

app.run(debug=True)