# 🎓 Student Management REST API

A complete **Student Management System** built with **Flask**, **SQLAlchemy**, **SQLite**, and a **Bootstrap + JavaScript frontend**. This project demonstrates the implementation of RESTful APIs and CRUD (Create, Read, Update, Delete) operations with a responsive web interface.

---

# 📌 Project Overview

The Student Management REST API allows users to manage student records through a RESTful backend and an interactive frontend. Users can add, view, update, and delete student information stored in a SQLite database.

This project follows the REST architecture and uses Flask Blueprints for better project organization.

---

# 🚀 Features

- Add a new student
- View all students
- View a single student by ID
- Update student information
- Delete a student
- SQLite database integration
- SQLAlchemy ORM
- REST API implementation
- Responsive Bootstrap UI
- JavaScript Fetch API integration
- CORS enabled
- Clean project architecture

---

# 🛠 Technologies Used

### Backend

- Python 3.x
- Flask
- Flask SQLAlchemy
- Flask CORS
- SQLite

### Frontend

- HTML5
- CSS3
- Bootstrap 5
- JavaScript (ES6)
- Fetch API

### Tools

- Visual Studio Code
- Postman
- Git & GitHub

---

# 📁 Project Structure

```text
student-management-api/
│
├── app.py
├── config.py
├── models.py
├── requirements.txt
├── students.db
│
├── routes/
│   └── student_routes.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│

│
└── README.md
```

---

# ⚙️ Installation

## 1 Clone Repository

```bash
git clone https://github.com/your-username/student-management-api.git
```

---

## 2 Navigate to Project

```bash
cd student-management-api
```

---

## 3 Create Virtual Environment

Windows

```bash
python -m venv myenv
```

---

## 4 Activate Virtual Environment

Windows PowerShell

```bash
myenv\Scripts\activate
```

Command Prompt

```bash
myenv\Scripts\activate.bat
```

---

## 5 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 6 Run Application

```bash
python app.py
```

The application will start on

```
http://127.0.0.1:5000
```

---

# 📚 API Endpoints

## Get All Students

```
GET /students
```

Response

```json
[
  {
    "id": 1,
    "name": "Ali",
    "age": 22,
    "email": "ali@gmail.com",
    "course": "Computer Science"
  }
]
```

Status Code

```
200 OK
```

---

## Get Student By ID

```
GET /students/<id>
```

Example

```
GET /students/1
```

Status Code

```
200 OK
```

or

```
404 Not Found
```

---

## Add Student

```
POST /students
```

Request Body

```json
{
    "name":"Ali",
    "age":22,
    "email":"ali@gmail.com",
    "course":"Computer Science"
}
```

Status Code

```
201 Created
```

---

## Update Student

```
PUT /students/<id>
```

Example

```
PUT /students/1
```

Request Body

```json
{
    "name":"Ali Ahmad",
    "age":23,
    "email":"ali@gmail.com",
    "course":"Software Engineering"
}
```

Status Code

```
200 OK
```

---

## Delete Student

```
DELETE /students/<id>
```

Example

```
DELETE /students/1
```

Status Code

```
200 OK
```

---

# 💾 Database

Database Used

```
SQLite
```

Table

```
students
```

Columns

| Column | Type |
|---------|------|
| id | Integer |
| name | String |
| age | Integer |
| email | String |
| course | String |

---

# 🎨 Frontend Features

- Responsive Dashboard
- Student Registration Form
- Student Records Table
- Add Student
- Update Student
- Delete Student
- Bootstrap Design
- JavaScript Fetch API

---

# 🔄 CRUD Operations

| Operation | HTTP Method |
|-----------|-------------|
| Create Student | POST |
| Read Students | GET |
| Update Student | PUT |
| Delete Student | DELETE |

---


# 📦 Requirements

```text
Flask
Flask-SQLAlchemy
Flask-CORS
SQLAlchemy
```

Install using

```bash
pip install -r requirements.txt
```

---

# 👨‍💻 Author

**Name:** Fakhar Alam

**Project:** Student Management REST API

**Technology Stack:** Flask, SQLAlchemy, SQLite, Bootstrap, JavaScript

---

# 📄 License

This project is developed for educational purposes and can be modified or extended for learning and academic use.

---

# ⭐ Learning Outcomes

After completing this project, you will understand:

- REST API Development
- Flask Application Structure
- SQLAlchemy ORM
- SQLite Database
- CRUD Operations
- HTTP Methods
- HTTP Status Codes
- Blueprint Architecture
- JavaScript Fetch API
- Frontend and Backend Integration
- Bootstrap Responsive Design

---

# 🎯 Future Improvements

- User Authentication (JWT)
- Login & Registration
- Search Students
- Pagination
- Sorting
- File Upload
- Export to PDF
- Export to Excel
- Dashboard Analytics
- Role-Based Access Control
- Docker Support
- Deployment on Render or Railway
- MySQL/PostgreSQL Support

---