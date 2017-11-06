from flask import Flask, render_template
from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)
import pandas as pd

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/my-movies')
def list_user_movies():
    my_movies_rated = pd.read_csv('./data/my-ratings.csv', sep=',', header=0)
    all_movies = pd.read_csv('./data/movies.csv', sep=',', header=0)
    my_movies_rated = pd.merge(my_movies_rated, all_movies, on='movieId', how='inner')
    return render_template('my-movies.html', page_title='My Movies', my_movies_rated=my_movies_rated)

def getnorm():
    """retourne la la racine carrée de la somme des notes au carré """
    all_movies = pd.read_csv('./data/movies.csv', sep=',', header=0)
    all_rates =  pd.read_csv('./data/ratings.csv', sep=',', header=0)
    all_rates =  pd.merge(all_rates, all_movies, on='movieId', how='inner')


    # http://localhost:5000/my-movies