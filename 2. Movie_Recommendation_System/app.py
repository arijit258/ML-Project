import streamlit as st
import pickle
import pandas as pd
import numpy as np
import requests

movie_dict=pickle.load(open('movies.pkl','rb'))
movies=pd.DataFrame(movie_dict)
similarity=pickle.load(open('similarity.pkl','rb'))
api_key='00c797fbe9dd573f70cffbb306e77a38'


# Fetching the poster
def fetch_poster(movie_id):
    response=requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&langauge=en-US')
    data=response.json()
    return "https://image.tmdb.org/t/p/w500"+data['poster_path']


# Function which recommends 5 movies
def recommend(movie):
    # Fetching the index oof movie in movie dataset
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x : x[1])[1:6]
    recommended_movies=[]
    recommended_movies_poster=[]
    vote=[]
    overview=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        vote.append(movies.iloc[i[0]].rating)
        overview.append(movies.iloc[i[0]].overview)
        # Fetch poster from API using movie id
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_poster,vote,overview


st.title('Movie Recommendation System')
selected_movie= st.selectbox("Select Your Movie...",movies['title'].values)

if st.button('Recommend'):
    names,posters,vote,overview=recommend(selected_movie)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
        st.write(f'Rating : {vote[0]}')
        st.write(f'Overview :\n {overview[0]}')
    with col2:
        st.text(names[1])
        st.image(posters[1])
        st.write(f'Rating : {vote[1]}')
        st.write(f'Overview :\n{overview[1]}')
    with col3:
        st.text(names[2])
        st.image(posters[2])
        st.write(f'Rating : {vote[2]}')
        st.write(f'Overview :\n{overview[2]}')
    with col4:
        st.text(names[3])
        st.image(posters[3])
        st.write(f'Rating : {vote[3]}')
        st.write(f'Overview :\n{overview[3]}')
    with col5:
        st.text(names[4])
        st.image(posters[4])
        st.write(f'Rating : {vote[4]}')
        st.write(f'Rating : {overview[4]}')