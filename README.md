## 1. Virtual Environment
We need to create a virual enviornment for our web applications using default 'venv', it is a package manager and it comes with "python". Why we need to create Virtual Enviornment? The reason we should create a virtual enviornment because as we have seen python comes with latest updates and some of the functions and methods are not available to use anymore. To avoid that error in our web application we can create an environmnent with all the dependencies and it will not cause runtime error in future if the base version of python we are using is changed, because we will still be using the version and dependencies that we use to run our program. To create a Virtual Enviornment we use command `python -m venv myenv`. To activate the enviornment use inside the main directory `myenv\Scripts\activate` and install all the packages inside. To deactivate the enviornment use `deactivate`.

## 2.  Flask Basics
To create a very simple webpage first we are going to create a file and import flask init. Let's go through code and reviwe it:-
```
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello Puppy!</h1>"

if __name__ == "__main__":
    app.run()
```
Lets break it down and understand what is going on.
* First we are importing Flask from flask library. Captilization is important.
* In the second line we are creating an instance of an object which is Flask.
* Then we are creating a route which we will be calling templates, we are routing in this case to the main page. And then we are declaring a function which is returning an HTML.
* At the very end we are running the script and upon run we are running the function.

## 3. Basic Routes
Currently our domain is local and represented as ** http://127.0.0.1:5000/ ** or ** localhost:5000 **. We use decorators to add on this:-
```
# http://127.0.0.1:5000/some_page

@app.route("/some_page")
```
And when this is deployed this local link will be changed to the domain for ex: www.site.com
Here is the example of this routing process!
```
@app.route('/information') #127.0.0.1:5000/information
def info():
    return "<h1> Puppies are cute</h1>"
```
In this code above decorator is providing the route /information

## 4. Flask Dynamic Routing
We are going to demonstrate URL extension to be dynamic based on the situation (This is how Real World application works!).
For example we may want to create page per user, extension could be in form of: ** www.site.com/user/unique_user_name **
To acheive this effect we can use dynamic routes. Dynamic routes have 2 key aspects, a variable in the route '<variable>' instead of the hard code value like above examples. Second parameter passed into the function.
For ex:-
```
@app.route('some_page/<name>')
def other-page(name):
    #Later we will see how yo use this with templates!
    return 'User:{}'.format(name)
```
.format(name) is filling up the space that is in curly braces. Curly braces is a placeholder.

```
@app.route('/puppy/<name>')
def puppy(name):
    return "<h1>This is a page for {}</h1>".format(name.upper())
```

## 5. Debug Mode
We can set debug=True in our application to catch errors and it will stop immediatly the moment we make a mistake and or bug is introduced. This debug mode also gives us access to a console in the browser.
If we try to run some code that is errornous but we are not using debug mode it will let it run, and at some point it will return Internal Server Error. For ex:
```
@app.route('some_page/<name>')
def other-page(name):
    #Later we will see how yo use this with templates!
    return 'User:{}'.format(name[100])
```
This is the code and out value that is passed in the function is 'hello' but since hello does not have 100 charachters in it, it will cause an error and Flask will return Internal Server Error upon requesting this.
To simply put the application in debug mode we can do this:-
```
if __name__ == "__main__":
    app.run(debug=True)
```
We just have to pass positional argument with it being True for debug mode. And now if some error occurs it will either shut down the program but if it is in different route if will show what type of error is it. For the last example it will show something like `IndexError`.
To access the console you have to go to any error and you will see a terminal windows sign click on it, and it will ask you for a pin. The pin will be in your terminal where server is running: *`Debugger PIN: xxx-xxx-xxx` and then you can see based on which console you open you will see a console something like this:-
```
[ console ready ]
>>> 
```
You can open console after a particular variable or the error you wanna debug. If you open console and the variable or function is not declared that you want to see result for it will give you some errors, because what you are trying to find does not exist yet.


