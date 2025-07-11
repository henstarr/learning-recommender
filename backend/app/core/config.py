from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    """Application settings and configuration"""
    
    # API Settings
    api_title: str = "Learning Recommender API"
    api_version: str = "1.0.0"
    debug: bool = True
    
    # LinkedIn API (placeholder)
    linkedin_client_id: Optional[str] = None
    linkedin_client_secret: Optional[str] = None
    
    # GitHub API
    github_token: Optional[str] = None
    
    # Database (future implementation)
    database_url: Optional[str] = None
    
    class Config:
        env_file = ".env"

settings = Settings()
