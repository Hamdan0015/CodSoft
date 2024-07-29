document.getElementById('get-recommendations').addEventListener('click', getRecommendations);

function getRecommendations() {
    var bookTitle = document.getElementById('book-title').value;
    fetch(`/recommend?book_title=${bookTitle}`)
       .then(response => response.json())
       .then(recommendations => {
            var list = document.getElementById('recommendations');
            list.innerHTML = '';
            recommendations.forEach(recommendation => {
                var item = document.createElement('li');
                var img = document.createElement('img');
                img.src = recommendation[2];
                img.alt = recommendation[0];
                img.onerror = function() {
                    this.onerror = null;
                    this.src = '/static/images/placeholder.jpg';
                };
                item.appendChild(img);
                item.appendChild(document.createTextNode(`${recommendation[0]} by ${recommendation[1]}`));
                list.appendChild(item);
            });
        })
       .catch(error => console.error(error));
}
