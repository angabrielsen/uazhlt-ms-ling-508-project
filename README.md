# UAZHLT MS-LING-508 Project

## Overview

This project is a Flask application that interacts with Reddit's API to fetch and save submissions and comments. It uses SQLAlchemy for ORM and integrates with Docker for containerized development.

## Features

- Fetch and display Reddit submissions.
- Retrieve and save comments from Reddit submissions.
- API endpoints for accessing submissions and comments.

## Getting Started

### Prerequisites

1. **Docker and Docker Compose**: Ensure you have Docker and Docker Compose installed. You can download Docker Desktop from [Docker's website](https://www.docker.com/products/docker-desktop).

### Setup and Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/angabrielsen/uazhlt-ms-ling-508-project.git
    cd uazhlt-ms-ling-508-project
    ```

 2. **Environment Variables**: Create a `.env` file in the root directory with the following content:
   This file is provided on the assignment submission.
    ```env
    CLIENT_ID=your_reddit_client_id
    CLIENT_SECRET=your_reddit_client_secret
    USER_AGENT=your_user_agent
    ```

3. **Build and Start the Containers**

    ```bash
    docker compose up -d --build
    ```

4. **Start the Flask Application**

    ```bash
    flask run
    ```

## Usage

1. **Fetch Submissions**

    - **Endpoint:** `GET /submissions`
    - **Command:**

        ```bash
        curl -X GET http://localhost:5000/submissions
        ```

2. **Fetch Comments**

    - **Endpoint:** `POST /get_comments`
    - **Request Body:** 

        ```json
        {
          "url": "https://www.reddit.com/r/Music/comments/17a2a6l/whats_a_song_that_makes_you_misty_eyed/"
        }
        ```

    - **Description:** Submit a URL from Reddit (e.g., a URL from `/r/music`) to retrieve comments for that post.

    - **Example URL:** 

   ```url
       https://www.reddit.com/r/Music/comments/17a2a6l/whats_a_song_that_makes_you_misty_eyed/
       https://www.reddit.com/r/Music/comments/18bqzgy/what_song_did_you_discover_from_a_sample_that/
       https://www.reddit.com/r/Music/comments/1dd5a4e/what_song_did_you_love_only_to_realize_at_a_later/
    ```

## Contributing

Contributions are welcome! Please submit a PR!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please reach out to [Ashton Gabrielsen](mailto:ashtongabrielsen@arizona.edu).
