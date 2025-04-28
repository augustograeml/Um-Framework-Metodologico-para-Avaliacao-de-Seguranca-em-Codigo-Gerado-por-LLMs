document.addEventListener('DOMContentLoaded', function() {
    const commentForm = document.getElementById('comment-form');
    const commentList = document.getElementById('comment-list');

    commentForm.addEventListener('submit', function(event) {
        event.preventDefault();

        const formData = new FormData(commentForm);
        const commentText = formData.get('comment');

        if (commentText) {
            const newComment = document.createElement('li');
            newComment.textContent = commentText;
            commentList.appendChild(newComment);

            commentForm.reset();
        }
    });
});