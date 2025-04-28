document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('account-settings-form');
    
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        
        const username = document.getElementById('username').value;
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;
        const confirmPassword = document.getElementById('confirm-password').value;

        let valid = true;

        // Clear previous error messages
        const errorMessages = document.querySelectorAll('.error-message');
        errorMessages.forEach(msg => msg.textContent = '');

        // Validate username
        if (username.trim() === '') {
            document.getElementById('username-error').textContent = 'Username is required.';
            valid = false;
        }

        // Validate email
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailPattern.test(email)) {
            document.getElementById('email-error').textContent = 'Please enter a valid email address.';
            valid = false;
        }

        // Validate password
        if (password.length < 6) {
            document.getElementById('password-error').textContent = 'Password must be at least 6 characters long.';
            valid = false;
        }

        // Validate confirm password
        if (password !== confirmPassword) {
            document.getElementById('confirm-password-error').textContent = 'Passwords do not match.';
            valid = false;
        }

        // If valid, submit the form
        if (valid) {
            form.submit();
        }
    });
});