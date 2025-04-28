document.addEventListener('DOMContentLoaded', function() {
    const emailUpdateForm = document.getElementById('email-update-form');
    
    if (emailUpdateForm) {
        emailUpdateForm.addEventListener('submit', function(event) {
            event.preventDefault();
            const emailInput = document.getElementById('email-input').value;

            fetch('/update-email', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrf_token')
                },
                body: JSON.stringify({ email: emailInput })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert('Email updated successfully!');
                } else {
                    alert('Error updating email: ' + data.message);
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    }

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