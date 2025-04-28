document.addEventListener('DOMContentLoaded', function() {
    const searchForm = document.getElementById('search-form');
    const resultsContainer = document.getElementById('results-container');

    searchForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const searchTerm = document.getElementById('search-term').value;

        fetch(`/search?term=${encodeURIComponent(searchTerm)}`)
            .then(response => response.json())
            .then(data => {
                resultsContainer.innerHTML = '';
                if (data.results.length > 0) {
                    data.results.forEach(result => {
                        const resultItem = document.createElement('div');
                        resultItem.className = 'result-item';
                        resultItem.textContent = result;
                        resultsContainer.appendChild(resultItem);
                    });
                } else {
                    resultsContainer.textContent = 'No results found.';
                }
            })
            .catch(error => {
                console.error('Error fetching search results:', error);
                resultsContainer.textContent = 'An error occurred while searching.';
            });
    });
});