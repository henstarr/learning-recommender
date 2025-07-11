from fastapi import APIRouter, HTTPException
from ..models.schemas import UserProfile, GitHubProfile, LinkedInProfile
from ..services.github_service import GitHubService
from ..services.linkedin_service import LinkedInService

router = APIRouter()

@router.get("/github/{username}", response_model=GitHubProfile)
async def get_github_profile(username: str):
    """
    Fetch GitHub profile information
    """
    try:
        github_service = GitHubService()
        profile = await github_service.get_profile(username)
        return profile
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"GitHub profile not found: {str(e)}")

@router.post("/linkedin", response_model=LinkedInProfile)
async def get_linkedin_profile(linkedin_url: str):
    """
    Fetch LinkedIn profile information (placeholder)
    """
    try:
        linkedin_service = LinkedInService()
        profile = await linkedin_service.get_profile(linkedin_url)
        return profile
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"LinkedIn profile not found: {str(e)}")

@router.post("/combined", response_model=UserProfile)
async def get_combined_profile(github_username: str = None, linkedin_url: str = None):
    """
    Get combined user profile from GitHub and LinkedIn
    """
    try:
        user_profile = UserProfile()
        
        if github_username:
            github_service = GitHubService()
            user_profile.github_username = github_username
            user_profile.github_profile = await github_service.get_profile(github_username)
            user_profile.repositories = await github_service.get_repositories(github_username)
            user_profile.starred_repos = await github_service.get_starred_repositories(github_username)
        
        if linkedin_url:
            linkedin_service = LinkedInService()
            user_profile.linkedin_url = linkedin_url
            user_profile.linkedin_profile = await linkedin_service.get_profile(linkedin_url)
        
        return user_profile
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch profile: {str(e)}")
