from typing import List, Dict, Set
from datetime import datetime
from ..models.schemas import (
    UserProfile, RecommendationResponse, LearningRecommendation,
    SkillGap, GitHubProfile, LinkedInProfile
)
from .github_service import GitHubService
from .linkedin_service import LinkedInService

class RecommendationService:
    """Service for generating personalized learning recommendations"""
    
    def __init__(self):
        self.github_service = GitHubService()
        self.linkedin_service = LinkedInService()
    
    async def build_user_profile(
        self, 
        github_username: str = None, 
        linkedin_url: str = None
    ) -> UserProfile:
        """Build comprehensive user profile from GitHub and LinkedIn data"""
        
        user_profile = UserProfile()
        
        # Fetch GitHub data
        if github_username:
            user_profile.github_username = github_username
            user_profile.github_profile = await self.github_service.get_profile(github_username)
            user_profile.repositories = await self.github_service.get_repositories(github_username)
            user_profile.starred_repos = await self.github_service.get_starred_repositories(github_username)
        
        # Fetch LinkedIn data
        if linkedin_url:
            user_profile.linkedin_url = linkedin_url
            user_profile.linkedin_profile = await self.linkedin_service.get_profile(linkedin_url)
        
        return user_profile
    
    async def generate_recommendations(self, user_profile: UserProfile) -> RecommendationResponse:
        """Generate personalized learning recommendations"""
        
        # Analyze user's current skills
        current_skills = self._extract_current_skills(user_profile)
        
        # Identify skill gaps
        skill_gaps = self._identify_skill_gaps(current_skills, user_profile)
        
        # Generate recommendations based on skill gaps
        recommendations = self._generate_learning_recommendations(skill_gaps, current_skills)
        
        return RecommendationResponse(
            user_profile=user_profile,
            skill_gaps=skill_gaps,
            recommendations=recommendations,
            generated_at=datetime.now()
        )
    
    def _extract_current_skills(self, user_profile: UserProfile) -> Set[str]:
        """Extract current skills from user profile"""
        skills = set()
        
        # Extract from GitHub repositories
        if user_profile.repositories:
            for repo in user_profile.repositories:
                if repo.language:
                    skills.add(repo.language.lower())
                
                # Add languages from language stats
                for lang in repo.languages.keys():
                    skills.add(lang.lower())
                
                # Add topics as skills
                for topic in repo.topics:
                    skills.add(topic.lower())
        
        # Extract from starred repositories
        if user_profile.starred_repos:
            for repo in user_profile.starred_repos:
                if repo.language:
                    skills.add(repo.language.lower())
                for topic in repo.topics:
                    skills.add(topic.lower())
        
        # Extract from LinkedIn profile
        if user_profile.linkedin_profile:
            for skill in user_profile.linkedin_profile.skills:
                skills.add(skill.lower())
        
        return skills
    
    def _identify_skill_gaps(self, current_skills: Set[str], user_profile: UserProfile) -> List[SkillGap]:
        """Identify skill gaps based on current skills and profile analysis"""
        skill_gaps = []
        
        # Define skill categories and important skills
        skill_categories = {
            "frontend": ["react", "vue", "angular", "typescript", "html", "css", "tailwind"],
            "backend": ["node.js", "express", "fastapi", "django", "spring", "ruby on rails"],
            "database": ["postgresql", "mongodb", "redis", "mysql", "sqlite"],
            "devops": ["docker", "kubernetes", "aws", "terraform", "jenkins"],
            "mobile": ["react native", "flutter", "swift", "kotlin"],
            "data": ["pandas", "numpy", "machine learning", "tensorflow", "pytorch"],
            "testing": ["jest", "pytest", "cypress", "selenium"]
        }
        
        # Analyze gaps in each category
        for category, skills_in_category in skill_categories.items():
            missing_skills = []
            for skill in skills_in_category:
                if skill not in current_skills:
                    missing_skills.append(skill)
            
            # If user has some skills in category but missing key ones, it's a gap
            has_some_skills = any(skill in current_skills for skill in skills_in_category)
            
            if missing_skills and (has_some_skills or self._should_recommend_category(category, user_profile)):
                # Pick the most important missing skill
                priority_skill = missing_skills[0]  # Simple prioritization
                
                skill_gaps.append(SkillGap(
                    skill=priority_skill,
                    category=category,
                    confidence=0.8,
                    reasoning=f"You have {category} experience but could benefit from learning {priority_skill}"
                ))
        
        return skill_gaps[:5]  # Return top 5 gaps
    
    def _should_recommend_category(self, category: str, user_profile: UserProfile) -> bool:
        """Determine if a category should be recommended based on user profile"""
        # Simple logic - recommend backend if they have frontend, and vice versa
        current_skills = self._extract_current_skills(user_profile)
        
        frontend_skills = ["javascript", "react", "vue", "angular", "html", "css"]
        backend_skills = ["python", "java", "node.js", "go", "ruby"]
        
        has_frontend = any(skill in current_skills for skill in frontend_skills)
        has_backend = any(skill in current_skills for skill in backend_skills)
        
        if category == "backend" and has_frontend and not has_backend:
            return True
        if category == "frontend" and has_backend and not has_frontend:
            return True
        if category == "database" and (has_frontend or has_backend):
            return True
        
        return False
    
    def _generate_learning_recommendations(
        self, 
        skill_gaps: List[SkillGap], 
        current_skills: Set[str]
    ) -> List[LearningRecommendation]:
        """Generate learning recommendations based on skill gaps"""
        
        recommendations = []
        
        # Recommendation templates
        recommendation_templates = {
            "react": {
                "title": "Build a Full-Stack React Application",
                "description": "Create a modern web application using React, including state management, routing, and API integration",
                "type": "project",
                "difficulty": "intermediate",
                "estimated_time": "2-3 weeks",
                "skills_gained": ["React", "JavaScript", "HTML/CSS", "State Management", "API Integration"],
                "resources": [
                    {"type": "tutorial", "url": "https://react.dev/learn"},
                    {"type": "course", "url": "https://www.freecodecamp.org/learn/front-end-development-libraries/"}
                ]
            },
            "fastapi": {
                "title": "Build REST APIs with FastAPI",
                "description": "Learn to create high-performance APIs using FastAPI with automatic documentation and validation",
                "type": "project",
                "difficulty": "intermediate",
                "estimated_time": "1-2 weeks",
                "skills_gained": ["FastAPI", "Python", "REST APIs", "Database Integration", "Authentication"],
                "resources": [
                    {"type": "documentation", "url": "https://fastapi.tiangolo.com/"},
                    {"type": "tutorial", "url": "https://fastapi.tiangolo.com/tutorial/"}
                ]
            },
            "docker": {
                "title": "Containerize Your Applications with Docker",
                "description": "Learn containerization by dockerizing your existing projects and deploying them",
                "type": "project",
                "difficulty": "intermediate",
                "estimated_time": "1 week",
                "skills_gained": ["Docker", "Containerization", "DevOps", "Deployment"],
                "resources": [
                    {"type": "tutorial", "url": "https://docs.docker.com/get-started/"},
                    {"type": "course", "url": "https://www.docker.com/101-tutorial/"}
                ]
            },
            "postgresql": {
                "title": "Database Design and Management with PostgreSQL",
                "description": "Learn database design principles and advanced PostgreSQL features",
                "type": "course",
                "difficulty": "intermediate",
                "estimated_time": "2 weeks",
                "skills_gained": ["PostgreSQL", "Database Design", "SQL", "Performance Optimization"],
                "resources": [
                    {"type": "course", "url": "https://www.postgresql.org/docs/current/tutorial.html"},
                    {"type": "practice", "url": "https://sqlbolt.com/"}
                ]
            }
        }
        
        # Generate recommendations for each skill gap
        for gap in skill_gaps:
            skill_key = gap.skill.replace(" ", "").lower()
            
            if skill_key in recommendation_templates:
                template = recommendation_templates[skill_key]
                recommendation = LearningRecommendation(
                    title=template["title"],
                    description=template["description"],
                    type=template["type"],
                    difficulty=template["difficulty"],
                    estimated_time=template["estimated_time"],
                    skills_gained=template["skills_gained"],
                    resources=template["resources"],
                    reasoning=gap.reasoning
                )
                recommendations.append(recommendation)
            else:
                # Generic recommendation
                recommendation = LearningRecommendation(
                    title=f"Learn {gap.skill.title()}",
                    description=f"Expand your {gap.category} skills by learning {gap.skill}",
                    type="course",
                    difficulty="intermediate",
                    estimated_time="1-2 weeks",
                    skills_gained=[gap.skill.title()],
                    resources=[
                        {"type": "search", "url": f"https://www.google.com/search?q={gap.skill}+tutorial"}
                    ],
                    reasoning=gap.reasoning
                )
                recommendations.append(recommendation)
        
        return recommendations[:5]  # Return top 5 recommendations
    
    async def get_example_recommendations(self) -> RecommendationResponse:
        """Get example recommendations for demo purposes"""
        
        # Mock user profile
        user_profile = UserProfile(
            github_username="example_user",
            github_profile=GitHubProfile(
                username="example_user",
                name="Example User",
                bio="Full-stack developer",
                public_repos=15,
                followers=50,
                following=30
            )
        )
        
        # Mock skill gaps
        skill_gaps = [
            SkillGap(
                skill="Docker",
                category="devops",
                confidence=0.9,
                reasoning="You have many projects but no containerization experience"
            )
        ]
        
        # Mock recommendations
        recommendations = [
            LearningRecommendation(
                title="Containerize Your Applications with Docker",
                description="Learn containerization by dockerizing your existing projects",
                type="project",
                difficulty="intermediate",
                estimated_time="1 week",
                skills_gained=["Docker", "Containerization", "DevOps"],
                resources=[
                    {"type": "tutorial", "url": "https://docs.docker.com/get-started/"}
                ],
                reasoning="Perfect next step for your development workflow"
            )
        ]
        
        return RecommendationResponse(
            user_profile=user_profile,
            skill_gaps=skill_gaps,
            recommendations=recommendations,
            generated_at=datetime.now()
        )
