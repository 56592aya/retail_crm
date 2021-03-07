from flask import Flask, render_template, url_for, request, flash, jsonify
import pickle
import joblib
import sys
import os
sys.path.insert(1, '../src/')
import config
import pandas as pd


app = Flask(__name__)

#removed key in app
# app.config['SECRET_KEY'] = '***************************'


@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html')

#make options for reading the data fram
#make options for training within the app
#make jsonify
@app.route('/predict',methods=['POST'])
def predict():
    return render_template('result.html')

if __name__ == "__main__":
    app.run(debug=True)
    