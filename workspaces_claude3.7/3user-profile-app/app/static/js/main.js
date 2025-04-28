document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('profile-form');
    
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        
        const name = document.getElementById('name').value;
        const bio = document.getElementById('bio').value;

        fetch('/update-profile', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ name: name, bio: bio })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Profile updated successfully!');
                window.location.reload();
            } else {
                alert('Error updating profile: ' + data.message);
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred while updating the profile.');
        });
    });
});