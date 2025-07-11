'use client';

import React, { useState } from 'react';
import ProfileForm from '@/components/ProfileForm';
import RecommendationCard from '@/components/RecommendationCard';
import ThemeToggle from '@/components/ThemeToggle';
import Footer from '@/components/Footer';

interface Recommendation {
  title: string;
  description: string;
  type: 'project' | 'course';
  difficulty: 'beginner' | 'intermediate' | 'advanced';
  estimated_time: string;
  skills_gained: string[];
  job_relevance?: string;
  company?: string;
}

export default function Home() {
  const [recommendations, setRecommendations] = useState<Recommendation[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (data: { githubUsername: string; linkedinUrl: string }) => {
    setIsLoading(true);
    setError(null);

    try {
      const response = await fetch('/api/recommendations', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      });

      if (!response.ok) {
        throw new Error('Failed to fetch recommendations');
      }

      const result = await response.json();
      setRecommendations(result.recommendations || []);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900 transition-colors">
      <ThemeToggle />
      
      <div className="max-w-6xl mx-auto px-4 py-8">
        {/* Header */}
        <div className="text-center mb-12">
          <h1 className="text-5xl font-bold bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent mb-4">
            Learning Recommender
          </h1>
          <p className="text-xl text-gray-600 dark:text-gray-400 max-w-2xl mx-auto">
            Get personalized learning recommendations based on your GitHub and LinkedIn profiles, 
            tailored to your career goals and current position.
          </p>
        </div>
        
        <ProfileForm onSubmit={handleSubmit} isLoading={isLoading} />
        
        {error && (
          <div className="mt-8 p-4 bg-red-50 dark:bg-red-900/20 border border-red-200 dark:border-red-800 text-red-700 dark:text-red-300 rounded-lg">
            <div className="flex items-center">
              <svg className="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              {error}
            </div>
          </div>
        )}
        
        {recommendations.length > 0 && (
          <div className="mt-12">
            <div className="text-center mb-8">
              <h2 className="text-3xl font-bold text-gray-800 dark:text-white mb-4">
                Your Personalized Learning Path
              </h2>
              <p className="text-gray-600 dark:text-gray-400">
                Based on your profile analysis, here are the recommendations to advance your career
              </p>
            </div>
            
            <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-8">
              {recommendations.map((recommendation, index) => (
                <RecommendationCard key={index} recommendation={recommendation} />
              ))}
            </div>
            
            {/* Summary section */}
            <div className="mt-12 p-6 bg-blue-50 dark:bg-blue-900/20 rounded-xl border border-blue-200 dark:border-blue-800">
              <h3 className="text-xl font-semibold text-blue-800 dark:text-blue-200 mb-3">
                📊 Learning Summary
              </h3>
              <div className="grid grid-cols-1 md:grid-cols-3 gap-4 text-sm">
                <div className="text-center">
                  <div className="text-2xl font-bold text-blue-600 dark:text-blue-400">
                    {recommendations.length}
                  </div>
                  <div className="text-gray-600 dark:text-gray-400">Total Recommendations</div>
                </div>
                <div className="text-center">
                  <div className="text-2xl font-bold text-blue-600 dark:text-blue-400">
                    {recommendations.filter(r => r.type === 'project').length}
                  </div>
                  <div className="text-gray-600 dark:text-gray-400">Projects</div>
                </div>
                <div className="text-center">
                  <div className="text-2xl font-bold text-blue-600 dark:text-blue-400">
                    {recommendations.filter(r => r.type === 'course').length}
                  </div>
                  <div className="text-gray-600 dark:text-gray-400">Courses</div>
                </div>
              </div>
            </div>
          </div>
        )}
      </div>
      
      <Footer />
    </div>
  );
}
