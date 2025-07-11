from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import recommendations, profiles
from .core.config import settings

app = FastAPI(
    title="Learning Recommender API",
    description="API for generating personalized learning recommendations based on LinkedIn and GitHub profiles",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(recommendations.router, prefix="/api/v1/recommendations", tags=["recommendations"])
app.include_router(profiles.router, prefix="/api/v1/profiles", tags=["profiles"])

@app.get("/")
async def root():
    return {"message": "Learning Recommender API is running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
