import json
from flask import Flask,render_template,session,request
from flask_mail import *
from random import *
app = Flask(__name__)


with open('configmail_12.json','r') as f:
    para=json.load(f)['parameter']


app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']=para['gmail-user']
app.config['MAIL_PASSWORD']=para['gmail-password']
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True

mail=Mail(app)
otp=randint(0000,9999) #any 4 number to generate otp which starts from 0 to 9

@app.route('/verify',methods=['POST'])
def verify():
    emailaayegafromweb=request.form['email']
    message=Message('OTP',sender="patildevesh677@gmail.com",recipients=[emailaayegafromweb])
    message.body= str(otp)
    mail.send(message)
    return render_template("verify15.html")

@app.route('/validate',methods=['POST'])
def validate():
    if request.method == 'POST':
        userotp=request.form['otp']
        if otp == int(userotp):
            return render_template("verify15.html",text="email verified succesfully")
        else:
            return render_template("email15.html",msg="not verified!,try again")

@app.route('/')
def indexx():
    return render_template("email15.html",msg="dd")

if __name__ == "__main__":
    app.run(debug=True)