# Python Backend Portfolio

Welcome to my backend engineering portfolio.

This repository showcases a transition from 12 years of Delphi/SQL development to a modern Python backend stack — emphasizing production-quality code, robust structure, and best practices in modern Python engineering.

---

## Project Structure

| Folder | Description |
|--------|-------------|
| `data_structure/` | Clean implementations of core data structures (stack, queue, linked list, etc.) with full unit tests |
| `accounting_api/` | Realistic accounting API using FastAPI + SQLAlchemy + Pydantic + Docker |
| `common/` | Shared modules used across subprojects (e.g., config, db, utils) |
| `docs/` | Word/PDF files, design notes, API diagrams, and planning artifacts |

---

## Technologies Used

- Python 3.11+
- FastAPI, Pydantic, SQLAlchemy 2.0
- `unittest` + `pytest`
- `flake8`, `mypy`
- `Docker`, `.env`, `BackgroundTasks`, AsyncIO

---

## Highlights

- Type-safe, modular Python codebase
- Object-oriented design with clean separation of concerns
- REST API with CRUD, background tasks, and error handling
- Fully tested and linted with clear structure
- Designed for real-world extensibility and maintainability

---

## Run All Tests

```bash
python3 -m unittest discover -s data_structure -p 'test_*.py'
python3 -m unittest discover -s accounting_api/tests
```

---

## Next Up

- Add authentication and user model to accounting API
- Expand `common/` utilities (validation, helpers, error mappers)
- Create a small async-based service to compare threading and asyncio
- Polish README files and add architecture diagrams
- Final refactors and documentation pass

---

## Connect

- GitHub: [github.com/Ardo0Emami](https://github.com/Ardo0Emami)
- Email: [it.arghavanemami@gmail.com]
- Website: [myportfolio.com]
