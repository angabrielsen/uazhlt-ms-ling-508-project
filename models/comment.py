class Comment:
    def __init__(self, submission_id, comment_text):
        self.submission_id = submission_id
        self.comment_text = comment_text

    def __str__(self):
        return f"Comment(submission_id={self.submission_id}, comment_text={self.comment_text})"
