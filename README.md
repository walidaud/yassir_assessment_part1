# README.md

# GoREST API Automation

Automated tests for GoREST's RESTful API using Python, Pytest, and GitHub Actions.

## Features
- Authenticated API testing
- Modular and scalable test structure
- GitHub Actions integration for CI

## Setup
```bash
pip install -r requirements.txt
```

Add your GoREST token to `utils/config.py`:
```python
ACCESS_TOKEN = "your_token_here"
```

## Running Tests
```bash
pytest
```