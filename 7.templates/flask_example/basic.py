from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('main.html')

@app.route("/variables")
def index_1():
    name = "Some Name"
    letters = list(name)
    pup_dict = {'pup_name':'Sammy'}
    return render_template('basic.html', name = name, letters = letters, pup_dict = pup_dict)

@app.route("/control_flow")
def index_2():
    mylist = [i for i in range(1,6)]
    puppies = ['Fluffy','Rufus','Spike']
    user_log = False
    return render_template('control.html', mylist = mylist, puppies = puppies, user_log = user_log)

if __name__ == "__main__":
    app.run(debug=True)