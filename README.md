movie listing api 
## Features
- **User Registration and Authentication:** Users can register and log in. JWT tokens are used for authentication.
- **Movie Management:** Users can create, read, update, and delete movies. Movies have fields such as title, director, release year, genre, and description.
- **Comments:** Users can add comments to movies. Comments can be nested to create threads.
- **Ratings:** Users can rate movies (future feature, placeholder included).


project structure 
movie-listing-api/
├── app/                    # Main application directory
│   ├── models/             # Database models (User, Movie, Comment, etc.)
│   ├── routers/            # API routes (auth, movies, comments, etc.)
│   ├── schemas/            # Pydantic models for request/response validation
│   ├── utils/              # Utility functions (e.g., security-related utilities)
│   ├── main.py             # Entry point for the FastAPI app
├── alembic/                # Directory for Alembic migrations
├── tests/                  # Test cases for the application
├── myenv/                  # Virtual environment directory
├── alembic.ini             # Alembic configuration file
├── requirements.txt        # Python dependencies
└── README.md               # This readme file



## Installation

### Prerequisites
- Python 3.11
- PostgreSQL

### Setup

1. **Clone the repository:**
    ```sh
    git clone https://github.com/your-username/movie-listing-api.git
    cd movie-listing-api
    ```

2. **Create a virtual environment:**
    ```sh
    python3 -m venv myenv
    source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up the database:**
    - Create a PostgreSQL database and user.
    - Update `alembic.ini` with your database connection string.

5. **Run migrations to create the necessary tables:**
    ```sh
    alembic upgrade head
    ```

6. **Run the application:**
    ```sh
    uvicorn app.main:app --reload
    ```

## Usage

You can interact with the API using tools like `curl` or Postman.

### Example Curl Commands

- **Register a new user:**
    ```sh
    curl -X POST "http://127.0.0.1:8000/auth/register" \
    -H "Content-Type: application/json" \
    -d '{
      "username": "newuser",
      "email": "newuser@example.com",
      "password": "securepassword"
    }'
    ```

- **Login and get a token:**
    ```sh
    curl -X POST "http://127.0.0.1:8000/auth/login" \
    -H "Content-Type: application/json" \
    -d '{
      "email": "newuser@example.com",
      "password": "securepassword"
    }'
    ```

- **Add a movie:**
    ```sh
    curl -X POST "http://127.0.0.1:8000/movies/" \
    -H "Authorization: Bearer <your_token>" \
    -H "Content-Type: application/json" \
    -d '{
      "title": "The Matrix",
      "director": "The Wachowskis",
      "release_year": 1999,
      "genre": "Sci-Fi",
      "description": "A hacker discovers reality as an illusion."
    }'
    ```

## License