## 6. Template Basics
For now we were just rendering string in return from the function on routes. But realistically we want to create HTML templates and we want function to render those.
Flask will automatically look for HTML templates in the directory that will be called `templates`.
So to render template in our application we have to use one of the function from flask library `render_template`, this will help us render templates .html files.

Now where we imported Flask from flask library, we are also going to import render_template. The code will look somthing like this:-
```
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('basic.html')
```
In this code while returning we are using render template function and in parantheses we are passing the name of the html file that should reside in the templates folder. This function will look files declared inside the templates folder so make sure you have created a directory called templates and in that directory html files should exist.
We can also pass in some static files for example in that .html file in the template folder we can add one img tag and give it a souce to a local image. Anything that is staic does not reside in the template folder, create a folder called `static` to store static files like templates in the main directory of our application. The will be something like this:-
```
<img src="../static/puppy.jpg" alt="">
```
We went up one directory since we reside in templates when rendering, from there we will enter static and then the name of the img or static files.

## 7. Template Variables
We are rendering HTML file using render_temoplate function, but we can also use variables inside those templates which will be done by template engine for flask called Jinja. We can directly pass variables inside of our html file. Syntax to pass a variable inside the html is `{{ some_variable }}`. We set parameters in our render_template function to pass those variables inside the html and then we pass those variable inside our templates in between these: `{{ }}`.
What we can do we can create a variable inside the function and then pass it to render_template like this:-
```
@app.route("/")
def index():
    some_variable = "Some Value"
    return render_template('basic.html', myvar = some_variable)
```
When passing the variable we created an alias for the template to refer to the variable in the function. In this case we are using `myvar` for our template which will refer to `some_variable` which exist in our function called `index`.
To read the variable inside the template what we can do is this:-
```
<h1>Hello! {{ myvar }}</h1> 
<!-- This will return the value of myvar which in python file is set to 'Some Value' -->
```
Another easy way while passing parameter make both value the same for example instead of setting it to myvar just use `some_variable = some_variable` to make it less confusing.
Not only we can pass strings in the template we can pass all sorts of data inside the template. We can pass lists, tuples, dictionaries and other forms of data, and we can use some data functions inside the templates too. For example:-
* Python
```
@app.route("/")
def index():
    myList = [1,2,3,4]
    myTuple = (1,2,3,4)
    myDict = {'One':'Number One'}
    render_template('basic.html', myList = myList, myTuple = myTuple, myDict = myDict)
```
* HTML
```
<h2>This is List {myList[0]}</h2>
<h2>This is Tuple {myTuple[:]}</h2>
<h2>This is Dcitionary {myDict['One']}</h2>
```
## 8. Template Control Flow
Now we know that we can pass variables in our templates, but it doesn't end there, we also have access to control flow syntax in our templates, such as: For Loop, if-else-elif ladder and more Jinja based control flow structures. To use these syntax simpliy we have to use something like this: `{% control_flow %}`. Take a look at this example with list to understand more:-
* HTML
```
<ul>
{% for item in mylist %}
<li> {{ item }} </li>
{% endfor %}
</ul>

{% if user_logged_in %}
<p> You are logged in!</p>
{% else %}
<p>Please log in</p>
{% endif %}
```
Make sure end your control flow data whenever it is being use, such as for loop like for use endfor, or for if use endif.

