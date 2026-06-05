# Phase 4 — API Automation Framework

Automated API test suite built with Python, pytest, and the requests
library. Tests a public REST API across multiple endpoints with schema
validation, data-driven parametrization, and request chaining.

## What This Project Covers
- REST API testing: GET, POST, PUT, PATCH, DELETE
- Status code and response body assertions
- JSON schema validation with jsonschema
- Request chaining — using one response to build the next request
- Shared fixtures via conftest.py (requests.Session, base URL)
- Data-driven tests with external JSON test data
- HTML test reporting with pytest-html

## Tech Stack
- Python 3.x
- requests
- pytest
- jsonschema
- pytest-html

## Project Structure
```text
phase4-api/
├── conftest.py              # Shared session and URL fixtures
├── pytest.ini               # pytest config and HTML report settings
├── schemas.py               # Reusable JSON schema definitions
├── test_data.json           # External test data
├── test_api_basics.py       # Core HTTP method tests
├── test_chaining.py         # Request chaining and lifecycle tests
├── test_schema.py           # Schema validation tests
└── test_data_driven_api.py  # Parametrized data-driven API tests
```

## Setup & Installation
1. Clone the repo:
git clone https://github.com/RJEsbenshadePro/phase4-api.git
2. Navigate to the project folder:
cd phase4-api
3. Create and activate a virtual environment:
python3 -m venv venv
source venv/bin/activate
4. Install dependencies:
pip install requests pytest pytest-html jsonschema

## Running Tests
Run the full suite: pytest -v

Run a specific test file: test_schema.py -v

## Test Report
An HTML report is automatically generated after every run:
open test-results/report.html

## API Under Test
[JSONPlaceholder](https://jsonplaceholder.typicode.com) — a free public
REST API designed for testing and prototyping.

