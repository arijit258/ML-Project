import streamlit as st
import pickle
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


tfidf=pickle.load(open('vectorizer.pkl','rb'))
model=pickle.load(open('model.pkl','rb'))


def convert_text(text):
    ps=PorterStemmer()
    text=text.lower() # lowercase
    text=nltk.word_tokenize(text) # tokenize
    # Removing special characters
    y=[]
    for i in text:
        if i.isalnum():
            y.append(i)
    
    # Removing stopwords and punctuation
    y1=[]
    for i in y:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y1.append(i)
    
    result=[]
    for i in y1:
        result.append(ps.stem(i))
    return " ".join(result)
    






st.title('SMS/Email Spam Classifier')
msg=st.text_area('Enter the message')

if st.button('Check'):

    # 1. Preprocessing
    transformed_msg=convert_text(msg)

    # 2. Vectorize
    vector=tfidf.transform([transformed_msg])

    # 3. Evaluate
    prediction=model.predict(vector)[0]

    # 4. Show
    if prediction==1:
        st.header('This message is spam')
    else:
        st.header('This message is not spam')