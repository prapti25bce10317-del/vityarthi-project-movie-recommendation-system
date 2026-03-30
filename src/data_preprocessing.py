from src.config import DATA_PATH_MOVIES, DATA_PATH_CREDITS
import pandas as pd

def load_data():
    movies = pd.read_csv(DATA_PATH_MOVIES)
    credits_df = pd.read_csv(DATA_PATH_CREDITS)

    movies = movies.merge(credits_df, on='title')

    movies = movies[['movie_id','title','overview','genres','keywords','cast','crew']]

    return movies