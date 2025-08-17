from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/fetch/')
def fetchingdatafunction():
    return render_template('fetchform6.html')

@app.route('/success/',methods=['POST'])
def answer():
    if request.method == 'POST':
        resultgot = request.form
        return render_template('resultfetchform.html',resultloop=resultgot)

app.run(host='0.0.0.0',port=8000,debug=True)