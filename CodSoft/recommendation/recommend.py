import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.neighbors import NearestNeighbors

def load_data():
    books = pd.read_csv('data/books.csv')
    ratings = pd.read_csv('data/ratings.csv')
    users = pd.read_csv('data/users.csv')
    return books, ratings, users

def preprocess_data(ratings):
    ratings['Book-Rating'] = ratings['Book-Rating'].astype(float)
    user_item_matrix = ratings.pivot(index='User-ID', columns='ISBN', values='Book-Rating')
    return user_item_matrix

def train_model(user_item_matrix):
    similarity_matrix = cosine_similarity(user_item_matrix.fillna(0))
    cf_model = NearestNeighbors(metric='cosine', algorithm='brute')
    cf_model.fit(user_item_matrix.fillna(0))
    return cf_model, similarity_matrix

def recommend(book_name, books, ratings):
    user_item_matrix = preprocess_data(ratings)
    cf_model, similarity_matrix = train_model(user_item_matrix)
    
    book_row = books[books['Book-Title'].str.lower() == book_name.lower()]
    if book_row.empty:
        return []

    book_isbn = book_row['ISBN'].values[0]
    if book_isbn not in user_item_matrix.columns:
        return []

    index = list(user_item_matrix.columns).index(book_isbn)
    similar_books = sorted(list(enumerate(similarity_matrix[index])), key=lambda x: x[1], reverse=True)[1:6]
    
    data = []
    for idx, _ in similar_books:
        temp_df = books[books['ISBN'] == user_item_matrix.columns[idx]]
        item = [temp_df['Book-Title'].values[0], temp_df['Book-Author'].values[0], temp_df['Image-URL-M'].values[0]]
        data.append(item)
    return data
