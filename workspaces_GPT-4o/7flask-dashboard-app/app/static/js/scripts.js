document.addEventListener('DOMContentLoaded', function() {
    const settingsForm = document.getElementById('settings-form');

    if (settingsForm) {
        settingsForm.addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent the default form submission

            // Perform client-side validation here if needed

            const formData = new FormData(settingsForm);

            fetch(settingsForm.action, {
                method: 'POST',
                body: formData,
            })
            .then(response => response.json())
            .then(data => {
                // Handle success or error response
                if (data.success) {
                    alert('Settings updated successfully!');
                } else {
                    alert('Error updating settings: ' + data.message);
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('An error occurred while updating settings.');
            });
        });
    }
});