from flask import Flask, render_template, request, jsonify, redirect, url_for
import os
import json
import requests

app = Flask(__name__)

# Fonction pour récupérer les films depuis l'API TMDB
def fetch_movies(url):
    headers = {
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2MTdhNGZlNWQ1MzI2ZDk0ZTI3ZDI3YTRiODQzMmFlZSIsInN1YiI6IjY1YjUyZmYwNmUwZDcyMDE0OTQ3MDg3MyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.QCiPm9TC11xtADfyp2jr85Z_aBvWLaEzaJjWeqC7ZM4',
        'Accept': 'application/json'
    }
    response = requests.get(url, headers=headers)
    return response.json()['results'] if response.status_code == 200 else []

# Fonction pour récupérer les détails d'un film à partir de l'API TMDB
def fetch_movie_details(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?language=en-US'
    headers = {
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2MTdhNGZlNWQ1MzI2ZDk0ZTI3ZDI3YTRiODQzMmFlZSIsInN1YiI6IjY1YjUyZmYwNmUwZDcyMDE0OTQ3MDg3MyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.QCiPm9TC11xtADfyp2jr85Z_aBvWLaEzaJjWeqC7ZM4',
        'Accept': 'application/json'
    }
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else None




# Route pour récupérer les données des films populaires
@app.route('/get-movies')
def get_movies():
    url = 'https://api.themoviedb.org/3/movie/popular?language=en-US&page=1'
    movies_data = fetch_movies(url)
    return jsonify(movies_data)

# Route pour effectuer une recherche de films
@app.route('/search-movies')
def search_movies():
    search_query = request.args.get('query')
    url = f'https://api.themoviedb.org/3/search/movie?query={search_query}&language=en-US&page=1'
    movies_data = fetch_movies(url)
    return jsonify(movies_data)
# Route pour afficher les détails d'un film
@app.route('/movie-details/<int:movie_id>')
def movie_details(movie_id):
    movie = fetch_movie_details(movie_id)
    if movie:
        return render_template('movie.html', movie=movie)
    else:
        return render_template('error.html', message="Détails du film non disponibles.")


@app.route('/')
def home():
    return render_template('videotheque.html')

@app.route('/connexion')
def formulaire():
    return render_template('connexion.html')

@app.route('/inscription')
def inscription():
    return render_template('inscription.html')



@app.route('/inscription_success')
def inscription_success():
    username = request.args.get('username')
    return render_template('inscription_success.html', username=username)

@app.route('/videotheque')
def videotheque():
    # Récupérer les films depuis l'API TMDB
    movies = fetch_movies('https://api.themoviedb.org/3/movie/popular?language=en-US&page=1')
    return render_template('videotheque.html', movies=movies)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    print(f"Starting the app on port {port}")
    app.run(debug=True, host='0.0.0.0', port=port, use_reloader=True)
