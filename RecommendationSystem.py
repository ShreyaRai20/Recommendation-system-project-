import numpy as np # for array

# dataframes are structured table. 
# it is better to load csv file as datadrame 
# as we can do better data analysis using dataframe.

import pandas as pd 

# For Visualisations

import matplotlib.pyplot as plt
import seaborn as sns

# For algorithm

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

credits = pd.read_csv('tmdb_5000_credits.csv')
movies = pd.read_csv('tmdb_5000_movies.csv')

credits.head()

movies.head()

# below two code snippets gives us info on the movie dataframe.
# and we got to know that 3 rows in overview colomn is empty.

movies.shape

movies.info()

# TfidfVectorizer
# converting overview column of movie dataframe into TFIDF feature.

tfidf = TfidfVectorizer(stop_words = 'english') # remove common english words.
movies['overview'] = movies['overview'].fillna("") # handling missing values.

# Creating a Vector Space Model of Overview column from movie dataset.
tfidf_matrix = tfidf.fit_transform(movies ['overview']) 

# finding consine similarity.
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

#indices = pd.Series(movies.index, index = movies['original_title']).drop_dublicates()
#indices

indices = pd.Series(movies.index, index=movies['original_title']).drop_duplicates()
indices

indices['The Matrix']

# Function to extract top 10 similar movies/ recommendations.

def get_recommendations(title, cosine_sim = cosine_sim):
    idx = indices[title]
    sim_scores = enumerate(cosine_sim[idx])
    sim_scores = sorted(sim_scores, key = lambda x: x[1], reverse = True)
    sim_scores = sim_scores[1:11]
    sim_index =[i[0]for i in sim_scores]
    return movies['original_title'].iloc[sim_index].tolist()