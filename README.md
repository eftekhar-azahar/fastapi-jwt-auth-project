# FastAPI JWT Authentication Project

This is a **FastAPI application** that implements **JWT (JSON Web Token) authentication**, providing secure user login and API access. The project uses **Argon2** for password hashing and features modular, maintainable code structure.

## Project Structure

fastapi-jwt-auth-project/
│
├── product/
│ ├── routers/
│ │ ├── login.py # Handles user login and JWT generation
│ │ └── seller.py # Seller-related endpoints
│ ├── schemas.py # Pydantic models for request/response validation
│ ├── models.py # SQLAlchemy ORM models
│ └── main.py # FastAPI application entry point
│
├── README.md
├── requirements.txt
└── .gitignore

## Key Features

- JWT-based authentication with token expiration
- Secure password hashing using Argon2
- Login endpoint for token generation
- Modular project structure with FastAPI routers
- SQLAlchemy ORM for database interactions
- Interactive API documentation available at `/docs`

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/eftekhar-azahar/fastapi-jwt-auth-project.git
cd fastapi-jwt-auth-project
Create and activate a virtual environment:
python -m venv env
.\env\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Running the Application
uvicorn product.main:app --reload
Access the interactive Swagger UI at: http://127.0.0.1:8000/docs

Usage

Use the /login endpoint to obtain a JWT access token.

Include the token in the Authorization header to access protected endpoints.

The JWT token expires after 20 minutes (configurable in login.py).

Requirements

Python 3.10+

FastAPI

SQLAlchemy

Passlib (Argon2)

Python-JOSE (JWT)

License

This project is open-source and free to use.
