from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/')
def upload():
    return render_template('fileuploading_7.html')

@app.route('/page',methods=['POST'])
def mainfunction():
    if request.method == 'POST':
        f = request.files['file1']
        f.save('static/image/' + f.filename)
        return "your item(image) succesfully loaded"
    
app.run(host='0.0.0.0',port=7000,debug=True)