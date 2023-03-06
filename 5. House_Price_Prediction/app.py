import streamlit as st
import pandas as pd
import numpy as np
import pickle

model=pickle.load(open('model.pkl','rb'))
data=pd.read_csv('cleaned_data.csv')
loc=data['location'].unique()



st.title('Bangalore House Price Prediction')
location = st.selectbox("Select Location: ",sorted(list(loc)))
bhk=st.number_input('Enter BHK:')
bath=st.number_input('Enter number of Bathrooms:')
sqft=st.number_input('Enter Total Square Feet:')

if st.button('Predict'):
    result=model.predict(pd.DataFrame([[location,sqft,bath,bhk]],columns=['location','total_sqft','bath','bhk']))
    st.header(f'Price of House : Rs.{np.round(result[0]*100000,2)}')
