import streamlit as st,requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_icon='🎬', page_title='Movie Recommendation System')
st.title("🎬 Movie Recommendation System")
st.write("Welcome to the Movie Recommendation System! Explore and discover movies based on your preferences.")

with st.sidebar:
    st.title("**MOVIES**")
    options = st.selectbox("**CHOOSE YOUR OPTION**", options=["movies_filter","view_all_movies","get_a_movie","add_movies","update_movies","delete_movies"], index=None)

if options == "view_all_movies":
    st.subheader("View all movies")
    response=requests.get(f"{API_URL}/view_all_movies")
    if response.status_code == 200:
        st.write(response.json())  
    else:
        st.error("Failed to fetch movies. Please try again later.")

elif options == "movies_filter":
    st.subheader("Filter movies")
    movie_genre = st.selectbox("Enter the genre of the movie", options=["Action", "Comedy", "Sport", "Thriller", "Drama", "Sci-Fi", "Crime", "Biography", "Romance", "History", "Horror", "Fantasy"],index=None)
    movie_language = st.selectbox("Enter the language of the movie",options=["Hindi", "Telugu", "Kannada", "Malayalam", "Tamil"],index=None)
    movie_rating = st.number_input("Enter the rating of the movie", min_value=0, max_value=10, step=1)
    if st.button("Filter Movies"):
        response = requests.get(f"{API_URL}/movies_filter", params={"genre": movie_genre, "language": movie_language, "rating": movie_rating})
        if response.status_code == 200:
            st.write(response.json())
        else:
            st.error("movies not found")

elif options == "get_a_movie":
    st.subheader("Get a movie by id")
    movie_id = st.number_input("Enter the movie id", min_value=1, step=1)
    if st.button("Get Movie"):
        response = requests.get(f"{API_URL}/get_a_movie/{movie_id}")
        if response.status_code == 200:
            st.write(response.json())
        else:
            st.error("Movie not found,Please check the ID and try again.")

elif options == "add_movies":
    st.subheader("Add a new movie")
    movie_id = st.number_input("Enter the movie id", min_value=1, step=1)
    movie_name = st.text_input("Enter the movie name")
    movie_genre = st.selectbox("Enter the genre of the movie", options=["Action", "Comedy", "Sport", "Thriller", "Drama", "Sci-Fi", "Crime", "Biography", "Romance", "History", "Horror", "Fantasy"],index=None)
    movie_language = st.selectbox("Enter the language of the movie",options=["Hindi", "Telugu", "Kannada", "Malayalam", "Tamil"],index=None)
    movie_rating = st.number_input("Enter the rating of the movie", min_value=0, max_value=10, step=1)
    if st.button("Add Movie"):
        movie_data = {
            "id": movie_id,
            "movie name": movie_name,
            "genre": movie_genre,
            "language": movie_language,
            "rating": movie_rating
        }
        response = requests.post(f"{API_URL}/add_movies", json=movie_data)
        if response.status_code == 200:
            st.success(response.json())
        else:
            st.error("Failed to add movie. Please try again later.")

elif options == "update_movies":
    st.subheader("Update a movie")
    movie_id = st.number_input("Enter the movie id", min_value=1, step=1)
    movie_name = st.text_input("Enter the new movie name")
    movie_genre = st.selectbox("Enter the new genre of the movie", options=["Action", "Comedy", "Sport", "Thriller", "Drama", "Sci-Fi", "Crime", "Biography", "Romance", "History", "Horror", "Fantasy"],index=None)
    movie_language = st.selectbox("Enter the new language of the movie",options=["Hindi", "Telugu", "Kannada", "Malayalam", "Tamil"],index=None)
    movie_rating = st.number_input("Enter the new rating of the movie", min_value=0, max_value=10, step=1)
    if st.button("Update Movie"):
        response = requests.put(f"{API_URL}/update_movies/{movie_id}?movie_name={movie_name}&genre={movie_genre}&language={movie_language}&rating={movie_rating}")
        if response.status_code == 200:
            st.success(response.json())
        else:
            st.error("Failed to update movie. Please check the ID and try again.")

elif options == "delete_movies":
    st.subheader("Delete a movie")
    movie_id = st.number_input("Enter the movie id", min_value=1, step=1)
    if st.button("Delete Movie"):
        response = requests.delete(f"{API_URL}/delete_movies/{movie_id}")
        if response.status_code == 200:
            st.success(response.json())
        else :
            st.error("Failed to delete movie. Please check the ID and try again.")