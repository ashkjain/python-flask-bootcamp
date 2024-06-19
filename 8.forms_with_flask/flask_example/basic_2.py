from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, DateTimeField, RadioField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = "mykey"

class InfoForm(FlaskForm):
    breed = StringField("What breed are you?", validators=[DataRequired()])
    neutered = BooleanField("Have you been neutered?")
    mood = RadioField('Please choose your mood: ', choices=[('mood_one','Happy'),('mood_two','Excited')])
    food = SelectField('Pick your favorite food:', choices=[('chi','Chicken'),('bf','Beef'),('fish','Fish')])
    feedback = TextAreaField()
    submit = SubmitField()

@app.route("/", methods= ['GET','POST'])
def index():
    return 