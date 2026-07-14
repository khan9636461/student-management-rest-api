import os

# Get the absolute path of the project directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    # SQLite Database Configuration
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "students.db")

    # Disable modification tracking to improve performance
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Secret key for Flask sessions and security
    SECRET_KEY = "student_management_secret_key"