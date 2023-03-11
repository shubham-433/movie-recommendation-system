import streamlit as st
import pickle
import pandas as pd
import requests
import json

def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=ab7efc1c88a94d161fde923d779d463a&language=en-US'.format(movie_id))
    data=response.json()
    # st.text('https://api.themoviedb.org/3/movie/{}?api_key=ab7efc1c88a94d161fde923d779d463a&language=en-US'.format(movie_id))
    return "http://image.tmdb.org/t/p/w500/"+data["poster_path"]


def recommend(movie):
      movie_index= movies[movies['title']== movie].index[0]
      distance=similarity[movie_index]
      movies_lsit=sorted(list(enumerate(distance)),reverse=True ,key=lambda x:x[1])[1:6]
      recommended_movies=[]
      recommended_movies_poster=[]

      for i in movies_lsit:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetching image from api
        recommended_movies_poster.append(fetch_poster(movie_id))
      return recommended_movies,recommended_movies_poster

# movies_lsit=pickle.load(open('movies.pkl','rb'))
movies_dict=pickle.load(open('movie_dict.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))
movies=pd.DataFrame(movies_dict)

# movies_lsit=movies_lsit['title'].values
st.title("Movei Recommendation System")
selected_movie_name = st.selectbox(
    'Enter the name of the movie',
    movies['title'].values)

st.write('You selected:', selected_movie_name)

if st.button('Recommend'):
    names,posters= recommend(selected_movie_name)
    # for i in names:
    #     st.write(i)
    col1,col2,col3,col4,col5=st.columns(5)
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

    


