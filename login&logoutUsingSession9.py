from flask import Flask,render_template,request,session
app=Flask(__name__)

app.secret_key ="devesh"

@app.route('/')
def hey():
    return render_template('loginandlogoutUsingSession9.html')

@app.route('/logout')
def logout():
    session.pop('out',None)
    return render_template('loginandlogoutUsingSession9.html')


@app.route('/login',methods=['POST'])
def login():
    if request.method == 'POST':
        var_name=request.form["username"]
        var_pass=request.form["password"]
        if (var_name == "devesh" and var_pass == "123"):
            session['out']= var_name
            return render_template("succesfullyloggedin_out9.html",name=var_name)
        else:
            message="Invalid credentials/username or password"
            return render_template("loginandlogoutUsingSession9.html",msg=message)
        
        
app.run(host='0.0.0.0',port=3000,debug=True)
