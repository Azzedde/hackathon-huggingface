'use client';

import { useState } from 'react';
import { useForm } from 'react-hook-form';
import { useRouter } from 'next/navigation';
import { useAppContext } from '../contexts/AppContext';

type FormData = {
  prompt: string;
};

export default function PromptForm() {
  const { register, handleSubmit, formState: { errors } } = useForm<FormData>();
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);
  const [processingStep, setProcessingStep] = useState<string>('');
  const router = useRouter();
  const { selectedAgents, addConversation, selectedBrainstormingMethod } = useAppContext();

  const onSubmit = async (data: FormData) => {
    if (selectedAgents.length === 0) {
      setError('Please select at least one agent from the playground below.');
      return;
    }

    setIsLoading(true);
    setError(null);
    setProcessingStep('Initializing agents...');
    console.log('Submitting prompt:', data.prompt);
    console.log('Selected agents:', selectedAgents);
    
    const apiUrl = '/api/orchestrate';
    console.log('Fetching API route:', apiUrl);
    
    // Simulate processing steps
    setTimeout(() => setProcessingStep('Analyzing your prompt...'), 500);
    setTimeout(() => setProcessingStep(`Consulting ${selectedAgents.map(a => a.name).join(', ')}...`), 1500);
    setTimeout(() => setProcessingStep('Generating insights...'), 2500);
    
    try {
      // Prepare the request body
      const requestBody: any = {
        prompt: data.prompt,
        agents: selectedAgents.map(agent => agent.id)
      };
      
      // If brainstorming agent is selected, include the selected method
      if (selectedAgents.some(agent => agent.id === 'brainstorming')) {
        requestBody.brainstormingMethod = selectedBrainstormingMethod;
      }
      
      const apiResponse = await fetch(apiUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(requestBody),
      });
      console.log(`Received response from ${apiUrl} with status: ${apiResponse.status}`);

      if (!apiResponse.ok) {
        console.error('API response not OK.');
        try {
          const errorData = await apiResponse.json();
          console.error('API error (JSON):', errorData.error);
          setError(errorData.error || 'An unknown error occurred.');
        } catch (jsonError) {
          console.error('Failed to parse API error response as JSON.');
          const errorText = await apiResponse.text();
          console.error('API error response (Text):', errorText.substring(0, 500)); // Log first 500 chars
          setError(`API returned non-JSON error (Status: ${apiResponse.status}): ${errorText.substring(0, 100)}...`);
        }
        setIsLoading(false);
        return;
      }

      const result = await apiResponse.json();
      console.log('API response:', result);
      
      // Create a new conversation with both user prompt and system response
      const conversation = {
        id: Date.now().toString(),
        prompt: data.prompt,
        agents: selectedAgents,
        messages: [
          {
            id: '1',
            role: 'user' as const,
            content: data.prompt,
            timestamp: new Date()
          },
          {
            id: '2',
            role: 'system' as const,
            content: result.response,
            timestamp: new Date()
          }
        ],
        createdAt: new Date()
      };
      
      addConversation(conversation);
      
      // Navigate to results page
      router.push('/results');
    } catch (fetchError: any) {
      console.error('Fetch error:', fetchError);
      setError(fetchError.message || 'An error occurred while fetching.');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="p-4 max-w-xl mx-auto">
      <form onSubmit={handleSubmit(onSubmit)} className="bg-white rounded-lg shadow-md p-6">
        <div className="mb-4">
          <label htmlFor="prompt" className="block text-gray-700 text-sm font-bold mb-2">
            Enter your prompt:
          </label>
          <textarea
            id="prompt"
            rows={4}
            {...register('prompt', { required: 'Prompt is required' })}
            className={`shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline ${errors.prompt ? 'border-red-500' : ''}`}
            disabled={isLoading}
          ></textarea>
          {errors.prompt && <p className="text-red-500 text-xs italic mt-2">{errors.prompt.message}</p>}
        </div>
        <div className="flex items-center justify-between">
          <button
            type="submit"
            className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline disabled:opacity-50"
            disabled={isLoading}
          >
            {isLoading ? 'Processing...' : 'Submit'}
          </button>
        </div>
      </form>

      {isLoading && (
        <div className="mt-4 p-4 bg-blue-100 text-blue-700 rounded-md">
          <div className="flex items-center">
            <div className="animate-spin rounded-full h-5 w-5 border-b-2 border-blue-700 mr-3"></div>
            <div>
              <p className="font-semibold">Processing your request...</p>
              {processingStep && (
                <p className="text-sm mt-1 italic">{processingStep}</p>
              )}
            </div>
          </div>
        </div>
      )}

      {error && (
        <div className="mt-4 p-4 bg-red-100 text-red-700 rounded-md">
          Error: {error}
        </div>
      )}

    </div>
  );
}