import streamlit as st
from src.data_preprocessing import load_data
from src.feature_engineering import transform_data
from src.model import create_similarity
from src.recommender import recommend

st.title(" Movie Recommendation System")

# Load and process data
movies = load_data()
movies = transform_data(movies)
similarity = create_similarity(movies)

movie_list = movies['title'].values
selected_movie = st.selectbox("Select a movie", movie_list)

if st.button("Recommend"):
    recommendations = recommend(selected_movie, movies, similarity)
    for movie in recommendations:
        st.write(movie)
