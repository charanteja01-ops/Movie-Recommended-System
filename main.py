

from fastapi import FastAPI ,Body, Query
#from requests import put
app = FastAPI()

movies = [
    {"id": 1, "movie name": "3 Idiots", "genre": "Comedy", "language": "Hindi", "rating": 8},
    {"id": 2, "movie name": "Dangal", "genre": "Sport", "language": "Hindi", "rating": 8},
    {"id": 3, "movie name": "Baahubali 2", "genre": "Action", "language": "Telugu", "rating": 8},
    {"id": 4, "movie name": "RRR", "genre": "Action", "language": "Telugu", "rating": 7},
    {"id": 5, "movie name": "KGF Chapter 2", "genre": "Action", "language": "Kannada", "rating": 8},
    {"id": 6, "movie name": "Kantara", "genre": "Thriller", "language": "Kannada", "rating": 8},
    {"id": 7, "movie name": "Drishyam 2", "genre": "Thriller", "language": "Malayalam", "rating": 8},
    {"id": 8, "movie name" : "2018", "genre": "Drama", "language": "Malayalam", "rating": 8},
    {"id": 9, "movie name": "Vikram", "genre": "Action", "language": "Tamil", "rating": 8},
    {"id": 10, "movie name": "Jawan", "genre": "Action", "language": "Hindi", "rating": 7},
    {"id": 11, "movie name": "Pathaan", "genre": "Action", "language": "Hindi", "rating": 6},
    {"id": 12, "movie name": "Gadar 2", "genre": "Action", "language": "Hindi", "rating": 7},
    {"id": 13, "movie name": "Animal", "genre": "Action", "language": "Hindi", "rating": 6},
    {"id": 14, "movie name": "Salaar", "genre": "Action", "language": "Telugu", "rating": 6},
    {"id": 15, "movie name": "Leo", "genre": "Action", "language": "Tamil", "rating": 7},
    {"id": 16, "movie name": "Jailer", "genre": "Comedy", "language": "Tamil", "rating": 7},
    {"id": 17, "movie name": "Ponniyin Selvan 2", "genre": "Drama", "language": "Tamil", "rating": 7},
    {"id": 18, "movie name": "Pushpa 2", "genre": "Action", "language": "Telugu", "rating": 8},
    {"id": 19, "movie name": "Kalki 2898 AD", "genre": "Sci-Fi", "language": "Telugu", "rating": 7},
    {"id": 20, "movie name": "Devara", "genre": "Action", "language": "Telugu", "rating": 7},
    {"id": 21, "movie name": "Lucky Baskhar", "genre": "Crime", "language": "Telugu", "rating": 8},
    {"id": 22, "movie name": "Amaran", "genre": "Biography", "language": "Tamil", "rating": 7},
    {"id": 23, "movie name": "Sita Ramam", "genre": "Romance", "language": "Telugu", "rating": 8},
    {"id": 24, "movie name": "Manjummel Boys", "genre": "Thriller", "language": "Malayalam", "rating": 8},
    {"id": 25, "movie name": "Aavesham", "genre": "Comedy", "language": "Malayalam", "rating": 7},
    {"id": 26, "movie name": "The Goat Life", "genre": "Drama", "language": "Malayalam", "rating": 7},
    {"id": 27, "movie name": "Hridayam", "genre": "Romance", "language": "Malayalam", "rating": 8},
    {"id": 28, "movie name": "Shershaah", "genre": "Biography", "language": "Hindi", "rating": 8},
    {"id": 29, "movie name": "Uri", "genre": "Action", "language": "Hindi", "rating": 8},
    {"id": 30, "movie name": "Chhaava", "genre": "History", "language": "Hindi", "rating": 7},
    {"id": 31, "movie name": "Article 370", "genre": "Thriller", "language": "Hindi", "rating": 7},
    {"id": 32, "movie name": "Bramayugam", "genre": "Horror", "language": "Malayalam", "rating": 7},
    {"id": 33, "movie name": "Premalu", "genre": "Romance", "language": "Malayalam", "rating": 7},
    {"id": 34, "movie name": "Lubber Pandhu", "genre": "Sport", "language": "Tamil", "rating": 8},
    {"id": 35, "movie name": "Maharaja", "genre": "Thriller", "language": "Tamil", "rating": 8},
    {"id": 36, "movie name": "Captain Miller", "genre": "Action", "language": "Tamil", "rating": 7},
    {"id": 37, "movie name": "HanuMan", "genre": "Fantasy", "language": "Telugu", "rating": 7},
    {"id": 38, "movie name": "Fighter", "genre": "Action", "language": "Hindi", "rating": 6},
    {"id": 39, "movie name": "Tiger 3", "genre": "Action", "language": "Hindi", "rating": 6},
    {"id": 40, "movie name": "OMG 2", "genre": "Comedy", "language": "Hindi", "rating": 7}
]

@app.get("/")
def home_page():
    return {"message": "welcome to the world of movies"}

@app.get("/movies_filter")
def filter_movies(
    genre:    str = Query(None, description="Filter by genre"),
    language: str = Query(None, description="Filter by language"),
    rating:   int = Query(None, description="Filter by minimum rating"),
):
    
    result = []
    for movie in movies:
        if genre    and movie["genre"]    != genre:              continue
        if language and movie["language"] != language:           continue
        if rating   and movie["rating"]   != rating:             continue
        result.append(movie)
    return result

@app.get("/view_all_movies")
def get_all_movies():
    return movies


@app.get("/get_a_movie/{movie_id}")
def get_movie_by_id(movie_id: int):
    for movie in movies:
        if movie["id"] == movie_id:
            return movie
    return {"message": "Movie not found"}

@app.post("/add_movies")
def add_movie(movie: dict = Body()):
    movies.append(movie)
    return {"message": "Movie added successfully", "movie": movie}




@app.put("/update_movies/{movie_id}")
def update_movie(
    movie_id: int,
    movie_name: str,
    genre: str,
    language: str,
    rating: float
):
    dict_ = {
        "id": movie_id,
        "movie name": movie_name,
        "genre": genre,
        "language": language,
        "rating": rating
    }

    for i in range(len(movies)):
        if movies[i]["id"] == movie_id:
            movies[i].update(dict_)
            return {
                "message": "Movie updated successfully",
                "movie": movies[i]
            }

    return {"message": "Movie not found"}



@app.delete("/delete_movies/{movie_id}")
def delete_movie(movie_id: int):
    for movie in range(len(movies)):
        if movies[movie]["id"] == movie_id:
            deleted_movie = movies.pop(movie)
            return {"message": "Movie deleted successfully", "movie": deleted_movie}
    return {"message": "Movie not found","remaining movies": movies}