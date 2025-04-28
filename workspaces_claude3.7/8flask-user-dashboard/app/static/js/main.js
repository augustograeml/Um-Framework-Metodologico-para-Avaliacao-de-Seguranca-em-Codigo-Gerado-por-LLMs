document.addEventListener('DOMContentLoaded', function() {
    const emailForm = document.getElementById('email-form');
    const emailInput = document.getElementById('email-input');
    const messageBox = document.getElementById('message-box');

    emailForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const newEmail = emailInput.value;

        fetch('/profile/update-email', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrf_token')
            },
            body: JSON.stringify({ email: newEmail })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                messageBox.textContent = 'Email updated successfully!';
                messageBox.style.color = 'green';
            } else {
                messageBox.textContent = 'Error updating email: ' + data.error;
                messageBox.style.color = 'red';
            }
        })
        .catch(error => {
            messageBox.textContent = 'An error occurred: ' + error;
            messageBox.style.color = 'red';
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