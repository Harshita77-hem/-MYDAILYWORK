import pickle
import streamlit as st
import requests

# -------- PAGE CONFIG --------
st.set_page_config(page_title="Movie Recommender", layout="wide")

# -------- LOAD MODEL --------
movies = pickle.load(open('model/movie_list.pkl','rb'))
similarity = pickle.load(open('model/similarity.pkl','rb'))

API_KEY = "7b88890e7c4f22b74c16a8ae3e7dbd04"


# -------- FETCH POSTER --------
def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
        data = requests.get(url).json()
        poster_path = data.get('poster_path')

        if poster_path:
            return "https://image.tmdb.org/t/p/w500" + poster_path
        else:
            return "https://via.placeholder.com/300x450?text=No+Image"
    except:
        return "https://via.placeholder.com/300x450?text=Error"


# -------- FETCH DETAILS --------
def fetch_details(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
        data = requests.get(url).json()

        overview = data.get('overview', 'No description available')
        rating = data.get('vote_average', 'N/A')
        release = data.get('release_date', 'N/A')

        return overview, rating, release
    except:
        return "No data", "N/A", "N/A"


# -------- RECOMMEND --------
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]

    distances = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda x: x[1]
    )

    names, posters, overviews, ratings, releases = [], [], [], [], []

    for i in distances[1:6]:

        movie_id = movies.iloc[i[0]]['id']

        names.append(movies.iloc[i[0]].title)
        posters.append(fetch_poster(movie_id))

        o, r, d = fetch_details(movie_id)
        overviews.append(o)
        ratings.append(r)
        releases.append(d)

    return names, posters, overviews, ratings, releases


# -------- UI --------
st.title("🎬 AI Movie Recommender System")

movie_list = movies['title'].values
selected_movie = st.selectbox("🔍 Search or select a movie", movie_list)


# -------- BUTTON --------
if st.button('✨ Show Recommendations'):

    names, posters, overviews, ratings, releases = recommend(selected_movie)

    cols = st.columns(5)

    for i in range(5):
        with cols[i]:

            st.image(posters[i], use_container_width=True)

            st.markdown(f"**{names[i]}**")
            st.caption(f"⭐ {ratings[i]} | 📅 {releases[i]}")

            with st.expander("📖 View Details"):
                st.write(overviews[i])


# -------- FOOTER --------
st.markdown("---")
st.caption("Built with ❤️ using Streamlit & TMDB API")
