'use client';

import { useEffect, useState } from 'react';
import { useRouter } from 'next/navigation';
import { useAppContext } from '../../contexts/AppContext';
import ChatInterface from '../../components/ChatInterface';

export default function ResultsPage() {
  const router = useRouter();
  const { currentConversation } = useAppContext();
  const [showSummarize, setShowSummarize] = useState(false);

  useEffect(() => {
    // Redirect to home if no conversation
    if (!currentConversation) {
      router.push('/');
    }
  }, [currentConversation, router]);

  if (!currentConversation) {
    return null;
  }

  const handleBack = () => {
    router.push('/');
  };

  const handleSummarize = () => {
    setShowSummarize(true);
    // TODO: Implement summarize functionality
  };

  return (
    <div className="min-h-screen bg-gray-100">
      {/* Header */}
      <header className="sticky top-0 z-10 w-full bg-white shadow-sm border-b border-yellow-400">
        <div className="container mx-auto px-4 sm:px-6 lg:px-8 py-3 flex items-center">
          <img src="/huggingface-logo.svg" alt="Hugging Face Logo" className="h-8" />
        </div>
      </header>

      {/* Main Content */}
      <main className="container mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Prompt and Agent Info */}
        <div className="bg-white rounded-lg shadow-md p-6 mb-6">
          <h2 className="text-2xl font-bold text-gray-800 mb-4">Your Prompt</h2>
          <p className="text-gray-700 mb-4">{currentConversation.prompt}</p>
          
          <h3 className="text-lg font-semibold text-gray-800 mb-2">Selected Agents:</h3>
          <div className="flex flex-wrap gap-2 mb-6">
            {currentConversation.agents.map((agent) => (
              <div key={agent.id} className="flex items-center bg-blue-100 rounded-full px-3 py-1">
                <img src={agent.iconUrl} alt={agent.name} className="w-5 h-5 mr-2 rounded-full" />
                <span className="text-sm text-blue-800">{agent.name}</span>
              </div>
            ))}
          </div>

          {/* Action Buttons */}
          <div className="flex gap-4">
            <button
              onClick={handleBack}
              className="bg-gray-500 hover:bg-gray-600 text-white font-bold py-2 px-6 rounded focus:outline-none focus:shadow-outline"
            >
              Back
            </button>
            <button
              onClick={handleSummarize}
              className="bg-yellow-500 hover:bg-yellow-600 text-white font-bold py-2 px-6 rounded focus:outline-none focus:shadow-outline"
            >
              Summarize
            </button>
          </div>

          {showSummarize && (
            <div className="mt-4 p-4 bg-yellow-100 text-yellow-800 rounded-md">
              Summarize functionality coming soon...
            </div>
          )}
        </div>

        {/* Chat Interface */}
        <div className="bg-white rounded-lg shadow-md p-6">
          <h2 className="text-2xl font-bold text-gray-800 mb-4">Chat with Results</h2>
          <ChatInterface />
        </div>
      </main>
    </div>
  );
}