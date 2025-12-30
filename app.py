import streamlit as st
import pickle
import pandas as pd
import requests
movies=pickle.load(open('movies.pkl', 'rb')) 
similarity = pickle.load(open('similarity.pkl', 'rb'))
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=b5c91a054d2457d189d7880273d00a87&language=en-US"
    pramas={"api_key":"b5c91a054d2457d189d7880273d00a87",}
    response = requests.get(url.format(movie_id),params=pramas)
    data= requests.get(url) 
    data = response.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path
def recommended(movie):
     movie_index = movies[movies['title'] == movie].index[0]
     distances = similarity[movie_index]

     movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]
     recommended_names =[]
     recommended_posters = []
     for i in movies_list:
        movie_id = movies.iloc[i[0]]['movie_id']
        recommended_names.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movies.iloc[i[0]]['movie_id']))

     return recommended_names,recommended_posters

st.header('Movie Recommender System')
       
selected_movie= st.selectbox(
         'Select a movie you like', 
         movies['title'].values)    
    
if st.button("Recommend"):
    names,posters= recommended(selected_movie)


    col1, col2, col3, col4, col5= st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:

        st.text(names[1])

        st.image(posters[1])

    with col3:

        st.text(names[2])
        st.image(posters[2])

    with col4:

       st.text(names[3])
       st.image(posters[3])

    with col5:

      st.text(names[4])
      st.image(posters[4])