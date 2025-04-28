document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('file-form');
    const fileInput = document.getElementById('file-name');
    const resultDiv = document.getElementById('result');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        const fileName = fileInput.value;

        fetch(`/get-file/${fileName}`)
            .then(response => {
                if (!response.ok) {
                    throw new Error('File not found');
                }
                return response.text();
            })
            .then(data => {
                resultDiv.textContent = data;
            })
            .catch(error => {
                resultDiv.textContent = error.message;
            });
    });
});