## 9. Template Inheritance
Template inheritance is used to irradicate the need to add similar items in every template which is same in our application. For example: Header, Footer, Naviagation bars, most of the time are similar and show the same information, but in templates we have to create them again, to remove that unnessary work we can inherit those templates in our other templates. In order to do that we use these: `{% extend "base.html" %}` and `{% block %}`. So to do this theoretical method we create a template first like this:-
* base.html
```
Here is all the information that will be same in all the page, such as navigation bar, header
{% block content %}
{% endblock %}
Here is all the information that will be same in all the page, such as navigation bar, footer
```
* home.html
```
{% extends "base.html" %}
All information from base.html

{% block content %}
Here will be the new information based on the page
{% endblock %}

All information from base.html
```
What we did here in base.html we created all the information that will be same throughout all the pages, after block we can give that block whatever name we want, like `{% block header %}` but usually content is easy way to remeber the name of the block. And whatever is in the block will be changed based on the page we are inheriting it to, in simple language the block is where dymanic content is shown. Then in home.html we extended that template by using `{% extends "base.html" %}` and we create more block where we will write the content that will be dynamic and serves the purpose of the page. In result the header and footer content will be on our home.html page without typing it again, and with dynamic content that will be coming from variables.
There is also one function or feature from Jinja, that we can use filters on our variables, to filter our variable we have to use pipe operator and tell what filter to use. For example I want to capitalize the Variable that is coming in template which could be lower or upper but I need it to be capitalize what we can do is: `{{ name | capitalize }}` this will make the first letter uppercase and rest lowercase, we do not have to do all the logic in our python code, because it can get messy.

## 10. url_for help function
There is a function called url_for that helps us to connect our templtes pages or files within our templates. To use it in the links where we define HREF we have to pass the name of the view, and when I say view I mean the name of the function that is rendering that template. Example:
* Python
```
@app.route("/")
def index():
    return render_template('index.html')
```
* HTML
```
<a href="{{url_for('index')}}">Home Page</a>
```
We cannot only add templates we can also add static files to it. For example we can pass in two parameters, first parameter folder name, second parameter filename = nameofthefile.extensions. Here is the example:-
* HTML
```
<a href="{{url_for('static', filename = iamge.jpg)}}"></a>
```

## 11. Template Forms
We learned how to retreive infomration using variables, but now we are gonna use forms to get information from user. No we are not going to connect to database yet, but it is a beginning. Lets introduce new function called `request`, this function will help to return the information from the external form. To use this function what we do is when the form is routing to a different page, or sending the request to different page, on that page function we have to catch those values. This is how we do it:-
* HTML Form
```
<form action="{{url_for('thankyou')}}">
    <label for="first">First Name</label>
    <input type="text" name="first">
    <label for="last">Last Name</label>
    <input type="text" name="last">
    <input type="submit" value="Submit form">
</form>
```
* HTML Requested
```
<h1> Thank you for submitting {{firstName}} {{lastName}} </h1>
```
* Python
```
app.route("/thankyou")
def thankyou():
    firstName = request.args.get('first')
    lastName = request.args.get('last')
    return render_template('thankyou.html', firstName = firstName, lastName = lastName)
```
This way you are getting the values passed from the form and being catched in another page, and then we can use the data as we want, based on the application. `request` function have to functions itself, first .args and then .get, it means return arguments and then we pass the name of the argument in this case we named our input boxes first and last, so we used those.

### **** Bonus Section ****
Lets create our own custom 404 error page. In order to do that first what we have to do is, we have to create our own template so we can pass that when 404 occurs. Since we are creating a route for 404 it is not going to be a typical route like normal template, in this we have to modify our decorator: `@app.errorhandler(404)`, this is the function of the application, in this we have to pass the type of the error since we are creating 404 error page we are passing the error code: 404. Then declare the function, and as a convention pass a variable `e` it could be anything it is just the convetion to use 'e' for errors. And when rendering template after using then add comma in return and add the number of the error. Here is the example:-
```
@app.errorhandler(404)
def pageNotFound(e):
    return render_template('404.html'), 404
```

