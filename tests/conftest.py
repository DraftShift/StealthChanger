"""
Shared pytest fixtures and configuration for the StealthChanger test suite.
"""
import os
import sys
import tempfile
from pathlib import Path
from typing import Generator, Dict, Any

import pytest


@pytest.fixture
def temp_dir() -> Generator[Path, None, None]:
    """
    Provide a temporary directory for test files.
    
    Yields:
        Path: Path to a temporary directory that is cleaned up after the test.
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


@pytest.fixture
def mock_config() -> Dict[str, Any]:
    """
    Provide a mock configuration dictionary for testing.
    
    Returns:
        Dict[str, Any]: A dictionary with common configuration options.
    """
    return {
        "build_volume": {
            "x": 300,
            "y": 300,
            "z": 300
        },
        "printer_type": "voron_2.4",
        "toolchanger": {
            "enabled": True,
            "tools": 4,
            "dock_spacing": 50
        },
        "output_format": "svg",
        "debug": False
    }


@pytest.fixture
def sample_polyline_points() -> list:
    """
    Provide sample polyline points for CAD testing.
    
    Returns:
        list: A list of coordinate tuples for testing polyline operations.
    """
    return [
        (0, 0),
        (10, 0),
        (10, 10),
        (0, 10)
    ]


@pytest.fixture
def project_root() -> Path:
    """
    Get the project root directory.
    
    Returns:
        Path: Path to the project root directory.
    """
    return Path(__file__).parent.parent


@pytest.fixture
def cad_query_path(project_root: Path) -> Path:
    """
    Get the path to the Cad Query module.
    
    Returns:
        Path: Path to the Cad Query directory.
    """
    return project_root / "UserMods" / "Dumplap" / "Stealth Changer Build Plate Slicer Textures" / "Cad Query"


@pytest.fixture(autouse=True)
def add_project_to_path(project_root: Path):
    """
    Automatically add the project root to Python path for all tests.
    
    This ensures that modules can be imported during testing.
    """
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))


@pytest.fixture
def mock_cadquery(monkeypatch):
    """
    Mock the cadquery module for tests that don't need the actual CAD functionality.
    
    This is useful for unit tests that test logic without requiring the heavy
    cadquery dependencies.
    """
    class MockWorkplane:
        def __init__(self, *args, **kwargs):
            pass
        
        def polyline(self, points):
            return self
        
        def close(self):
            return self
        
        def extrude(self, height):
            return self
    
    class MockExporters:
        @staticmethod
        def export(obj, filename, **kwargs):
            pass
    
    class MockCQ:
        Workplane = MockWorkplane
        exporters = MockExporters()
    
    monkeypatch.setitem(sys.modules, "cadquery", MockCQ)
    return MockCQ


@pytest.fixture
def clean_environment(monkeypatch):
    """
    Provide a clean environment for tests by clearing specific env variables.
    """
    env_vars_to_clear = [
        "PYTHONPATH",
        "OUTPUT_DIR",
        "DEBUG",
    ]
    
    for var in env_vars_to_clear:
        monkeypatch.delenv(var, raising=False)


@pytest.fixture
def mock_file_operations(tmp_path, monkeypatch):
    """
    Mock file operations to use a temporary directory.
    
    This prevents tests from writing to the actual filesystem.
    """
    def mock_open(filename, mode='r', *args, **kwargs):
        # Redirect file operations to tmp directory
        if 'w' in mode or 'a' in mode:
            filepath = tmp_path / Path(filename).name
            return open(filepath, mode, *args, **kwargs)
        return open(filename, mode, *args, **kwargs)
    
    monkeypatch.setattr("builtins.open", mock_open)
    return tmp_path


# Pytest configuration hooks

def pytest_configure(config):
    """
    Configure pytest with custom settings.
    """
    config.addinivalue_line(
        "markers", "requires_cadquery: mark test as requiring cadquery installation"
    )


def pytest_collection_modifyitems(config, items):
    """
    Modify test collection to add markers based on test location.
    """
    for item in items:
        # Add unit/integration markers based on test location
        if "unit" in str(item.fspath):
            item.add_marker(pytest.mark.unit)
        elif "integration" in str(item.fspath):
            item.add_marker(pytest.mark.integration)
        
        # Mark slow tests (those with 'slow' in their name)
        if "slow" in item.nodeid.lower():
            item.add_marker(pytest.mark.slow)