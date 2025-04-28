document.addEventListener('DOMContentLoaded', function() {
    const searchForm = document.getElementById('search-form');
    const searchInput = document.getElementById('search-input');
    const resultsContainer = document.getElementById('results-container');

    searchForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const searchTerm = searchInput.value.trim();

        if (searchTerm) {
            fetch(`/search?term=${encodeURIComponent(searchTerm)}`)
                .then(response => response.json())
                .then(data => {
                    displayResults(data);
                })
                .catch(error => {
                    console.error('Error fetching search results:', error);
                });
        }
    });

    function displayResults(data) {
        resultsContainer.innerHTML = '';

        if (data.length === 0) {
            resultsContainer.innerHTML = '<p>No results found.</p>';
            return;
        }

        const ul = document.createElement('ul');
        data.forEach(entry => {
            const li = document.createElement('li');
            li.textContent = `${entry.timestamp} [${entry.level}] ${entry.message}`;
            ul.appendChild(li);
        });

        resultsContainer.appendChild(ul);
    }
});