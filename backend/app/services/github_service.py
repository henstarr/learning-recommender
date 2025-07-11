import httpx
from typing import List, Optional, Dict, Any
from ..models.schemas import GitHubProfile, GitHubRepository
from ..core.config import settings
from datetime import datetime

class GitHubService:
    """Service for interacting with GitHub API"""
    
    def __init__(self):
        self.base_url = "https://api.github.com"
        self.headers = {}
        if settings.github_token:
            self.headers["Authorization"] = f"token {settings.github_token}"
    
    async def get_profile(self, username: str) -> GitHubProfile:
        """Fetch GitHub user profile"""
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.base_url}/users/{username}",
                headers=self.headers
            )
            response.raise_for_status()
            data = response.json()
            
            return GitHubProfile(
                username=data["login"],
                name=data.get("name"),
                bio=data.get("bio"),
                public_repos=data["public_repos"],
                followers=data["followers"],
                following=data["following"],
                created_at=datetime.fromisoformat(data["created_at"].replace("Z", "+00:00")) if data.get("created_at") else None,
                updated_at=datetime.fromisoformat(data["updated_at"].replace("Z", "+00:00")) if data.get("updated_at") else None
            )
    
    async def get_repositories(self, username: str, limit: int = 30) -> List[GitHubRepository]:
        """Fetch user's public repositories"""
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.base_url}/users/{username}/repos",
                headers=self.headers,
                params={"sort": "updated", "per_page": limit}
            )
            response.raise_for_status()
            data = response.json()
            
            repositories = []
            for repo_data in data:
                # Get languages for this repository
                languages = await self._get_repository_languages(username, repo_data["name"])
                
                repo = GitHubRepository(
                    name=repo_data["name"],
                    description=repo_data.get("description"),
                    language=repo_data.get("language"),
                    languages=languages,
                    stars=repo_data["stargazers_count"],
                    forks=repo_data["forks_count"],
                    created_at=datetime.fromisoformat(repo_data["created_at"].replace("Z", "+00:00")) if repo_data.get("created_at") else None,
                    updated_at=datetime.fromisoformat(repo_data["updated_at"].replace("Z", "+00:00")) if repo_data.get("updated_at") else None,
                    topics=repo_data.get("topics", [])
                )
                repositories.append(repo)
            
            return repositories
    
    async def get_starred_repositories(self, username: str, limit: int = 30) -> List[GitHubRepository]:
        """Fetch user's starred repositories"""
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.base_url}/users/{username}/starred",
                headers=self.headers,
                params={"per_page": limit}
            )
            response.raise_for_status()
            data = response.json()
            
            repositories = []
            for repo_data in data:
                repo = GitHubRepository(
                    name=repo_data["name"],
                    description=repo_data.get("description"),
                    language=repo_data.get("language"),
                    stars=repo_data["stargazers_count"],
                    forks=repo_data["forks_count"],
                    created_at=datetime.fromisoformat(repo_data["created_at"].replace("Z", "+00:00")) if repo_data.get("created_at") else None,
                    updated_at=datetime.fromisoformat(repo_data["updated_at"].replace("Z", "+00:00")) if repo_data.get("updated_at") else None,
                    topics=repo_data.get("topics", [])
                )
                repositories.append(repo)
            
            return repositories
    
    async def _get_repository_languages(self, username: str, repo_name: str) -> Dict[str, int]:
        """Get languages used in a repository"""
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{self.base_url}/repos/{username}/{repo_name}/languages",
                    headers=self.headers
                )
                response.raise_for_status()
                return response.json()
        except:
            return {}
