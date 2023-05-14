from flask import Flask , render_template , request
import mysql.connector

app = Flask(__name__)

# global variables used
medical_complication = ' '
stress_level = ' '
activity_level = ' '

# create a connection to the database
mydb1 = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="yoga_diet")

# create a cursor object to execute SQL queries
cur = mydb1.cursor()


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


@app.route("/diet")
def diet():
    global medical_complication
    
    var = "SELECT Diet_1,Diet_2,Diet_3,Diet_4 FROM health_output WHERE Health_Problems  LIKE '"+medical_complication+"%'"
    # print(var)
    cur.execute(var)
    results = cur.fetchone()
    
    return render_template("diet.html",dietlst=results)


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

@app.route('/exercise', methods=['POST','GET'])
def exercise():
    global cur, medical_complication, activity_level, stress_level
    
    if (request.method=='POST'):
        stress_level = request.form.get('stress_level')
        activity_level = request.form.get('activity_level')
        medical_complication = request.form.get('medical_complication')

    # execute a SQL query to get the matching yoga asanas and dietary habits
    var = "SELECT Yoga_1,Yoga_2,Yoga_3,Yoga_4,Yoga_5 FROM health_output WHERE Health_Problems  LIKE '"+medical_complication+"%'"
    #print(var)
    cur.execute(var)
    results = cur.fetchone()
        
    return render_template('excercises.html', stress_level=stress_level,activity_level=activity_level,medical_complication=medical_complication,matching_yogas=results)


if __name__ == '__main__':
    app.run(debug=True)