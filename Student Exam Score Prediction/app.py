import streamlit as st
import numpy as np
import pandas as pd
import pickle
model=pickle.load(open('model.pkl','rb'))
mx=pickle.load(open('scale.pkl','rb'))

st.header('Student Exam Score Prediction')
predictors=['mother_education_level',
 'father_education_level',
 'mother_job',
 'father_job',
 'travel_time',
 'study_time',
 'absences',
 'math_sem1_grade',
 'math_sem2_grade',
 'attends_extra_paid_portuguese_classes',
 'portuguese_sem1_grade',
 'portuguese_sem2_grade']

with st.form("Exam_Form"):
    v1=st.selectbox('Mother"s education Level : ',("none","primary education (4th grade)","5th to 9th grade","secondary education","higher education"))
    v2=st.selectbox('Father"s education Level : ',("none","primary education (4th grade)","5th to 9th grade","secondary education","higher education"))
    v3=st.selectbox('Mother"s Job : ',('other','services','health','teacher','at_home'))
    v4=st.selectbox('Father"s Job : ',('other','services','health','teacher','at_home'))
    v5=st.selectbox('Travel Time : ',('<15 min', '15 to 30 min', '30 min. to 1 hour', '1 hour'))
    v6=st.selectbox('Study Time : ',('<2 hours', '2 to 5 hours', '5 to 10 hours', '>10 hours'))
    v7=st.text_input('Enter number of absences (0-93): ')
    v8=st.text_input('Mathmatics Sem-1 Grade (0-20): ')
    v9=st.text_input('Mathmatics Sem-2 Grade (0-20): ')
    v10=st.selectbox('Have you atttended any extra paid portugese classes? ',('yes','no'))
    v11=st.text_input('Portugese Sem-1 Grade (0-20): ')
    v12=st.text_input('Portugese Sem-2 Grade (0-20): ')

    if st.form_submit_button('Check Grade'):
        value=[v1,v2,v3,v4,v5,v6,v7,int(v8),int(v9),v10,int(v11),int(v12)]
        input_data=pd.DataFrame([value],columns=predictors)
        input_data['father_job']=input_data['father_job'].replace({'other':0,'services':1,'health':2,'teacher':3,'at_home':4}).astype('int64')
        input_data['mother_job']=input_data['mother_job'].replace({'other':0,'services':1,'health':2,'teacher':3,'at_home':4}).astype('int64')
        input_data['mother_education_level']=input_data['mother_education_level'].replace({
            "none" : 0,
            "primary education (4th grade)" : 1,
            "5th to 9th grade" : 2,
            "secondary education" : 3,
            "higher education" : 4,
        })
        input_data['father_education_level']=input_data['father_education_level'].replace({
            "none" : 0,
            "primary education (4th grade)" : 1,
            "5th to 9th grade" : 2,
            "secondary education" : 3,
            "higher education" : 4,
        })
        input_data['travel_time']=input_data['travel_time'].replace({
            "<15 min" : 1, 
            "15 to 30 min" : 2, 
            "30 min. to 1 hour" : 3, 
            "1 hour" : 4
        })
        input_data['study_time']=input_data['study_time'].replace({
            "<2 hours" : 1, 
            "2 to 5 hours" : 2, 
            "5 to 10 hours" : 3,
            ">10 hours" : 4
        })
        input_data['attends_extra_paid_portuguese_classes']=input_data['attends_extra_paid_portuguese_classes'].replace({'no':0,'yes':1}).astype('int64')
        input_data_sc=mx.transform(input_data)
        grade=model.predict(input_data_sc)[0]

        st.subheader(f'Grade : {round(grade)}/20')