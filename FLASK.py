from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')

def styling():
    return render_template("form2.html")
app.run(debug = True)