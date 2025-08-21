import json
from flask import Flask
from flask_mail import *

app=Flask(__name__)

with open('config_bulkmail_12.json','r') as b:
    brackets=json.load(b)['parameters']
mail=Mail(app)


app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']=brackets['gmail-id']
app.config['MAIL_PASSWORD']=brackets['gmail-pass']
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True


@app.route('/')
def bulkmail():
    message=Message('important notice',sender="patildevesh677@gmail.com",recipients=['deveshpatil450@gmail.com'])
    message.body="everyone plz apply on the portal -satvikka maam"
    mail.send(message)
    return "gmail succesfully sent"

if __name__ == "__main__":
    app.run(debug=True)