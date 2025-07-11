'use client';

import React from 'react';

export default function Footer() {
  return (
    <footer className="bg-white dark:bg-gray-900 border-t border-gray-200 dark:border-gray-700 mt-12">
      <div className="max-w-4xl mx-auto px-4 py-8">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div>
            <h3 className="text-lg font-semibold text-gray-800 dark:text-white mb-4">
              Learning Recommender
            </h3>
            <p className="text-gray-600 dark:text-gray-400 text-sm">
              Get personalized learning recommendations based on your GitHub and LinkedIn profiles.
            </p>
          </div>
          
          <div>
            <h4 className="text-md font-medium text-gray-800 dark:text-white mb-3">
              Features
            </h4>
            <ul className="space-y-2 text-sm text-gray-600 dark:text-gray-400">
              <li>• GitHub Profile Analysis</li>
              <li>• LinkedIn Integration</li>
              <li>• Job-Specific Recommendations</li>
              <li>• Skill Gap Analysis</li>
            </ul>
          </div>
          
          <div>
            <h4 className="text-md font-medium text-gray-800 dark:text-white mb-3">
              Resources
            </h4>
            <ul className="space-y-2 text-sm text-gray-600 dark:text-gray-400">
              <li>
                <a href="#" className="hover:text-blue-600 dark:hover:text-blue-400 transition-colors">
                  Documentation
                </a>
              </li>
              <li>
                <a href="#" className="hover:text-blue-600 dark:hover:text-blue-400 transition-colors">
                  Privacy Policy
                </a>
              </li>
              <li>
                <a href="#" className="hover:text-blue-600 dark:hover:text-blue-400 transition-colors">
                  Terms of Service
                </a>
              </li>
            </ul>
          </div>
        </div>
        
        <div className="border-t border-gray-200 dark:border-gray-700 mt-8 pt-6 text-center">
          <p className="text-sm text-gray-600 dark:text-gray-400">
            © 2025 Learning Recommender. Built with Next.js and FastAPI.
          </p>
        </div>
      </div>
    </footer>
  );
}
