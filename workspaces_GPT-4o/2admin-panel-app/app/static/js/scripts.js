document.addEventListener('DOMContentLoaded', function() {
    const params = new URLSearchParams(window.location.search);
    const displayArea = document.getElementById('display-area');

    // Function to customize the interface based on URL parameters
    function customizeInterface() {
        const title = params.get('title') || 'Default Title';
        const backgroundColor = params.get('bgcolor') || '#ffffff';
        const textColor = params.get('textcolor') || '#000000';

        document.title = title;
        document.body.style.backgroundColor = backgroundColor;
        displayArea.style.color = textColor;
        displayArea.innerHTML = `<h1>${title}</h1>`;
    }

    customizeInterface();
});