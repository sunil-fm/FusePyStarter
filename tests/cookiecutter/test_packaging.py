import os
import types
from unittest import mock

from fusepystarter import __version__
from fusepystarter.cookiecutter import cookiecutter_template

# ----------------------------
# Version & Metadata Tests
# ----------------------------


def test_version_property():
    """Test that version property returns the correct package version."""
    main = cookiecutter_template()
    assert main.version == __version__


@mock.patch("fusepystarter.cookiecutter.packaging.toml.load")
def test_get_project_meta(mock_toml_load):
    """Test loading project metadata from pyproject.toml using a mocked loader."""
    mock_toml_load.return_value = {
        "project": {
            "name": "Test Project",
            "version": "1.0.0",
            "description": "A test project",
        }
    }
    result = cookiecutter_template._get_project_meta()
    assert result == {
        "name": "Test Project",
        "version": "1.0.0",
        "description": "A test project",
    }
    mock_toml_load.assert_called_once_with("pyproject.toml")


def test_get_project_meta_returns_dict(monkeypatch, tmp_path):
    """Test that _get_project_meta loads the pyproject.toml correctly from file."""
    pyproject_path = tmp_path / "pyproject.toml"
    pyproject_path.write_text("""
[project]
name = "fusepystarter"
version = "0.1.0"
    """)
    monkeypatch.chdir(tmp_path)
    meta = cookiecutter_template._get_project_meta()
    assert isinstance(meta, dict)
    assert meta["name"] == "fusepystarter"
    assert meta["version"] == "0.1.0"


# ----------------------------
# Main Class Structure Tests
# ----------------------------


def test_main_has_init_and_version():
    """Ensure Main class has expected methods and attributes."""
    assert hasattr(cookiecutter_template, "init") and isinstance(
        cookiecutter_template.init, types.FunctionType
    )
    assert hasattr(cookiecutter_template, "version")  # property


# ----------------------------
# Project Structure Tests
# ----------------------------


def test_pyproject_toml_exists():
    assert os.path.isfile("pyproject.toml"), "Missing pyproject.toml file"


def test_cookiecutter_json_exists():
    assert os.path.isfile("cookiecutter.json"), "Missing cookiecutter.json file"


def test_tests_directory_exists():
    assert os.path.isdir("tests"), "Missing tests/ directory"


def test_tox_ini_exists():
    assert os.path.isfile("tox.ini"), "Missing tox.ini file"


# ----------------------------
# Init Method Tests
# ----------------------------


@mock.patch("fusepystarter.cookiecutter.packaging.cookiecutter")
@mock.patch("fusepystarter.cookiecutter.packaging.os.chdir")
@mock.patch("fusepystarter.cookiecutter.packaging.subprocess.run")
@mock.patch(
    "fusepystarter.cookiecutter.packaging.spawn.find_executable",
    side_effect=["/usr/bin/git", "/usr/bin/python3", "/usr/local/bin/uv"],
)
def test_init_success(mock_spawn, mock_run, mock_chdir, mock_cookiecutter):
    """Test cookiecutter_template.init runs successfully and performs expected calls."""
    mock_cookiecutter.return_value = "/tmp/test-project"

    cookiecutter_template.init()

    mock_cookiecutter.assert_called_once_with("gh:sunil-fm/FusePyStarter")
    mock_chdir.assert_called_once_with("/tmp/test-project")
    assert mock_run.call_count >= 5
