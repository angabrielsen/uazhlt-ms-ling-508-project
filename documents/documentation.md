# Welcome to /r/music Maker!

This app allows a user to submit a url from [/r/music](https://www.reddit.com/r/music) and receive a link to all the top comments from that post. As work progresses, the app will parse those comments to retrieve a search query to submit to Spotify's API and will return a playlist made from those songs.

# API Endpoints

There are three API endpoints to help achieve the goals of the app:

## Get All Submissions

- URL: `/submission`
- Method: `GET`
- Description: Gets all submissions from the db

## Get Comments from Reddit

- URL: `/get_comments`
- Method: `POST`
- Description: Given a Reddit URL, uses the praw library to get all top level comments

## Get Comments by Submission ID

- URL: `get_comments/<submission_id>`
- Method: `GET`
- Description: Fetches comments for a given `submission_id` from the db