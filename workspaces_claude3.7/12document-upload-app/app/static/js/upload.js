document.addEventListener('DOMContentLoaded', function() {
    const uploadForm = document.getElementById('uploadForm');
    const fileInput = document.getElementById('fileInput');
    const messageDiv = document.getElementById('message');

    uploadForm.addEventListener('submit', function(event) {
        event.preventDefault();

        const file = fileInput.files[0];
        if (!file) {
            messageDiv.textContent = 'Please select a file to upload.';
            return;
        }

        const formData = new FormData();
        formData.append('file', file);

        fetch('/upload', {
            method: 'POST',
            body: formData
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('File upload failed.');
            }
            return response.json();
        })
        .then(data => {
            messageDiv.textContent = 'File uploaded successfully: ' + data.filename;
        })
        .catch(error => {
            messageDiv.textContent = error.message;
        });
    });
});