## 12. Flask Form Basics
Now we are going to make our life easy when we are creating forms using flask. We can use `flask_wtf`, and `wtforms` packages to create forms quickly, with just our python scripts. First we have to configure secret key for security. Second we create WTForm class and create fields for each part of the form. Then we set up our view function, in which we add methods `methods = ['GET','POST']`, create an instance of form class, and then handle form submission. Make sure you also install `flask_wtf` using this command: `pip install flask_wtf` if upon importing shows error make sure you install it in the global environment as well. Now in application we are required to import few more things. First: `from flask_wtf import FlaskForm` this will help us built forms, and Second `from wtforms import StringField, SubmitField` this will helps us building the types inside the form like submit button, and string text input. Now we are going to set a secret key, so our flask app instance have some configuration that we can set and add. We are gonna set secret key like this: `app.config["SECRET_KEY"] = "secretkey"` and this config is a dictionary and there are various configuration we can set.
Now we are going to create a class which is going to be our form. We are going to declare a class and inherit `FlaskForm` and then declare fields with `wtforms`. Here is the example:-
```
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = "mysecretkey"

class InfoForm(FlaskForm):
    breed = StringField("What Breed Are You?")
    submit = SubmitField("Submit")

@app.route("/", methods = ['GET','POST'])
def index():
    breed = False
    form = InfoForm()
    if form.validate_on_submit():
        breed = form.breed.data
        form.breed.data = ''
    return render_template('index.html', form = form, breed = breed)
```
In the `breed` attribute we will get the input from the user and the content in the function is the label for that field. Same for submit, but it will just be going to a submission button. Then we create our route and put the methods that we will be using which is GET and POST method. Then we created a view in which we created a variable `breed` which we make a boolean False, Then we created an Instance of our class as `form = InfoForm()`. Now we are using if statement and checking if upon submission the form is validated or not. If it is validated the local variable `breed` will receive the value from the form `breed = form.breed.data` it means from the form instance grab the attribute breed and then extract its data into the variable. Then we reset the value of the breed attribute not variable `form.breed.data = ''` and then we rendered the template and pass the instance for the InfoForm which is `form` and the local variable `breed`. Now we are going to work on HTML:-
```
<p>
    {% if breed %}
    The Breed You Entered is {{breed}}
    Update it in the form below:
    {% else %}
    Please enter your breed:
    {% endif %}
</p>
<form method="POST">
    {{ form.hidden_tag() }}
    {{ form.breed.label}} {{ form.breed() }}
    {{ form.submit() }}
</form>
```
In this HTML what is happeinig is, we are checking if the breed variable that we passed is True or Not, if not it is going to ask user to Enter the value, if True it will show the breed and the form under will ask user to update the value. Then we are creating a form and in this form our Method is 'POST' because we are creating the data not pulling or getting it out. Then in the form we added the function with our object `form.hidden_tag()` which is a Cross-Site Request Forgery, which is a type of security vulnerability, to prevent that we use this function. Then we are calling the attribute breed which also contains a label which we passed in the parantheses during declaration, and next to it we pass the input field which is a function. Then on next line we passed the function which creates a submit button.

