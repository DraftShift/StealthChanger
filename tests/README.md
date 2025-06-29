# StealthChanger Testing Infrastructure

This directory contains the testing infrastructure for the StealthChanger project.

## Setup

The project uses Poetry for dependency management and pytest for testing.

### Installing Dependencies

```bash
poetry install
```

To install optional CAD dependencies:
```bash
poetry install --with cad
```

## Running Tests

There are several ways to run tests:

### Using Poetry Scripts
```bash
poetry run test   # or 'poetry run tests'
```

### Using pytest directly
```bash
poetry run pytest
```

### With coverage reporting
```bash
poetry run pytest --cov=UserMods --cov-report=term-missing --cov-report=html
```

### Running specific test types
```bash
# Run only unit tests
poetry run pytest -m unit

# Run only integration tests  
poetry run pytest -m integration

# Exclude slow tests
poetry run pytest -m "not slow"
```

## Test Structure

- `tests/` - Main test directory
  - `conftest.py` - Shared pytest fixtures and configuration
  - `test_validation.py` - Infrastructure validation tests
  - `unit/` - Unit tests directory
  - `integration/` - Integration tests directory

## Writing Tests

### Using Fixtures

The `conftest.py` file provides several useful fixtures:

- `temp_dir` - Temporary directory for test files
- `mock_config` - Mock configuration dictionary
- `project_root` - Path to project root
- `mock_cadquery` - Mock for cadquery module (for tests without CAD dependencies)
- `clean_environment` - Clean environment variables
- `mock_file_operations` - Mock file operations to use temp directory

### Test Markers

The following markers are available:
- `@pytest.mark.unit` - Mark test as a unit test
- `@pytest.mark.integration` - Mark test as an integration test  
- `@pytest.mark.slow` - Mark test as slow-running
- `@pytest.mark.requires_cadquery` - Mark test as requiring cadquery

## Coverage Configuration

Coverage is configured in `pyproject.toml` with:
- 80% coverage requirement
- HTML and XML report generation
- Exclusion of test files and common patterns

To generate coverage reports manually:
```bash
poetry run pytest --cov=UserMods --cov-fail-under=80
```