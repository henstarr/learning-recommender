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

interface RecommendationCardProps {
  recommendation: Recommendation;
}

export default function RecommendationCard({ recommendation }: RecommendationCardProps) {
  const getDifficultyColor = (difficulty: string) => {
    switch (difficulty) {
      case 'beginner': return 'bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-200';
      case 'intermediate': return 'bg-yellow-100 text-yellow-800 dark:bg-yellow-900 dark:text-yellow-200';
      case 'advanced': return 'bg-red-100 text-red-800 dark:bg-red-900 dark:text-red-200';
      default: return 'bg-gray-100 text-gray-800 dark:bg-gray-700 dark:text-gray-200';
    }
  };

  const getTypeColor = (type: string) => {
    return type === 'project' 
      ? 'bg-blue-100 text-blue-800 dark:bg-blue-900 dark:text-blue-200' 
      : 'bg-purple-100 text-purple-800 dark:bg-purple-900 dark:text-purple-200';
  };

  const getTypeIcon = (type: string) => {
    return type === 'project' ? (
      <svg className="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10" />
      </svg>
    ) : (
      <svg className="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.746 0 3.332.477 4.5 1.253v13C19.832 18.477 18.246 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
      </svg>
    );
  };

  return (
    <div className="bg-white dark:bg-gray-800 rounded-xl shadow-lg border border-gray-200 dark:border-gray-700 p-6 hover:shadow-xl hover:scale-105 transition-all duration-300 ease-in-out">
      {/* Header with job relevance */}
      {recommendation.job_relevance && (
        <div className="mb-4 p-3 bg-blue-50 dark:bg-blue-900/20 rounded-lg border-l-4 border-blue-500">
          <div className="flex items-center">
            <svg className="w-4 h-4 text-blue-600 dark:text-blue-400 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2-2v2m8 0V6a2 2 0 00-2 2H8a2 2 0 00-2-2V6m8 0h2.586a1 1 0 01.707.293l2.414 2.414a1 1 0 01.293.707V11a1 1 0 01-1 1h-4a1 1 0 01-1-1V7a1 1 0 011-1z" />
            </svg>
            <span className="text-xs font-medium text-blue-800 dark:text-blue-200">
              {recommendation.job_relevance}
              {recommendation.company && (
                <span className="ml-1 text-blue-600 dark:text-blue-300">
                  @ {recommendation.company}
                </span>
              )}
            </span>
          </div>
        </div>
      )}
      
      {/* Title and badges */}
      <div className="flex items-start justify-between mb-4">
        <h3 className="text-lg font-bold text-gray-800 dark:text-white leading-tight pr-2">
          {recommendation.title}
        </h3>
        <div className="flex flex-col sm:flex-row gap-2 flex-shrink-0">
          <span className={`px-3 py-1 rounded-full text-xs font-semibold flex items-center ${getTypeColor(recommendation.type)}`}>
            {getTypeIcon(recommendation.type)}
            {recommendation.type}
          </span>
          <span className={`px-3 py-1 rounded-full text-xs font-semibold ${getDifficultyColor(recommendation.difficulty)}`}>
            {recommendation.difficulty}
          </span>
        </div>
      </div>
      
      {/* Description */}
      <p className="text-gray-600 dark:text-gray-300 mb-6 leading-relaxed">
        {recommendation.description}
      </p>
      
      {/* Time estimation */}
      <div className="mb-6 p-3 bg-gray-50 dark:bg-gray-700 rounded-lg">
        <div className="flex items-center">
          <svg className="w-4 h-4 text-gray-600 dark:text-gray-400 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
          <span className="text-sm font-medium text-gray-700 dark:text-gray-300">
            Estimated Time:
          </span>
          <span className="text-sm text-gray-600 dark:text-gray-400 ml-1">
            {recommendation.estimated_time}
          </span>
        </div>
      </div>
      
      {/* Skills gained */}
      <div className="space-y-3">
        <h4 className="text-sm font-semibold text-gray-700 dark:text-gray-300 flex items-center">
          <svg className="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
          </svg>
          Skills You'll Gain
        </h4>
        <div className="flex flex-wrap gap-2">
          {recommendation.skills_gained && recommendation.skills_gained.map((skill, index) => (
            <span
              key={index}
              className="px-3 py-1.5 bg-gradient-to-r from-gray-100 to-gray-200 dark:from-gray-600 dark:to-gray-700 text-gray-700 dark:text-gray-200 rounded-lg text-sm font-medium hover:scale-105 transition-transform duration-200"
            >
              {skill}
            </span>
          ))}
        </div>
      </div>
    </div>
  );
}
