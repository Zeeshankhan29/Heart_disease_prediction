from sklearn.metrics import accuracy_score,classification_report
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestClassifier
import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import streamlit as st
# from streamlit_option_menu import option_menu

#Pickling the Model
with open('Random_forest','rb') as f:
    Rf = pickle.load(f)


#Defining the title
st.title('Heart Disease Prediction')


#Defining the parameter
Age = st.text_input('Enter your Age')
# Sex = st.text_input('Sex')
option = st.selectbox('Sex',('Male', 'Female'))
if option =='Male':
    Sex = 1
else:
    Sex = 0
cp = st.text_input('Chest_pain_type')
trestbps = st.text_input('Resting_Blood_Pressure')
chol = st.text_input('Serum_cholestoral_in_mg')
fbs = st.text_input('Fasting_blood_sugar_>_120_mg/dl')
restecg = st.text_input('Resting_electrocardiographic_results')
thalach = st.text_input('Maximum_heart_rate_achieved')
exang = st.text_input('Exercise_induced_angina')
oldpeak = st.text_input('Oldpeak')
Slope = st.text_input('Slope')
ca = st.text_input('Number_of_major_vessels')
thal = st.text_input('Thal') 


#Code for Prediction
Prediction = " "

#Creating a button for Prediction
if st.button('Heart Disease Prediction'):
    result = Rf.predict([[Age,Sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,Slope,ca,thal]])
    if result[0] == 1:
        Prediction = 'Heart issue Please Consult a Doctor Immediately'
    else:
        Prediction = 'Heart is in Good Condition'
st.success(Prediction)
