# Learning Recommender

A web application that analyzes your GitHub and LinkedIn profiles to provide personalized learning recommendations.

## Tech Stack

- **Backend**: FastAPI (Python)
- **Frontend**: Next.js (React/TypeScript)
- **Scraping**: Beautiful Soup, Selenium
- **Styling**: Tailwind CSS

## Features

- **GitHub Analysis**: Analyzes your repositories, languages, and starred projects
- **LinkedIn Analysis**: Extracts skills and experience from your LinkedIn profile
- **Smart Recommendations**: Identifies skill gaps and suggests relevant projects or courses
- **Beautiful UI**: Modern, responsive interface built with Next.js and Tailwind CSS

## Getting Started

### Prerequisites

- Python 3.8+
- Node.js 18+
- npm or yarn

### 1. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Install dependencies
pip install -r requirements.txt

# Set up environment variables (optional)
cp .env.example .env
# Edit .env with your GitHub token if you want higher rate limits

# Start the FastAPI server
./start.sh
# Or manually: uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The backend will be running at `http://localhost:8000`

### 2. Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start the development server
npm run dev
```

The frontend will be running at `http://localhost:3000`

## How to Use

1. **Open your browser** and go to `http://localhost:3000`

2. **Enter your details**:
   - GitHub username (e.g., `octocat`)
   - LinkedIn profile URL (e.g., `https://linkedin.com/in/your-profile`)

3. **Click "Get Recommendations"** to analyze your profiles

4. **View your personalized recommendations** including:
   - Recommended projects to build
   - Courses to take
   - Skills to learn
   - Difficulty levels and time estimates

## API Endpoints

- `GET /`: API documentation
- `POST /api/recommendations`: Generate recommendations
- `GET /api/profile/{username}`: Get GitHub profile analysis

## Example Request

```bash
curl -X POST "http://localhost:8000/api/recommendations" \
  -H "Content-Type: application/json" \
  -d '{
    "github_username": "octocat",
    "linkedin_url": "https://linkedin.com/in/octocat"
  }'
```

## Environment Variables

### Backend (.env)
```
GITHUB_TOKEN=your_github_token_here  # Optional, for higher rate limits
LINKEDIN_EMAIL=your_email            # Optional, for LinkedIn scraping
LINKEDIN_PASSWORD=your_password      # Optional, for LinkedIn scraping
```

## Development

### Running Tests

```bash
# Backend tests
cd backend
pytest

# Frontend tests
cd frontend
npm test
```

### Code Structure

```
learning-recommender/
├── backend/
│   ├── app/
│   │   ├── core/          # Configuration
│   │   ├── models/        # Data models
│   │   ├── routers/       # API endpoints
│   │   └── services/      # Business logic
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── app/           # Next.js app directory
│   │   └── components/    # React components
│   └── package.json
└── README.md
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## License

MIT License