# FizzBuzz Backend
This project implements a FizzBuzz API in Python.
## Prerequisites
*   Docker
*   Docker Compose
## Installation and Launch with Docker
This project is configured to run easily with Docker.
### Start the application
To build and start the container:
```
docker compose build
docker compose up
```
To run the tests inside the container:
```pytest tests/```
The application will be accessible at `http://localhost:8000`.
### Stop the application
To stop the containers:
```docker compose down```

## Project Structure
*   `fizz_buzz/`: Application source code.
*   `tests/`: Unit and integration tests.
*   `Dockerfile`: Configuration for building the Docker image.
*   `docker-compose.yml`: Configuration for container orchestration.
