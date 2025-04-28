document.addEventListener('DOMContentLoaded', function() {
    const commentForm = document.getElementById('comment-form');
    const commentList = document.getElementById('comment-list');

    commentForm.addEventListener('submit', function(event) {
        event.preventDefault();

        const formData = new FormData(commentForm);
        const commentData = {
            name: formData.get('name'),
            content: formData.get('content')
        };

        fetch('/comments', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrf_token')
            },
            body: JSON.stringify(commentData)
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                const newComment = document.createElement('div');
                newComment.classList.add('comment');
                newComment.innerHTML = `<strong>${data.comment.name}</strong>: ${data.comment.content}`;
                commentList.appendChild(newComment);
                commentForm.reset();
            } else {
                alert('Error posting comment: ' + data.error);
            }
        })
        .catch(error => {
            console.error('Error:', error);
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