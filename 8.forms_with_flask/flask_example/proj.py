from flask import Flask, render_template, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = "mykey"

class SimpleForm(FlaskForm):
    breed = StringField("What is your dog's breed?", validators=[DataRequired()])
    submit = SubmitField("Click Me!")
    pass

@app.route("/", methods = ['GET','POST'])
def index():
    form = SimpleForm()
    if form.validate_on_submit():
        session['breed'] = form.breed.data
        flash(f"You Choose breed: {form.breed.data}")
        return redirect(url_for('index'))
    return render_template("proj.html", form = form)

if __name__ == "__main__":
    app.run(debug=True)