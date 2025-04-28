document.addEventListener('DOMContentLoaded', function() {
    const emailForm = document.getElementById('email-form');
    const emailInput = document.getElementById('email-input');
    const messageDiv = document.getElementById('message');

    emailForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const newEmail = emailInput.value;

        fetch('/profile/update_email', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrf_token') // Assuming CSRF protection is in place
            },
            body: JSON.stringify({ email: newEmail })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                messageDiv.textContent = 'Email updated successfully!';
                messageDiv.style.color = 'green';
            } else {
                messageDiv.textContent = 'Error updating email: ' + data.error;
                messageDiv.style.color = 'red';
            }
        })
        .catch(error => {
            messageDiv.textContent = 'An error occurred: ' + error;
            messageDiv.style.color = 'red';
        });
    });

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Check if this cookie string begins with the desired name
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});