## 13. Forms Fields Part One
There are various fields in a form, and you can import all of them from `wtforms` like we imported `SubmitField` and `StringField`. We are gonna use for this `session`, `redirect`, and `url_for` and these all are from main `flask` library. We have learned about `url_for` but this is different and on the flask script side. And from `wtforms` we will be importing other fields too like: `BooleanField, DateTimeField, RadioField, SelectField, TextAreaField`. We are also going to be importing validators for our form, so user will know what is required and what is valid while filling the form, we will import it like this: `from wtforms.validators import DataRequired` we are only importing this for now, and what this does is, it tells user that this is a required filed and needs to be filed. To use these validators in our form, what we have to do is, when we are passing the label for the field we can put a comma after the label and pass another parameter and we can simply say `validator = [type_of_validator()]` by default it is always none unless we change it to something like `DataRequired`. Now we are going to see how those other fields work. Booleanfield is a yes or no question  and accepts a label as a parameter. RadioField as it sounds creates a radio button and after label we can pass another parameter for various radio buttons, and to pass those choices the parameter that is accepted is called `choices = [('choice_1','First Choice'),('choice_2','Second Choice)]`, so we have to pass the choices which is a list, and the choices that user will see are going to be in a tuple pair, it means first values is going to be the identifier and the second value inside the tuple is going to be the prompt that user will choose, and we can pass as many tuple pair based on the choices that are offered, and only one can be chosen. Now lets see how SelectField works, don't worry it works as the same way as Radio works, the difference is that multiple values can be returned. And TextArea field will give user a space to write which is usually used to provide feedbacks on website by user.
So Now we are done with the fields, we will use session, what session does is, it holds the information by the user and holds it in the server, unlike cookies it is reserved per session to keep track of login and logout. So when we go to different page it remembers the values or holds the value and keep the information to be used in different page like logging into a webiste and using the functionality unless logged out, or the session is terminated. So how it stores the session values is, it is like a dictionary, and we set the key and values. Something Like this:-
```
if form.validate_on_submit():
    session['fname'] = form.firstname.data
    session['lname'] = form.lastname.data
    session['boolean'] = form.yesno.data
    session['radiovalue'] = form.radio.data
    session['selectfield'] = form.selectfield.data
    session['feedback'] = form.feedbacktextarea.data
```
This is an example how we can store the data in session which is treated as a dictionary and the values are stored and move around the pages until the session is terminated. These values or information are not permanent, this is not going to database it is used to save values be so when we move to different page the values we begin with remains the same and session be in running, until terminated. Now let's talk about `redirect`, and `url_for` function, so what these functions are going to do is, `url_for` will create the link to the url that it will be redirected to, as a parameter we pass the name of the function or the view we want it to go, and we pass the returned url into `redirect` as a parameter to send it to that view with all the information. For example after checking the form is validated as above shown we can return it from that if function like this: `return redirect(url_for('function_name_or_view'))`. Lets see how it can be used with an explanation:-
```
app.route("/", methods= ['GET','POST'])
def index():
    form = InfoForm()
    if form.validate_on_submit():
        session['fname'] = form.firstname.data
        session['lname'] = form.lastname.data
        session['boolean'] = form.yesno.data
        session['radiovalue'] = form.radio.data
        session['selectfield'] = form.selectfield.data
        session['feedback'] = form.feedbacktextarea.data
        return redirect(url_for('thankyou'))

    return render_template('main.html', form = form)

@app.route("/thankyou")
def thankyou():
    return render_template('thank.html')
```
In this example what we did, we creating a form, if the session has not been created user will see the `main.html` in the return value, but if the submission has been made and the session is started the return from the if which is validation will return and in result it will redirect it to the another view called `thankyou`.
Here is the class that will help you to know how the form field are working:-
```
class InfoForm(FlaskForm):
    firstname = StringField("What is your first name?", validators = [DataRequired()])
    lastname = StringField("What is your last name?", validators = [DataRequired()])
    yesno = BooleanField("Are you a human?")
    radio = RadioField('Please choose your mood: ', choices=[('mood_one','Happy'),('mood_two','Excited')])
    selecfield = SelectField('Pick your favorite food:', choices=[('chi','Chicken'),('bf','Beef'),('fish','Fish')])
    feedbacktextarea = TextAreaField()
    submit = SubmitField()
```

