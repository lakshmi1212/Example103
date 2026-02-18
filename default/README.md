# Example103 Math Operations

## Overview
This repository provides basic math operations (addition and subtraction) implemented in Python, along with comprehensive pytest-based tests and CI/CD workflow integration.

## Folder Structure
- `src/`: Production code for math operations
- `tests/`: Pytest test files
- `default/`: Documentation, requirements, and metadata

## Usage

### Install dependencies
```
pip install -r default/requirements.txt
```

### Run tests
```
pytest tests/
```

## CI/CD Workflow
Workflow file: `.github/workflows/ci.yml`
- Triggers: Push to Feature1, Pull Request to main
- Test command: `python -m pytest tests/ -v --tb=short --junitxml=reports/report.xml --html=reports/report.html --self-contained-html`
- Reports generated in `reports/` directory

## Math Operations API
```
from src.math_operations import add, subtract

result1 = add(2, 3)
result2 = subtract(5, 2)
```

## License
MIT
