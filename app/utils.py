"""Utility functions for the application."""

import tomllib
from pathlib import Path
from typing import Dict, Any


def read_pyproject_toml() -> Dict[str, Any]:
    """Read and parse the pyproject.toml file.
    
    Returns:
        Dict containing the parsed TOML data.
        
    Raises:
        FileNotFoundError: If pyproject.toml is not found.
        tomllib.TOMLDecodeError: If the TOML file is malformed.
    """
    pyproject_path = Path("pyproject.toml")
    
    if not pyproject_path.exists():
        raise FileNotFoundError("pyproject.toml not found")
    
    with open(pyproject_path, "rb") as f:
        return tomllib.load(f)


def get_project_info() -> Dict[str, str]:
    """Extract project name and version from pyproject.toml.
    
    Returns:
        Dict with 'name' and 'version' keys.
        
    Raises:
        FileNotFoundError: If pyproject.toml is not found.
        KeyError: If required project fields are missing.
        tomllib.TOMLDecodeError: If the TOML file is malformed.
    """
    try:
        data = read_pyproject_toml()
        project = data.get("project", {})
        
        name = project.get("name")
        version = project.get("version")
        
        if not name:
            raise KeyError("Project name not found in pyproject.toml")
        if not version:
            raise KeyError("Project version not found in pyproject.toml")
            
        return {"name": name, "version": version}
        
    except Exception as e:
        # Re-raise with more context for debugging
        raise type(e)(f"Error reading project info: {str(e)}") from e
