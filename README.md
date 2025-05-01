# API Test Automation: GoREST /users Endpoint

This project automates RESTful API testing using Python and pytest for the [GoREST API](https://gorest.co.in/). It focuses on the /users endpoint and demonstrates automated validation of various HTTP methods.

---

## Requirements

- Python 3.10
- pip (Python package manager)
- A personal access token from [https://gorest.co.in/](https://gorest.co.in/)

---

## Setup Instructions

-  Clone and Set Up the Project
   ```bash
   git clone https://github.com/walidaud/yassir_assessment_part1.git
   cd yassir_assessment_part1

   # Create and activate a virtual environment
   python -m venv venv
   venv\Scripts\activate

   # Install dependencies
   pip install -r requirements.txt

   # Set your GoREST access token in config.py

   # Run the tests
   PYTHONPATH=. pytest --maxfail=2 --disable-warnings