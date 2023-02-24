import pandas as pd
import streamlit as st
import pickle
data=pd.read_csv('cleaned_data.csv')
model=pickle.load(open('model.pkl','rb'))


st.title('Car Price Prediction')
company=st.selectbox('Select Company:',sorted(list(data['company'].unique())))
name=st.selectbox('Select Model:',sorted(list(data['name'].unique())))
year=st.selectbox('Select year:',sorted(list(data['year'].unique()),reverse=True))
fuel=st.selectbox('Select year:',sorted(list(data['fuel_type'].unique())))
kms=st.number_input('Number of kms driven:')


if st.button('Predict Price'):
    prediction=model.predict(pd.DataFrame([[name,company,year,int(kms),fuel]],columns=['name','company','year','kms_driven','fuel_type']))
    st.subheader(f'Price of {name} : {prediction[0]}')