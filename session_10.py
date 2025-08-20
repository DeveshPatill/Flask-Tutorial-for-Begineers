from flask import Flask, render_template, request, session

app=Flask(__name__)
app.secret_key='authentication'

@app.route('/')
def say():
    return render_template('sessionloginform_10.html')

@app.route('/logoutpage')
def logoutt():
    session.pop('out',None)
    return render_template('sessionloginform_10.html')


@app.route('/loginpage',methods=['POST'])
def loginn():
    if request.method == 'POST':
        namekavariable = request.form['username']
        passkavariable = request.form['password']
        if (namekavariable == 'deveshpatil' and passkavariable == '1234'):
            session['out']= namekavariable
            return render_template('sessionresultform_10.html',name=namekavariable)
        else:
            errormsg="invalid username or password"
            return render_template('sessionloginform_10.html',errormessage=errormsg)

@app.route('/profilepage')
def profile():
    if 'out' in session:
        variableforsession=session['out']
        return render_template('sessionprofilepage_10.html',var=variableforsession)
    else:
        msg="login first"
        return render_template('sessionloginpage_10.html')
        
app.run(host='0.0.0.0',port=2000,debug=True)
