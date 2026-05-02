# Flask Todo Application

A modern, fast, and feature-complete Todo application built with Python Flask.

## Features

- **Backend**: Python Flask with a file-based SQLite database (`todo.db`).
- **Authentication**: Full session-based user authentication (Register, Login, Logout).
- **CRUD Operations**: Add tasks, mark them as complete, and delete them.
- **Modern UI**: Clean, responsive dark-themed UI built with pure Vanilla CSS (no external frameworks).
- **Automated Testing**: 15 comprehensive Selenium E2E tests built with `pytest`.
- **Containerization**: Separate Dockerfiles for the application and the test suite.
- **CI/CD**: Ready-to-use Jenkinsfile for automated testing and deployments.

## Getting Started

### 1. Run Locally (Native Python)

Make sure you have Python 3.11+ installed.

```bash
# Install dependencies
pip install -r requirements.txt

# Start the Flask app
python app.py
```
*The app will be available at `http://localhost:5000`.*

### 2. Run the Test Suite

The project includes 15 automated end-to-end tests using Selenium and a headless Chrome browser. 

Make sure your Flask app is running locally, then in a new terminal window:

```bash
# Run pytest on the tests directory
pytest tests/
```

### 3. Run with Docker

You can run the application entirely within Docker without installing Python locally.

```bash
# Build the Docker image
docker build -t flask-todo-app .

# Run the container
docker run -p 5000:5000 flask-todo-app
```

## Continuous Integration (Jenkins)

This project includes a `Jenkinsfile` configured to:
1. Clone the repository.
2. Build and start the Flask app in a Docker container.
3. Build a specialized testing container (`Dockerfile.test`) that includes Chrome and ChromeDriver.
4. Execute the Selenium test suite against the running app.
5. Tear down containers and send an email notification with the build results.

**Setup**:
Just point a new Jenkins Pipeline job to this repository, and it will handle the rest automatically.
