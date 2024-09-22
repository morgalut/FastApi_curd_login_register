Here’s the updated README with the provided Git clone link:


# FastAPI Task Management Project

## Purpose

The FastAPI Task Management Project is a web application designed to help users manage their tasks efficiently. It provides a RESTful API for task creation, updating, deletion, and retrieval, as well as user registration and authentication. The application leverages FastAPI's asynchronous capabilities, SQLAlchemy for database interactions, and Pydantic for data validation, ensuring a fast and reliable experience.

## Features

- User registration and authentication
- Create, read, update, and delete tasks
- Input validation using Pydantic
- Support for task priority and status using Enums
- Database management with SQLAlchemy

## Installation

To set up this project locally, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/morgalut/FastApi_curd_login_register.git
   cd FastApi_curd_login_register
   ```

2. **Create a Virtual Environment:**
   ```bash
   python -m venv env
   ```

   - **On Windows:**
     ```cmd
     env\Scripts\activate
     ```

   - **On macOS/Linux:**
     ```bash
     source env/bin/activate
     ```

3. **Install Required Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database:**
   - If using SQLite, no additional setup is required.
   - For other databases, configure your database connection in the `app/database.py` file.

5. **Run the Application:**
   ```bash
   uvicorn app.main:app --reload
   ```

