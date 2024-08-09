import streamlit as st
import pickle
import pandas as pd


def main_func(movie):
    movie_index = movieslis[movieslis['title']==movie].index[0]
    distances = similarity[movie_index]
    movie_lists = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recco_movie = []
    for i in movie_lists:
       recco_movie.append(movieslis.iloc[i[0]].title)
    return recco_movie

movies_dict = pickle.load(open("listmovie.pkl",'rb'))
movieslis = pd.DataFrame(movies_dict)
similarity = pickle.load(open("similarity.pkl",'rb'))

st.title("Movie Recommendation System")
selected_movie = st.selectbox('Movies Recommendation',(movieslis["title"]))
st.write("Recommendations:",selected_movie)

if st.button("Recommend"):

    reco = main_func(selected_movie)
    for i in reco:
        st.write(i)