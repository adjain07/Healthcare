from flask import Flask,render_template,url_for,request
import sqlite3

import joblib
model = joblib.load('./models/randomforest_model.lb')
app = Flask(__name__)

@app.route('/')  # http://127.0.0.1:5000
def home():
    return render_template('home.html')

@app.route('/project')    # http://127.0.0.1:5000/project
def project():
    return render_template('project.html') 

@app.route("/prediction",methods=['GET','POST'])
def prediction():
    if  request.method == "POST":

        age = int(request.form["age"])

        gender = int(request.form["gender"])

        blood = request.form["blood"]
        A_positive = 0
        A_negative = 0
        B_positive = 0
        B_negative = 0
        O_positive = 0
        O_negative = 0
        Ab_positive = 0
        if blood == "A+":
            A_positive = 1
        elif blood == "A-":
            A_negative = 1
        elif blood == "B+":
            B_positive = 1
        elif blood == "B-":
            B_negative = 1
        elif blood == "O+":
            O_positive = 1
        elif blood == "O-":
            O_negative = 1
        elif blood == "AB+":
            Ab_positive = 1

        condition = request.form["condition"]
        Arthritis = 0
        Diabetes = 0
        Hypertension = 0
        Obesity = 0
        Cancer = 0
        if condition == "Arthritis":
            Arthritis = 1
        elif condition == "Diabetes":
            Diabetes = 1
        elif condition == "Hypertension":
            Hypertension = 1
        elif condition == "Obesity":
            Obesity = 1
        elif condition == "Cancer":
            Cancer = 1

        insurance = request.form["insurance"]
        Cigna = 0
        Medicare = 0
        United_Healthcare = 0
        Blue_Cross = 0
        if insurance == "Cigna":
            Arthritis = 1
        elif insurance == "Medicare":
            Medicare = 1
        elif insurance == "United Healthcare":
            United_Healthcare = 1
        elif insurance == "Blue Cross":
            Blue_Cross = 1

        admission = request.form["admission"]
        Elective = 0
        Urgent = 0
        if admission == "Elective":
            Arthritis = 1
        elif admission == "Urgent":
            Urgent = 1

        test = request.form["test"]
        Abnormal = 0
        Normal = 0
        if test == "Abnormal":
            Arthritis = 1
        elif test == "Normal":
            Normal = 1

        UNSEEN_DATA = [[age, gender, 
                        A_positive, A_negative,B_positive,B_negative,O_positive,O_negative,Ab_positive,
                        Arthritis,Diabetes,Hypertension,Obesity,Cancer,
                        Cigna,Medicare,United_Healthcare,Blue_Cross,
                        Elective,Urgent,
                        Abnormal,Normal]]
        
        prediction = model.predict(UNSEEN_DATA)[0]
        prediction = round(prediction,2)

        # return label[str(prediction)]
        return render_template('output.html',output=prediction,
                            )

if __name__ == "__main__":
    app.run(debug=True)