import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    anime_index = anime[anime['name']==movie].index[0]
    cos_simi = similarity[anime_index]
    anime_list = sorted(list(enumerate(cos_simi)),reverse=True,key=lambda x:x[-1])[1:6]
    
    recommended_movies = []
    for i in anime_list:
        recommended_movies.append(anime.iloc[i[0]]['name'])
    
    return recommended_movies


anime_dict = pickle.load(open('movies_dict.pkl','rb'))
anime = pd.DataFrame(anime_dict)

similarity = pickle.load(open('similarity.pkl','rb'))


st.title("Anime Recommender System")

#Adding Form like structure to see list of all Anime
selected_anime_name = st.selectbox(
    'Choose an Anime to get Recommendations',
    anime['name'].values
)

#Adding a Button
if st.button('Recommend'):
    recommendations = recommend(selected_anime_name)
    for i in recommendations:
        st.write(i)
