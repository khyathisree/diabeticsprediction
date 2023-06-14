import sqlite3
from flask import Flask,jsonify,request,render_template
import pickle

app=Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST','GET'])
def predict():
    if request.method=='POST':
        pregnancies = int(request.form['pregnancies'])
        glucose = int(request.form['glucose'])
        blood_pressure = int(request.form['blood-pressure'])
        skin_thickness = int(request.form['skin-thickness'])
        insulin = int(request.form['insulin'])
        bmi = float(request.form['bmi'])
        diabetes_pedigree = float(request.form['diabetes-pedigree'])
        age = int(request.form['age'])
        data=[pregnancies,glucose,blood_pressure,skin_thickness,insulin,bmi,diabetes_pedigree,age]
        print(data)
        with open('model2.pickle','rb') as file:
            model=pickle.load(file)
        result=model.predict([data])
        print(result)
        if result[0]==0:
            outcome='No Diabetic'
        else:
            outcome='Diabetic Patient'
        print('Data has been inserted')
        return jsonify({'message':outcome})
    else:
        return render_template('predict.html')
        

@app.route('/patient', methods=['POST','GET'])
def showpatient():
    conn=sqlite3.connect('patient.db')
    cur=conn.cursor()
    cur.execute("SELECT * FROM PATIENTINFO")
    data=[]
    for i in cur.fetchall():
        patient={}
        patient['name']=i[0]
        patient['result']=i[1]
        data.append(patient)
    return render_template('showpatient.html',data=data)









if __name__=='__main__':
    app.run(host='0.0.0.0',debug=False,port=5000)