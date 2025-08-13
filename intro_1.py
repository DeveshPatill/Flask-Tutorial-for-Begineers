from flask import Flask

app = Flask(__name__)
@app.route('/')

def my_function():
    return "ganpatti bappa morya mla job lagudya..........."
 

@app.route('/devesh')
def hello():
    return "ive changed link name"
app.run(debug=True)