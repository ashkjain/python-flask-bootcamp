from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Welcome! Go to /puppy_latin/name to see your name in puppy latin!</h1>"

@app.route("/pppy_latin/<name>")
def puppy_latin(name):
    new = name.title()
    name_l = list(name)
    if name_l[-1] == 'y':
        name_l[-1] = 'iful'
    else:
        name_l[-1] = 'y'

    latin = ""
    for i in name_l:
        latin+=i
    return "<h1>Hi {}! Your puppylatin name is {}</h1>".format(new, latin)

if __name__ == "__main__":
    app.run(debug=True)