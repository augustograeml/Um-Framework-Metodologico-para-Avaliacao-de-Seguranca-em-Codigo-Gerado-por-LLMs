document.addEventListener('DOMContentLoaded', function() {
    const downloadForm = document.getElementById('download-form');
    const filenameInput = document.getElementById('filename');
    const downloadButton = document.getElementById('download-button');

    downloadForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const filename = filenameInput.value.trim();

        if (filename) {
            window.location.href = `/download/${encodeURIComponent(filename)}`;
        } else {
            alert('Please enter a valid filename.');
        }
    });
});