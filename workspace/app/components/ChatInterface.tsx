'use client';

import { useState, useRef, useEffect } from 'react';
import { useAppContext } from '../contexts/AppContext';

export default function ChatInterface() {
  const { currentConversation, addMessageToCurrentConversation } = useAppContext();
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [processingStep, setProcessingStep] = useState('');
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [currentConversation?.messages]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim() || !currentConversation) return;

    const userMessage = {
      id: Date.now().toString(),
      role: 'user' as const,
      content: input.trim(),
      timestamp: new Date()
    };

    // Add user message to conversation
    addMessageToCurrentConversation(userMessage);
    setInput('');
    setIsLoading(true);
    setProcessingStep('Understanding your question...');

    // Simulate processing steps
    setTimeout(() => setProcessingStep('Reviewing conversation context...'), 800);
    setTimeout(() => setProcessingStep('Formulating response...'), 1600);

    try {
      // Prepare conversation history for the orchestrator
      const conversationHistory = currentConversation.messages.map(msg => ({
        role: msg.role,
        content: msg.content
      }));

      // Add the new user message to history
      conversationHistory.push({
        role: 'user',
        content: userMessage.content
      });

      // Call the orchestrator with conversation history
      const response = await fetch('/api/orchestrate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          prompt: `Previous conversation:\n${conversationHistory.map(msg => `${msg.role}: ${msg.content}`).join('\n')}\n\nUser's follow-up request: ${userMessage.content}`,
          agents: currentConversation.agents.map(agent => agent.id),
          isFollowUp: true
        }),
      });

      if (!response.ok) {
        throw new Error('Failed to get response');
      }

      const result = await response.json();

      // Add system response to conversation
      const systemMessage = {
        id: (Date.now() + 1).toString(),
        role: 'system' as const,
        content: result.response,
        timestamp: new Date()
      };

      addMessageToCurrentConversation(systemMessage);
    } catch (error) {
      console.error('Error sending message:', error);
      // Add error message
      const errorMessage = {
        id: (Date.now() + 1).toString(),
        role: 'system' as const,
        content: 'Sorry, I encountered an error processing your request. Please try again.',
        timestamp: new Date()
      };
      addMessageToCurrentConversation(errorMessage);
    } finally {
      setIsLoading(false);
      setProcessingStep('');
    }
  };

  if (!currentConversation) return null;

  return (
    <div className="flex flex-col h-[600px]">
      {/* Messages Container */}
      <div className="flex-1 overflow-y-auto p-4 space-y-4 bg-gray-50 rounded-lg">
        {currentConversation.messages.map((message) => (
          <div
            key={message.id}
            className={`flex ${message.role === 'user' ? 'justify-end' : 'justify-start'}`}
          >
            <div
              className={`max-w-[70%] rounded-lg p-4 ${
                message.role === 'user'
                  ? 'bg-blue-500 text-white'
                  : 'bg-white border border-gray-200'
              }`}
            >
              {message.role === 'system' && (
                <div className="flex items-center mb-2">
                  <div className="w-8 h-8 bg-purple-500 rounded-full flex items-center justify-center mr-2">
                    <span className="text-white text-lg">🧠</span>
                  </div>
                  <span className="text-sm font-semibold text-gray-600">AI Assistant</span>
                </div>
              )}
              {message.role === 'user' && (
                <div className="flex items-center mb-2">
                  <div className="w-8 h-8 bg-blue-600 rounded-full flex items-center justify-center mr-2">
                    <span className="text-white text-lg">👤</span>
                  </div>
                  <span className="text-sm font-semibold text-blue-100">You</span>
                </div>
              )}
              <p className={`whitespace-pre-wrap ${message.role === 'system' ? 'text-gray-800' : 'text-white'}`}>
                {message.content}
              </p>
              <p className={`text-xs mt-2 ${message.role === 'user' ? 'text-blue-100' : 'text-gray-500'}`}>
                {new Date(message.timestamp).toLocaleTimeString()}
              </p>
            </div>
          </div>
        ))}
        {isLoading && (
          <div className="flex justify-start">
            <div className="bg-white border border-gray-200 rounded-lg p-4">
              <div>
                <div className="flex items-center">
                  <div className="w-8 h-8 bg-purple-500 rounded-full flex items-center justify-center mr-2">
                    <span className="text-white text-lg">🧠</span>
                  </div>
                  <div>
                    <span className="text-sm text-gray-600">Thinking...</span>
                    {processingStep && (
                      <p className="text-xs text-gray-500 italic mt-1">{processingStep}</p>
                    )}
                  </div>
                </div>
              </div>
            </div>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      {/* Input Form */}
      <form onSubmit={handleSubmit} className="mt-4 flex gap-2">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type your message..."
          className="flex-1 px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
          disabled={isLoading}
        />
        <button
          type="submit"
          disabled={isLoading || !input.trim()}
          className="px-6 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 disabled:opacity-50 disabled:cursor-not-allowed"
        >
          Send
        </button>
      </form>
    </div>
  );
}