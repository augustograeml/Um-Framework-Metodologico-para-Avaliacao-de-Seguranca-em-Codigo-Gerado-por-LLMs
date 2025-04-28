document.addEventListener('DOMContentLoaded', function() {
    const commandForm = document.getElementById('command-form');
    const commandInput = document.getElementById('command-input');
    const outputArea = document.getElementById('output-area');

    commandForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const command = commandInput.value;

        fetch('/api/execute', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({ command: command })
        })
        .then(response => response.json())
        .then(data => {
            outputArea.textContent = data.output;
        })
        .catch(error => {
            outputArea.textContent = 'Error: ' + error.message;
        });
    });

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});