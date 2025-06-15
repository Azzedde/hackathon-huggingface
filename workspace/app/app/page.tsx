import PromptForm from '../components/PromptForm';
import AgentPlayground from '../components/AgentPlayground';

export default function Home() {
  return (
    <div className="flex flex-col items-center min-h-screen py-12 px-4 sm:px-6 lg:px-8 bg-gray-100">
      {/* Top Zone: Text Input Form */}
      <div className="w-full max-w-2xl mb-12 bg-white p-6 rounded-lg shadow-md">
        <PromptForm />
      </div>

      {/* Bottom Zone: Drag-and-Drop Playground */}
      <div className="w-full max-w-5xl bg-white p-6 rounded-lg shadow-md">
        <AgentPlayground />
      </div>
    </div>
  );
}
