"""Version endpoint for the API."""

from fastapi import APIRouter, HTTPException
from app.utils import get_project_info

router = APIRouter()


@router.get("/version")
async def get_version():
    """Get the application version and name from pyproject.toml.
    
    Returns:
        Dict containing the project name and version.
        
    Raises:
        HTTPException: If there's an error reading the project info.
    """
    try:
        project_info = get_project_info()
        return {
            "version": project_info["version"],
            "name": project_info["name"]
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error retrieving version information: {str(e)}"
        )