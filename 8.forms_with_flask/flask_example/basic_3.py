from flask import Flask, render_template, redirect, url_for, flash, session
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import data_required

app = Flask(__name__)

app.config['SECRET_KEY'] = "mykey"

class SimpelForm(FlaskForm):
    submit = SubmitField("Click Me!")

@app.route("/", methods=['GET','POST'])
def index():
    form = SimpelForm()

    if form.validate_on_submit():
        flash('You just clicked the button!')
        return redirect(url_for('index'))
    return render_template('flash.html', form = form)

if __name__ == "__main__":
    app.run(debug=True)