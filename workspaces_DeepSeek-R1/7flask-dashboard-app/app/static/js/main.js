document.addEventListener('DOMContentLoaded', function() {
    const accountSettingsForm = document.getElementById('account-settings-form');

    if (accountSettingsForm) {
        accountSettingsForm.addEventListener('submit', function(event) {
            event.preventDefault();

            const formData = new FormData(accountSettingsForm);

            fetch(accountSettingsForm.action, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-Requested-With': 'XMLHttpRequest'
                }
            })
            .then(response => response.json())
            .then(data => {
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