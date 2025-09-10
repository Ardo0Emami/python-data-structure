# Accounting API

This project implements a backend service for a basic accounting domain using Python and FastAPI.  
It demonstrates clean architectural separation, modular design, and production-grade development practices.

---

## Technologies

- Python 3.11+
- FastAPI
- SQLAlchemy 2.0 (async engine)
- Pydantic
- SQLite (development) — easily switchable to PostgreSQL
- unittest
- Docker (optional)

---

## Project Structure

```text
accounting_api/
├── api/            # API route definitions
├── db/             # Database connection and session management
├── models/         # Pydantic schemas and SQLAlchemy models
├── services/       # Business logic layer
├── tests/          # Unit tests
├── config.py       # Environment and settings
├── main.py         # Application entry point
└── README.md
