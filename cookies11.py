from flask import *
app = Flask(__name__)

@app.route('/set')
def set_cookie():
    resp=make_response("<h1>hey welcome to the cookies tutorial</h1>")
    resp.set_cookie("flask","devesh")
    return resp

@app.route('/get')
def get_cookie():
    result=request.cookies.get("flask")
    return result

@app.route('/count')
def count_cookie():
    #get
    count=int(request.cookies.get("countcookies",0))
    count=count+1
    message="visited this page"+ str(count)

    #set
    responseee=make_response(message)
    responseee.set_cookie("countcookies",str(count))
    return responseee

if __name__== "__main__":
    app.run(host='0.0.0.0',port=5001,debug=True)