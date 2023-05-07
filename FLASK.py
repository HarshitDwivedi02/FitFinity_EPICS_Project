from flask import Flask , render_template , request
import mysql.connector
import pickle

# Database connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="users_info"
)

# Create cursor
cursor = mydb.cursor()

# function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / ((height/100)**2)
    return round(bmi, 2)

app = Flask(__name__)

@app.route('/')

def styling():
    return render_template("main.html")

# route to handle the form 1 submission
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    age = request.form['age']
    height = request.form['height']
    weight = request.form['weight']
    gender = request.form['gender']
    bmi = calculate_bmi(float(weight), float(height))


    # Insert user details into the database
    query = "INSERT INTO users (name, age, height, weight, gender, bmi) VALUES (%s, %s, %s, %s, %s)"
    values = (name, age, height, weight, gender, bmi)
    cursor.execute(query, values)
    mydb.commit()

    return "Data inserted successfully!"

   # return the user's details from the database
    cursor.execute("SELECT * FROM users WHERE id=%s", (cursor.lastrowid,))
    result = cursor.fetchone()
    return render_template('', result=result)

# route to handle the form 2 submission
@app.route('/submit1', methods=['POST'])
def submit1():
    name1 = request.form['name']
    age1 = request.form['age']
    stress_level = request.form['stress_level']
    activity_level = request.form['activity_level']
    
    # return the user's details from the database
    return render_template('', name=name1, age=age1, stress_level=stress_level, activity_level=activity_level)

# route to handle the form submission and match the entered values with the database
@app.route('/submit2', methods=['POST'])
def submit():
    # get the medical complications entered by the user
    medical_complications = request.form.getlist('medical_complications')

    # create a connection to the database
    mydb1 = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="medical_complications")
    
    # create a cursor object to execute SQL queries
    cursor = mydb1.cursor()
     # create an empty list to store the matching yoga asanas and dietary habits
    matching_results = []
    
    # iterate over each medical complication entered by the user
    for medical_complication in medical_complications:
        # execute a SQL query to get the matching yoga asanas and dietary habits
        cursor.execute("SELECT yoga_asanas, dietary_habits FROM yoga_asanas WHERE medical_complication=?", (medical_complication,))
        
        # fetch all the matching results
        results = cursor.fetchall()
         # append the matching results to the list
        matching_results.extend(results)
    
    # close the connection to the database
    mydb1.close()
    
    # render the results template with the matching yoga asanas and dietary habits
    return render_template('result.html', matching_results=matching_results)

def mlModel(age_group, gender, stress_level, activity_level, occupation):
    # load the trained model
    with open('medical_complications_model.pkl', 'rb') as file:
        model = pickle.load(file)
    # # load the trained model
    # with open('medical_complications_model.pkl', 'rb') as file:
    #     model = pickle.load(file)
    #     age_group = request.form.get('age_group')
    #     gender = request.form.get('gender')
    #     stress_level = request.form.get('stress_level')
    #     activity_level = request.form.get('activity_level')
    #     occupation = request.form.get('occupation')
    #     # convert the user details to a list
    #     user_details = [age_group, gender, stress_level, activity_level, occupation]
        
        # make a prediction using the trained model
        # prediction = model.predict([user_details])[0]
        return model.predict([user_details])[0]
        
    # render the results template with the predicted medical complication
    return render_template('result.html', prediction=prediction)

    
if __name__== '_main_':
    app.run(debug=True)