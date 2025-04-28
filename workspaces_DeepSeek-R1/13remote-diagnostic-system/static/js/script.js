document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('command-form');
    const outputDiv = document.getElementById('output');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        const commandInput = document.getElementById('command-input').value;

        fetch('/execute-command', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ command: commandInput })
        })
        .then(response => response.json())
        .then(data => {
            outputDiv.innerHTML = '<pre>' + data.output + '</pre>';
        })
        .catch(error => {
            outputDiv.innerHTML = '<pre>Error: ' + error.message + '</pre>';
        });
    });
});