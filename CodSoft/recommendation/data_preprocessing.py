import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer


books = pd.read_csv('data/books.csv')


def clean_text(author):
    return str(author).lower().replace(' ', '')

books['Book-Author'] = books['Book-Author'].apply(clean_text)
books['Book-Title'] = books['Book-Title'].str.lower()
books['Publisher'] = books['Publisher'].str.lower()


books['data'] = books[['Book-Title', 'Book-Author', 'Publisher']].apply(lambda x: ' '.join(x.dropna().astype(str)), axis=1)


vectorizer = CountVectorizer()
vectorized = vectorizer.fit_transform(books['data'])
