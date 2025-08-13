from flask import Flask,request

app=Flask(__name__)

@app.route('/formlogin_1',methods=['GET'])
def login():
    fn = request.args.get("fname")
    ln = request.args.get("lname")
    email = request.args.get('email')
    passw = request.args.get('pass')
    if fn == "devesh" and ln == "patil" and email == "patildevesh677@gmail.com" and passw == "123":
        return "welcome to this "
    else:
        return "invalid credentials try again"

app.run(debug=True)