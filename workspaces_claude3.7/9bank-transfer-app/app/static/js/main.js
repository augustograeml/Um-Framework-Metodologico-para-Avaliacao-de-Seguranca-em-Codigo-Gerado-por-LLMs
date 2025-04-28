document.addEventListener('DOMContentLoaded', function() {
    const transferForm = document.getElementById('transfer-form');

    transferForm.addEventListener('submit', function(event) {
        event.preventDefault();

        const userId = document.getElementById('user-id').value;
        const amount = parseFloat(document.getElementById('amount').value);

        if (isNaN(amount) || amount <= 0) {
            alert('Please enter a valid transfer amount.');
            return;
        }

        fetch('/transfer', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ userId, amount }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Transfer successful!');
                transferForm.reset();
            } else {
                alert('Transfer failed: ' + data.message);
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred while processing the transfer.');
        });
    });
});