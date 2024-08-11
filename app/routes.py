from flask import Flask, jsonify, request
from flask_cors import CORS
import praw
import re
import os
from dotenv import load_dotenv
from services.submission_service import SubmissionService

load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
user_agent = os.getenv('USER_AGENT')

@app.route('/submissions', methods=['GET'])
def get_all_submissions():
    try:
        submissions = SubmissionService.fetch_all_submissions()
        return jsonify(submissions)
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500

@app.route('/get_comments', methods=['POST'])
def get_comments():
    url = request.json.get('url')
    if not url:
        return jsonify({"error": "URL parameter is required"}), 400

    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent
    )

    try:
        match = re.search(r'/comments/([a-zA-Z0-9_]+)/', url)
        if match:
            submission_id = match.group(1)
        else:
            return jsonify({"error": "Invalid URL format"}), 400

        submission = reddit.submission(id=submission_id)
        title = submission.title  # Get the title of the post
        top_level_comments = [comment.body for comment in submission.comments if not isinstance(comment, praw.models.MoreComments)]

        SubmissionService.save_submission(submission_id, url, title)

        return jsonify({"title": title, "comments": top_level_comments})

    except praw.exceptions.RedditAPIException as e:
        print(f"Reddit API error: {str(e)}")
        return jsonify({"error": f"Reddit API error: {str(e)}"}), 500

    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
