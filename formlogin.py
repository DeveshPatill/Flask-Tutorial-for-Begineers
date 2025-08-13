from flask import Flask,request
app = Flask(__name__)

@app.route('/formlogin',methods=['POST'])
def login():
    fn= request.form['firstname']
    ln = request.form['lastname']
    email = request.form['email']
    passw = request.form['password']
    if fn == "devesh" and ln == "patil" and email == "patildevesh677@gmail.com" and passw == "123":
        return "welcome " + fn
    else:
        return "not found invalid credentials"
     
app.run(host='0.0.0.0',port=8000,debug=True)

