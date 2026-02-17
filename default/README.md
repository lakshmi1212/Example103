# Example103 Math Operations

## Overview
This project provides basic math operations (addition and subtraction) in Python, along with comprehensive pytest test cases and CI workflow integration guidance.

## Usage

### Math Operations
- `add(a, b)`: Returns the sum of two numbers.
- `subtract(a, b)`: Returns the difference between two numbers.

```
from src.math_operations import add, subtract
result_add = add(2, 3)
result_subtract = subtract(5, 2)
```

### Running Tests
Install requirements:
```
pip install -r default/requirements.txt
```

Run all tests:
```
pytest tests/
```

## CI/CD Workflow
- The CI pipeline runs on push to `Feature1` and pull requests to `main`.
- Test reports are generated in both JUnit and HTML formats.
- Workflow file: `.github/workflows/ci.yml`

## Project Structure
- `src/`: Source code
- `tests/`: Test files
- `default/`: Metadata and documentation

## Requirements
- Python 3.10 or higher
- Pytest
