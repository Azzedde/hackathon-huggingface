'use client';

import { useForm } from 'react-hook-form';

type FormData = {
  prompt: string;
};

export default function PromptForm() {
  const { register, handleSubmit, formState: { errors } } = useForm<FormData>();

  const onSubmit = (data: FormData) => {
    console.log(data); // Replace with actual submission logic
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
          ></textarea>
          {errors.prompt && <p className="text-red-500 text-xs italic mt-2">{errors.prompt.message}</p>}
        </div>
        <div className="flex items-center justify-between">
          <button
            type="submit"
            className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
          >
            Submit
          </button>
        </div>
      </form>
    </div>
  );
}