import streamlit as st
import pickle
import pandas as pd

scale=pickle.load(open('scale.pkl','rb'))
model=pickle.load(open('model.pkl','rb'))

st.title('Diabetes Prediction System')


preg=st.number_input('Number of Pregnancies')
glucose=st.number_input('Glucose Level')
bp=st.number_input('Blood Pressure')
skin=st.number_input('Skin Thickness')
insulin=st.number_input('Insulin Level')
bmi=st.number_input('BMI')
dpf=st.number_input('Enter Diabetes Pedigree Function')
age=st.number_input('Enter your Age')

if st.button('Submit'):
    trf=scale.transform(pd.DataFrame([[preg,glucose,bp,skin,insulin,bmi,dpf,age]],columns=['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']))
    prediction=model.predict(trf)
    prediction='Diabetic' if prediction[0]==1 else 'Non-Diabetic'
    st.header(f'The Patient is {prediction}')