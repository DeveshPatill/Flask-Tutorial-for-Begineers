from flask import *
app=Flask(__name__)

app.secret_key="loginform"

@app.route('/')
def displayingform():
    return render_template('formloginforerrorflashmessaging8.html')

@app.route('/flashmessaging',methods=['GET'])
def output():
    error = None
    name = request.args.get('name')
    password=request.args.get('pass')
    if name =="devesh" and password =="123":
        flash("welcome succesfully loggedIn")
        return render_template('flasherrormessaging.html',var=name)
    else:
        error="invalid username or message"
        return render_template('formloginforerrorflashmessaging8.html',err=error)
app.run(debug=True)