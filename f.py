from flask import Flask , render_template , request
import mysql.connector
app = Flask(__name__)

@app.route('/')
def styling():
    return render_template("Landingpage.html")
@app.route('/Analysis')
def analysis():
    return render_template("DATA_ANALYSIS.html")
@app.route('/About us')
def about():
    return render_template("Aboutus.html")
@app.route('/Contact us')
def contact():
    return render_template("Contactus.html")
@app.route('/Get Started')
def getstarted():
    return render_template("form1.html")
app.run(debug=True)