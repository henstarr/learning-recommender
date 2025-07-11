#!/bin/bash

# Learning Recommender - Development Setup Script

echo "🚀 Starting Learning Recommender Development Environment..."

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check prerequisites
echo "📋 Checking prerequisites..."
if ! command_exists python3; then
    echo "❌ Python 3 is not installed. Please install Python 3.8+ and try again."
    exit 1
fi

if ! command_exists npm; then
    echo "❌ Node.js/npm is not installed. Please install Node.js 18+ and try again."
    exit 1
fi

# Start backend
echo "🐍 Starting FastAPI backend..."
cd backend
if [ ! -f "requirements.txt" ]; then
    echo "❌ requirements.txt not found in backend directory"
    exit 1
fi

# Install backend dependencies if needed
echo "📦 Installing backend dependencies..."
pip install -r requirements.txt

# Start backend server in background
echo "🚀 Starting backend server on port 8000..."
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000 &
BACKEND_PID=$!

# Wait for backend to start
sleep 5

# Check if backend is running
if curl -s http://localhost:8000 > /dev/null; then
    echo "✅ Backend server is running at http://localhost:8000"
else
    echo "❌ Backend server failed to start"
    kill $BACKEND_PID 2>/dev/null
    exit 1
fi

# Start frontend
echo "⚛️ Starting Next.js frontend..."
cd ../frontend

# Install frontend dependencies if needed
echo "📦 Installing frontend dependencies..."
npm install

# Start frontend server
echo "🚀 Starting frontend server on port 3000..."
npm run dev &
FRONTEND_PID=$!

# Wait for frontend to start
sleep 10

# Check if frontend is running
if curl -s http://localhost:3000 > /dev/null; then
    echo "✅ Frontend server is running at http://localhost:3000"
else
    echo "❌ Frontend server failed to start"
    kill $BACKEND_PID $FRONTEND_PID 2>/dev/null
    exit 1
fi

echo ""
echo "🎉 Learning Recommender is now running!"
echo "📱 Frontend: http://localhost:3000"
echo "🔧 Backend API: http://localhost:8000"
echo "📚 API Docs: http://localhost:8000/docs"
echo ""
echo "💡 To stop the servers, press Ctrl+C"
echo ""

# Keep the script running
wait
