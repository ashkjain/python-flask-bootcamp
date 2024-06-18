from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('exindex.html')


@app.route("/report")
def report():
    userName = list(request.args.get('user'))
    req1, req2, req3 = False, False, False
    try:
        temp = int(userName[-1])
        if type(temp) == int:
            req3 = True
    except:
        req3 = False
    for i in userName:
        if ord(i) >= 65 and ord(i) <= 90:
            req1 =  True
            break
    for i in userName:
        if ord(i) >= 97 and ord(i) <= 122:
            req2 =  True
            break
    prompt = False
    if (req1 and req2 and req3) == True:
        prompt = True
    requirments = [req1, req2, req3]
    return render_template('report.html', user = userName, prompt = prompt, req = requirments)

if __name__ == "__main__":
    app.run(debug=True)