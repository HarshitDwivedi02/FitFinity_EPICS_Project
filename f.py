from flask import Flask , render_template , request
import mysql.connector
app = Flask(__name__)

def calculate_bmi(weight, height):
    bmi = weight / (height**2)
    return round(bmi, 2)

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


@app.route('/Yogas')
def yoda():
    return render_template("Yogas.html")

"""def main_page():
    return render_template("excercises.html")"""


@app.route("/diet")
def diet():
    return render_template("diet.html")


@app.route("/exercise")
def exer():
    return render_template("excercises.html")


@app.route('/submit', methods=['POST','GET'])
def submit():
     if (request.method=='POST'):
        name = request.form.get('Username')
        age = request.form.get('Age')
        height = request.form.get('Height')
        weight = request.form.get('Weight')
        gender = request.form.get('Gender')
        bmi = calculate_bmi(float(weight), float(height))

     return render_template('form2.html', name=name,age=age,height=height,bmi=bmi,gender=gender,weight=weight)

@app.route('/get', methods=['POST','GET'])
def get():
     if (request.method=='POST'):
        stress_level = request.form.get('stress_level')
        activity_level = request.form.get('activity_level')
     return render_template('excercises.html', stress_level=stress_level,activity_level=activity_level)

        

if __name__ == '__main__':
    app.run(debug=True)