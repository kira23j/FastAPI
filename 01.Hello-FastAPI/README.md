# Hello FastAPI Project

This is a minimal FastAPI application that responds with a "Hello FastAPI!" message.

## Usage

1. Install FastAPI:

    ```bash
    pip install "fastapi[all]"
    ```

2. Run the application:

    ```bash
    uvicorn main:app --reload
    ```

3. Access the API at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

Explore the API documentation at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

## Endpoint

- **GET /:** Returns a JSON response with the message "Hello FastAPI!"
