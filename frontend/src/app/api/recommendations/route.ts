import { NextRequest, NextResponse } from 'next/server';

export async function POST(request: NextRequest) {
  try {
    const { githubUsername, linkedinUrl } = await request.json();

    if (!githubUsername || !linkedinUrl) {
      return NextResponse.json(
        { error: 'GitHub username and LinkedIn URL are required' },
        { status: 400 }
      );
    }

    // Call the FastAPI backend
    const response = await fetch('http://localhost:8000/api/v1/recommendations/generate', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        github_username: githubUsername,
        linkedin_url: linkedinUrl,
      }),
    });

    if (!response.ok) {
      const errorText = await response.text();
      console.error('Backend error:', errorText);
      throw new Error(`Backend responded with status ${response.status}: ${errorText}`);
    }

    const data = await response.json();
    return NextResponse.json(data);
  } catch (error) {
    console.error('Error fetching recommendations:', error);
    return NextResponse.json(
      { error: 'Failed to fetch recommendations: ' + (error instanceof Error ? error.message : 'Unknown error') },
      { status: 500 }
    );
  }
}
