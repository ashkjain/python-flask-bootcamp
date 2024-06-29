import os
from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate

basedir = os.path.abspath(os.path.dirname(__file__))
# __file__ --> basic.py

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sql')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db)
#-----------------------

class Puppy(db.Model):
    __tablename__ = "puppies"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True) 
    name = db.Column(db.String(100), nullable = False)
    age = db.Column(db.Integer, nullable = False)
    breed = db.Column(db.Text)

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __repr__(self):
        return f"Puppy {self.name} is {self.age} year's old"


if __name__ == "__main__":
    app.run(debug=True)