## 14. Forms Fields Part Two
Now we are going to add templates for the backend that we wrote, we are now going to use those classes and those form fields in out .HTML files to see the app functioning. So, for this part wer are using template for user to fill in the details, and if the details are filled or session is active, we will be redirected to `thankyou` view, otherwise it will return a form for a user to fill out. We are going to pass the simple instance attributes in the form, and when we get to that `thankyou` view, it will return the session content, something like this the code will be written: `{{session['breed']}}` it will only return something if the session is running. And when we are representing the RadioField or SelectField values, the keys will be shown, not the values that user saw while filling the form. So make sure to make those values same to store later and it also makes sense to user and programmer. What it means is, the tuple that is passed, first value is actual data and the second value is just the representation for the user.
Here is the HTML that is being used:-
* main.HTML
```
<h1>Welcome to the Puppy Survey!</h1>
<form method="post">
    {{form.hidden_tag()}}
    {{form.breed.label}} {{form.breed()}} <br>
    {{form.neutered.label}} {{form.neutered()}} <br>
    {{form.mood.label}} {{form.mood()}} <br>
    {{form.food_choice.label}} {{form.food_choice()}} <br>
    Any Other Feedback?
    {{form.feedback()}} <br>
    {{form.submit()}}
</form>
```
* thankyou.html
```
<h1>Thank you. Here is the info you gave us:</h1>
<ul>
    <li>Breed: {{session['breed']}}</li>
    <li>Neutered: {{session['neutered']}}</li>
    <li>Mood: {{session['mood']}}</li>
    <li>Food: {{session['food']}}</li>
    <li>Feedback: {{session['feedback']}}</li>
</ul>
```
## 15. Flash Alerts
We sometime need to send user a flash message that do not need to be saved, and can be closed by the user. Flask has some built in features to do that so we do not have to put those alerts permanetly on our templates. To do all that we have a function called `flask` that we can use in our application to perform that task. So how we can use flask is we just import it from `flask` library, and then we can call it in our view like this: `flash('Here Goes The Message)`, and to render it on the template there is a function that needs to be used, which is called `get_flashed_messages()` this will return an iterable object and we can iterate multiple flash alerts. We can use for loop to iterate this since it returns an iterable object. Here is the example:-
* python
```
@app.route("/", methods=['GET','POST'])
def index():
    form = SimpelForm()

    if form.validate_on_submit():
        flash('You just clicked the button!')
        return redirect(url_for('index'))
    return render_template('flash.html', form = form)
```
What is happening in this file is, it is returning itself upon clicking, but it shows the functionality how `flash` works.
* html
```
{% for mess in get_flashed_messages() %}
    <div class="alert alert-warning alert-dismissible fade show" role="alert">
        <strong>{{mess}}</strong>
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    </div>
    {% endfor %}
    <form method="POST">
        {{form.hidden_tag()}}
        {{form.submit()}}
    </form>
```
There is some copied code from bootstrap to make it look like javascript alerts without directly using JavaScript.

## 16. Forms and Flash Code Along Project
The main changes we did, is added one StringField and used session to pass the value in the Alert or Flash.

## 17. Python and Databases
We have used our application to receive data from the user, but we never stored it permanently so we can use it again, even after closing our application. We will be using Database to store our information, in order to store information in a database we are going to use SQL Queries to CREATE, READ, UPDATE, and DELETE operations. To make a connection from python, flask and sql we will be using a library or an ORM (object Relational Mapper) called `SQLAlchemy`. We are going to install this on our system using this command `pip install Flask-SQLAlchemy` make sure do install `Flask-SQLAlchemy` not just `SQLAlchemy`, they both are different, but serves the same purpose, but Flask-SQLAlchemy is tailored specifically for Flask applications, and require less manual configurations.

## 18. Flask and Databases Part One
When we are working with Database we are going to these following operations:-
- Setting up a SQLite Database in Flask App
- Create a model in flask
- Perform basic CRUD operations
To create a SQLite database we have to follow few things:-
- First we need to create a Flask application
- Then configure Flask App for Flask-SQLAlchemy
- Then pass our application into the SQLAlchemy class call
After all that we need to create a model in SQL which in simple words is creating a Table. We do not have to create a table manually in SQL. Instead we create a model class in Python that creates a table for us. \
To create a model is as simple as the way we created forms:-
- Create a Model class
- Inherit from `db.Model`
- Provide the name of the table
- Add table columns as attributes
- Add methods for `__init__` and `__repr__`.
## Application Directory Structure and Code after templates
> Directory Structure:-
- myenv (Virtual Environment)
- flask_example (Application Directory)
    - basic.py
    - templates
        - basic.html
    - static
        - puppy.jpg

> Code inside files:-
- flask_example/basic.py
```
```
- flask_example/templates/basic.html
```
```