from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def template():
    #return "<html><head><body><h1> hiiii this is template tutorials using flask </html></head></body><h1>"
    return render_template('index.html')
app.run(debug=True)
