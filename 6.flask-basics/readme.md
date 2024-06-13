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