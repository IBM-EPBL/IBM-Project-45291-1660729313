
import pickle
import time

import joblib
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas
import requests
from flask import Flask, render_template, request


app = Flask(__name__)
model=pickle.load(open('heart.pkl','rb'))
scale=pickle.load(open('scale.pkl','rb'))
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict',methods=["POST","GET"])
def predict():
    if request.method == 'POST':

        age = int(request.form['age'])
        gender = request.form.get('gender')
        cp = request.form.get('cp')
        trestbps = int(request.form['trestbps'])
        chol = int(request.form['chol'])
        fbs = request.form.get('fbs')
        restecg = int(request.form['restecg'])
        thalach = int(request.form['thalach'])
        exang = request.form.get('exang')
        oldpeak = float(request.form['oldpeak'])
        slope = request.form.get('slope')
        ca = int(request.form['ca'])
        thal = request.form.get('thal')
        
        data = np.array([[age,gender,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        prediction = model.predict(data)
    if prediction == "Yes":
        return render_template("chance.html")
    else:
        return render_template("nochance.html")
if __name__ == "__main__": 
  app.run(debug=True)            
