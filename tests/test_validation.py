"""
Validation tests to ensure the testing infrastructure is properly configured.
"""
import sys
from pathlib import Path

import pytest


class TestInfrastructureValidation:
    """Test suite to validate the testing infrastructure setup."""
    
    def test_pytest_installed(self):
        """Test that pytest is available."""
        assert "pytest" in sys.modules
    
    def test_project_structure(self, project_root):
        """Test that the project structure is set up correctly."""
        assert project_root.exists()
        assert (project_root / "tests").exists()
        assert (project_root / "tests" / "__init__.py").exists()
        assert (project_root / "tests" / "conftest.py").exists()
        assert (project_root / "tests" / "unit").exists()
        assert (project_root / "tests" / "integration").exists()
    
    def test_pyproject_toml_exists(self, project_root):
        """Test that pyproject.toml exists and is configured."""
        pyproject_path = project_root / "pyproject.toml"
        assert pyproject_path.exists()
        
        # Check that it contains expected content
        content = pyproject_path.read_text()
        assert "[tool.poetry]" in content
        assert "[tool.pytest.ini_options]" in content
        assert "[tool.coverage.run]" in content
    
    def test_fixtures_available(self, temp_dir, mock_config):
        """Test that common fixtures are available and working."""
        # Test temp_dir fixture
        assert temp_dir.exists()
        assert temp_dir.is_dir()
        
        # Test mock_config fixture
        assert isinstance(mock_config, dict)
        assert "build_volume" in mock_config
        assert mock_config["toolchanger"]["enabled"] is True
    
    @pytest.mark.unit
    def test_unit_marker(self):
        """Test that the unit marker is available."""
        assert True
    
    @pytest.mark.integration
    def test_integration_marker(self):
        """Test that the integration marker is available."""
        assert True
    
    @pytest.mark.slow
    def test_slow_marker(self):
        """Test that the slow marker is available."""
        assert True
    
    def test_mock_cadquery_fixture(self, mock_cadquery):
        """Test that the mock cadquery fixture works."""
        # Create a workplane using the mock
        wp = mock_cadquery.Workplane("XY")
        result = wp.polyline([(0, 0), (1, 1)]).close().extrude(1)
        assert result is not None
    
    def test_coverage_configured(self, project_root):
        """Test that coverage is properly configured."""
        pyproject_path = project_root / "pyproject.toml"
        content = pyproject_path.read_text()
        
        # Check coverage configuration sections exist
        assert "[tool.coverage.run]" in content
        assert "[tool.coverage.report]" in content
        assert "fail_under = 80" in content


class TestSampleUnitTest:
    """A sample unit test to demonstrate the setup."""
    
    def test_basic_assertion(self):
        """Simple test to verify pytest is working."""
        assert 2 + 2 == 4
    
    def test_using_temp_dir(self, temp_dir):
        """Test using the temp_dir fixture."""
        test_file = temp_dir / "test.txt"
        test_file.write_text("Hello, World!")
        
        assert test_file.exists()
        assert test_file.read_text() == "Hello, World!"
    
    def test_parametrized(self):
        """Test with parametrization."""
        test_cases = [
            (1, 1, 2),
            (2, 3, 5),
            (10, -5, 5),
        ]
        
        for a, b, expected in test_cases:
            assert a + b == expected


def test_module_level_test():
    """Test that module-level tests are discovered."""
    assert True