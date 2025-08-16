from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def helloo():
    dictionary = {'python': 100,'java': 80,'c':80,'sql':100}
    return render_template('flaskdelimiters.html',results=dictionary,name="devesh",result=200)


@app.route('/<username>/')
def myfunction(username):
    return render_template('flaskdelimiters.html',name=username)

@app.route('/<int:teachingscore>/')
def myfunction_1(teachingscore):
    return render_template('flaskdelimiters.html',result=teachingscore)

app.run(debug=True)
    