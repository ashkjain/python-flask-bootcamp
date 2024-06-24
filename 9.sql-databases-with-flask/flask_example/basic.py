import os
from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
# __file__ --> basic.py

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sql')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#-----------------------

class Puppy(db.Model):
    __tablename__ = "puppies"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True) 
    name = db.Column(db.String(100), nullable = False)
    age = db.Column(db.Integer, nullable = False)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Puppy {self.name} is {self.age} year's old"


if __name__ == "__main__":
    app.run(debug=True)