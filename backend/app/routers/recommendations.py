from fastapi import APIRouter, HTTPException
from ..models.schemas import RecommendationRequest, RecommendationResponse
from ..services.recommendation_service import RecommendationService
from ..services.github_service import GitHubService
from ..services.linkedin_service import LinkedInService

router = APIRouter()

@router.post("/generate", response_model=RecommendationResponse)
async def generate_recommendations(request: RecommendationRequest):
    """
    Generate personalized learning recommendations based on user's GitHub and LinkedIn profiles
    """
    try:
        # Initialize services
        github_service = GitHubService()
        linkedin_service = LinkedInService()
        recommendation_service = RecommendationService()
        
        # Fetch user profile data
        user_profile = await recommendation_service.build_user_profile(
            github_username=request.github_username,
            linkedin_url=request.linkedin_url
        )
        
        # Generate recommendations
        recommendations = await recommendation_service.generate_recommendations(user_profile)
        
        return recommendations
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to generate recommendations: {str(e)}")

@router.get("/example")
async def get_example_recommendations():
    """
    Get example recommendations for demo purposes
    """
    # This will return mock data for now
    recommendation_service = RecommendationService()
    return await recommendation_service.get_example_recommendations()
