Here’s the updated README with separate sections for Linux and Windows formats for the cURL commands:


# FastAPI Project

This project is a FastAPI application that provides a RESTful API for managing tasks and user authentication. It utilizes SQLAlchemy for database interactions and Pydantic for data validation.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Models](#models)
- [License](#license)

## Features

- User registration and authentication
- Task management (create, update, delete, retrieve)
- Input validation using Pydantic
- Enum usage for task status and priority
- Database interactions using SQLAlchemy

## Installation

To set up this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/morgalut/FastApi_curd_login_register.git
   cd FastApi_curd_login_register
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database (if using SQLite, no additional setup is required).

5. Start the FastAPI application:
   ```bash
   uvicorn app.main:app --reload
   ```

## Usage

You can interact with the API using a tool like [Postman](https://www.postman.com/) or [cURL](https://curl.se/).

### API Endpoints

#### Task Management

- **Add a Task**

  **Linux:**
  ```bash
  curl -X POST \
    "http://127.0.0.1:8000/tasks" \
    -H "Content-Type: application/json" \
    -d "{\"title\": \"New Task\", \"description\": \"This is a new task.\", \"priority\": \"medium\"}"
  ```

  **Windows CMD:**
  ```cmd
  curl -X POST ^
    "http://127.0.0.1:8000/tasks" ^
    -H "Content-Type: application/json" ^
    -d "{\"title\": \"New Task\", \"description\": \"This is a new task.\", \"priority\": \"medium\"}"
  ```

- **Get All Tasks**

  **Linux:**
  ```bash
  curl -X GET "http://127.0.0.1:8000/tasks" -H "accept: application/json"
  ```

  **Windows CMD:**
  ```cmd
  curl -X GET "http://127.0.0.1:8000/tasks" -H "accept: application/json"
  ```

- **Update Task Status**

  **Linux:**
  ```bash
  curl -X PATCH "http://127.0.0.1:8000/tasks/1/status?status=completed" -H "accept: application/json"
  ```

  **Windows CMD:**
  ```cmd
  curl -X PATCH "http://127.0.0.1:8000/tasks/1/status?status=completed" -H "accept: application/json"
  ```

#### User Authentication

- **Register a User**

  **Linux:**
  ```bash
  curl -X POST "http://127.0.0.1:8000/auth/register" \
    -H "Content-Type: application/json" \
    -d "{\"username\": \"mor\", \"email\": \"mor@example.com\", \"password\": \"password123\"}"
  ```

  **Windows CMD:**
  ```cmd
  curl -X POST "http://127.0.0.1:8000/auth/register" ^
    -H "Content-Type: application/json" ^
    -d "{\"username\": \"mor\", \"email\": \"mor@example.com\", \"password\": \"password123\"}"
  ```

- **Login User**

  **Linux:**
  ```bash
  curl -X POST "http://127.0.0.1:8000/auth/login" \
    -H "Content-Type: application/json" \
    -d "{\"username\": \"mor\", \"password\": \"password123\"}"
  ```

  **Windows CMD:**
  ```cmd
  curl -X POST "http://127.0.0.1:8000/auth/login" ^
    -H "Content-Type: application/json" ^
    -d "{\"username\": \"mor\", \"password\": \"password123\"}"
  ```

## Models

### User Model

- `id`: int (primary key)
- `username`: str (unique)
- `email`: str (unique)
- `hashed_password`: str

### Task Model

- `id`: int (primary key)
- `title`: str
- `description`: str
- `status`: Enum (e.g., PENDING, COMPLETED)
- `priority`: Enum (e.g., LOW, MEDIUM, HIGH)

