# Example103 Math Operations

## Overview
This repository provides basic math operations (addition and subtraction) implemented in Python. Unit tests are provided using pytest. CI workflow is enabled for test automation.

## Folder Structure
- `src/` : Contains production Python code
- `tests/` : Contains pytest test files
- `default/` : Contains workflow metadata and requirements

## Usage
```
from src.math_operations import add, subtract
result1 = add(2, 3)      # 5
result2 = subtract(5, 3) # 2
```

## Running Tests
Install dependencies:
```
pip install -r default/requirements.txt
```
Run tests:
```
python -m pytest tests/ -v --tb=short --junitxml=reports/report.xml --html=reports/report.html --self-contained-html
```

## CI Workflow
See `.github/workflows/ci.yml` for details. The workflow runs tests automatically on push and pull request.

## Requirements
Python 3.10+

## Meta Data
See `default/math.json` for CI workflow metadata.
