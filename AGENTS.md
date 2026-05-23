# Repository Guidelines

## Project Structure & Module Organization

This repository currently contains a small FastAPI application and supporting project notes.

- `main.py`: FastAPI entry point, route definitions, and Pydantic request models.
- `projects/`: planning documents for API ideas, including Kenyan market project concepts in Markdown and text formats.
- `api-design.pdf`: design reference material.
- `__pycache__/` and `.playwright-mcp/`: generated/local tooling artifacts; do not treat these as source files.

As the API grows, prefer splitting `main.py` into focused modules such as `app/routes/`, `app/models/`, and `app/services/`, with tests under `tests/`.

## Build, Test, and Development Commands

Install runtime dependencies in a virtual environment before running the app:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install fastapi uvicorn
```

Run the API locally:

```powershell
python main.py
```

Alternative development server command:

```powershell
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Open `http://localhost:8000/docs` for the interactive OpenAPI documentation and `http://localhost:8000/health` for a basic health check.

## Coding Style & Naming Conventions

Use Python 3 style with 4-space indentation. Keep route functions short, typed, and named by action, for example `create_item` or `read_item`. Use `PascalCase` for Pydantic models such as `Item`, and `snake_case` for variables, functions, and module names.

Prefer single-purpose request/response models over untyped dictionaries when adding new endpoints. Keep API paths lowercase and resource-oriented, such as `/items/{item_id}`.

## Testing Guidelines

No test suite is currently present. When adding tests, use `pytest` and FastAPI's `TestClient`. Place tests in `tests/` and name files `test_*.py`.

Example future command:

```powershell
pytest
```

Cover health checks, validation errors, and each new route's successful and failure paths.

## Commit & Pull Request Guidelines

This repository has no commit history yet. Use concise, imperative commit messages, for example `Add health endpoint` or `Document API project ideas`.

Pull requests should include a short summary, testing notes, and any relevant API behavior changes. Link issues when available. Include screenshots only when changing generated docs, UI-facing behavior, or visual assets.

## Security & Configuration Tips

Do not commit secrets, API keys, local virtual environments, or generated cache files. If environment-specific settings are added later, load them from environment variables and document required values in a sample `.env.example`.
