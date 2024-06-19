from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = "mykey"

class InfoForm(FlaskForm):
    firstname = StringField("Please Enter Your First Name: ")
    lastname = StringField("Please Enter Your Last Name: ")
    submit = SubmitField("Submit")

@app.route("/", methods = ['GET','POST'])
def index():
    fname = False
    lname = False
    myform = InfoForm()
    if myform.validate_on_submit():
        fname = myform.firstname.data
        lname = myform.lastname.data
        myform.firstname.data = ''
        myform.lastname.data = ''
    return render_template('index.html', myform = myform, fname = fname, lname = lname)

if __name__ == "__main__":
    app.run(debug=True)