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
<a href="{{'index'}}">Home Page</a>
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

# 12. Flask Form Basics

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