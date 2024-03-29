document.querySelectorAll('.reply-btn').forEach(button => {
    button.addEventListener('click', () => {
        const commentId = button.getAttribute("comment-id");
        const replyForm = document.getElementById(`reply-form-${commentId}`);
        if (replyForm.classList.contains("d-none")) {
            replyForm.classList.remove("d-none");
        } else {
            replyForm.classList.add("d-none");
        }
        i = 0
        while (document.getElementById(`reply-form-${i}`) != null) {
            if (i == commentId) {
                i++;
                continue;
            }
            document.getElementById(`reply-form-${i}`).classList.add("d-none");
            i++;
        }
    });
});