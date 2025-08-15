from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "welcome to url building lecture "

@app.route('/<name>/')
def hello_1(name):
    return "name " + name

#routing date in url 
@app.route('/<int:date>')
def hello_2(date):
    return "date = %d" %date

#routing float number in url
@app.route('/<float:date>')
def hello_3(date):
    return "date = %f" %date

app.run(debug=True)