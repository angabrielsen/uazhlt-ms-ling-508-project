class Submission:
    def __init__(self, id, submission_id, url):
        self.id = id
        self.submission_id = submission_id
        self.url = url

    def __str__(self):
        return f'Submission ID: {self.submission_id}, URL: "{self.url}", ID: {self.id}'
