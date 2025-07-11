from pydantic import BaseModel, HttpUrl
from typing import List, Optional, Dict, Any
from datetime import datetime

class GitHubProfile(BaseModel):
    """GitHub profile data model"""
    username: str
    name: Optional[str] = None
    bio: Optional[str] = None
    public_repos: int = 0
    followers: int = 0
    following: int = 0
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class GitHubRepository(BaseModel):
    """GitHub repository data model"""
    name: str
    description: Optional[str] = None
    language: Optional[str] = None
    languages: Dict[str, int] = {}
    stars: int = 0
    forks: int = 0
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    topics: List[str] = []

class LinkedInProfile(BaseModel):
    """LinkedIn profile data model (placeholder)"""
    profile_url: HttpUrl
    skills: List[str] = []
    experience: List[Dict[str, Any]] = []
    education: List[Dict[str, Any]] = []

class UserProfile(BaseModel):
    """Combined user profile"""
    github_username: Optional[str] = None
    linkedin_url: Optional[HttpUrl] = None
    github_profile: Optional[GitHubProfile] = None
    linkedin_profile: Optional[LinkedInProfile] = None
    repositories: List[GitHubRepository] = []
    starred_repos: List[GitHubRepository] = []

class SkillGap(BaseModel):
    """Identified skill gap"""
    skill: str
    category: str
    confidence: float
    reasoning: str

class LearningRecommendation(BaseModel):
    """Learning recommendation model"""
    title: str
    description: str
    type: str  # "project", "course", "tutorial"
    difficulty: str  # "beginner", "intermediate", "advanced"
    estimated_time: str
    skills_gained: List[str]
    resources: List[Dict[str, str]]
    reasoning: str

class RecommendationRequest(BaseModel):
    """Request model for generating recommendations"""
    github_username: Optional[str] = None
    linkedin_url: Optional[HttpUrl] = None

class RecommendationResponse(BaseModel):
    """Response model for recommendations"""
    user_profile: UserProfile
    skill_gaps: List[SkillGap]
    recommendations: List[LearningRecommendation]
    generated_at: datetime
