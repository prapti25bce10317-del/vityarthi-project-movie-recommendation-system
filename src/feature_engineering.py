import ast

def convert(text):
    L = []
    for i in ast.literal_eval(text):
        L.append(i['name'])
    return L

def fetch_director(text):
    L = []
    for i in ast.literal_eval(text):
        if i['job'] == 'Director':
            L.append(i['name'])
    return L

def transform_data(movies):
    movies.dropna(inplace=True)

    movies['genres'] = movies['genres'].apply(convert)
    movies['keywords'] = movies['keywords'].apply(convert)
    movies['cast'] = movies['cast'].apply(lambda x: convert(x)[0:3])
    movies['crew'] = movies['crew'].apply(fetch_director)

    # Remove spaces
    movies['genres'] = movies['genres'].apply(lambda x: [i.replace(" ", "") for i in x])
    movies['keywords'] = movies['keywords'].apply(lambda x: [i.replace(" ", "") for i in x])
    movies['cast'] = movies['cast'].apply(lambda x: [i.replace(" ", "") for i in x])
    movies['crew'] = movies['crew'].apply(lambda x: [i.replace(" ", "") for i in x])

    movies['overview'] = movies['overview'].apply(lambda x: x.split())

    # Combine all features
    movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']

    # Convert list to string
    movies['tags'] = movies['tags'].apply(lambda x: " ".join(x))

    return movies[['movie_id', 'title', 'tags']]