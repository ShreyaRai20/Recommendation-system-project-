document.getElementById('recommend_button').addEventListener('click', function(event) {
    event.preventDefault(); // Prevent default form submission
    var movieName = document.getElementById('movie_name').value;

    fetch('/recommendations', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ movie_name: movieName }),
    })
    .then(response => response.json())
        .then(data => {
        // Update HTML content to display recommended movies
        var recommendedMovies = data.recommended_movies;
        var recommendedMoviesHtml = '<h2>Recommended Movies</h2><ul>';
        recommendedMovies.forEach(movie => {
        recommendedMoviesHtml += '<li>' + movie + '</li>';
});
recommendedMoviesHtml += '</ul>';
document.getElementById('recommended_movies').innerHTML = recommendedMoviesHtml;
})
.catch(error => {
    console.error('Error:', error);
});
});

