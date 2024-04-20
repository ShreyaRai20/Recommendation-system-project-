from flask import Flask, render_template, request
from RecommendationSystem import get_recommendations


app = Flask(__name__)
app.static_folder ='static'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommendations', methods=['POST'])
def recommendations():
    movie_name = request.form['movie_name']
    recommended_movies = get_recommendations(movie_name.title())
    return render_template('index.html', movies=recommended_movies)

if __name__ == '__main__':
    app.run(debug=True)
