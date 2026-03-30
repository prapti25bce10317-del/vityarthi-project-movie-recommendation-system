# 🎬 Movie Recommendation System 

## 📌 Overview
This project is a content-based movie recommendation system that suggests movies similar to a selected movie. It uses Natural Language Processing (NLP) techniques and cosine similarity to find relationships between movies based on their features.

---

## 🎯 Problem Statement
With thousands of movies available, users often struggle to find relevant content. This project aims to solve that problem by recommending movies based on similarity in content such as genre, cast, keywords, and overview.

---

## 🧠 Approach
1. Data Collection: TMDB 5000 Movie Dataset
2. Data Preprocessing: Cleaning and merging datasets
3. Feature Engineering: Combining important features into a single "tags" column
4. Vectorization: Using CountVectorizer to convert text into numerical vectors
5. Similarity Calculation: Using cosine similarity to find similar movies
6. Recommendation: Returning top 5 similar movies

---

## ⚙️ Technologies Used
- Python
- Pandas
- Scikit-learn
- Streamlit

---

## ▶️ How to Run the Project

### 1. Clone the Repository
git clone https://github.com/prapti25bce10317-del/vityarthi-project-movie-recommendation-system.git
cd vityarthi-project-movie-recommendation-system


### 2. Install Dependencies
pip install -r requirements.txt


### 3. Run the App
streamlit run app.py


## 📂 Project Structure

- src/ → Core ML logic  
- data/ → Dataset files  
- notebooks/ → Analysis  
- models/ → Model info  
- app.py → Streamlit app  
- requirements.txt → Dependencies



---

## 💡 Features
- Movie recommendation based on content similarity
- Interactive UI using Streamlit
- Real-world dataset usage
- Modular code structure

---

## 🚧 Challenges Faced
- Handling large dataset efficiently
- Feature extraction from JSON-like columns
- Performance optimization using caching

---

## 📈 Future Improvements
- Add movie posters using API
- Use advanced models like TF-IDF or deep learning
- Deploy the application online

---



