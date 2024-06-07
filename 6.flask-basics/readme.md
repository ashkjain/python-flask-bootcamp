1. We need to create a virual enviornment for our web applications using default 'venv', it is a package manager and it comes with "python". Why we need to create Virtual Enviornment? The reason we should create a virtual enviornment because as we have seen python comes with latest updates and some of the functions and methods are not available to use anymore. To avoid that error in our web application we can create an environmnent with all the dependencies and it will not cause runtime error in future if the base version of python we are using is changed, because we will still be using the version and dependencies that we use to run our program. To create a Virtual Enviornment we use command `python -m venv myenv`. To activate the enviornment use inside the main directory `myenv\Scripts\activate` and install all the packages inside. To deactivate the enviornment use `deactivate`.

2. ## Flask Basics
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