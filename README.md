# HRMS Backend API

Human Resource Management System (HRMS) Backend API built using FastAPI, PostgreSQL, SQLAlchemy, JWT Authentication, and Alembic.

---

# Features

- User Authentication (Register/Login)
- JWT Access Token Authentication
- Refresh Token Authentication
- Role-Based Access Control (RBAC)
- Employee Management
- Attendance Management
- Payroll Management
- PostgreSQL Database
- SQLAlchemy ORM
- Alembic Database Migration
- Swagger API Documentation

---

# Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- JWT Authentication
- Passlib (Password Hashing)

---

# Project Structure

```text
hrms_backend/
│
├── alembic/
├── app/
│   ├── auth/
│   ├── models/
│   ├── routes/
│   ├── schemas/
│   ├── utils/
│   ├── config.py
│   ├── database.py
│   ├── dependencies.py
│   └── main.py
│
├── .env
├── .gitignore
├── alembic.ini
├── requirements.txt
└── README.md