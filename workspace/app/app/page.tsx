import PromptForm from '../components/PromptForm';
import AgentPlayground from '../components/AgentPlayground';

export default function Home() {
  return (
    <div className="relative min-h-screen bg-gray-100">
      {/* Sticky Header */}
      <header className="sticky top-0 z-10 w-full bg-white shadow-sm border-b border-yellow-400">
        <div className="container mx-auto px-4 sm:px-6 lg:px-8 py-3 flex items-center">
          {/* Hugging Face Logo */}
          <img src="/huggingface-logo.svg" alt="Hugging Face Logo" className="h-8" />
          {/* Right side is clean */}
        </div>
      </header>

      {/* Main Content */}
      <main className="flex flex-col items-center py-12 px-4 sm:px-6 lg:px-8 bg-gradient-to-b from-gray-100 to-gray-200">
        {/* Layout for Introduction, Combos, and Prompt Form */}
        <div className="w-full max-w-5xl mb-12 flex flex-col lg:flex-row gap-8">
          {/* Introduction Section (Left) */}
          <div className="w-full lg:w-1/2 bg-white p-8 rounded-lg shadow-xl text-gray-800">
            <h1 className="text-3xl font-bold text-yellow-600 mb-4">Welcome to the Agent Playground!</h1>
            <p className="text-base text-gray-700 leading-relaxed">
              Unlock the full potential of our platform by combining different agents to achieve powerful results. This playground allows you to experiment with various agent configurations and see how they interact to process your prompts.
            </p>
            <p className="text-base text-gray-700 mt-4 leading-relaxed">
              Drag and drop agents below to build your custom workflow and hit 'Run' to see the magic happen!
            </p>
          </div>

          {/* Combos Section (Right) */}
          <div className="w-full lg:w-1/2 bg-white p-8 rounded-lg shadow-xl text-gray-800">
            <h2 className="text-3xl font-bold text-yellow-600 mb-4">Suggested Combos</h2>
            <ul className="list-disc list-inside space-y-2 text-gray-700 text-base">
              <li>Use the <strong className="text-yellow-700">brainstorming agent</strong> alone if you want to think freely and generate ideas.</li>
              <li>Combine <strong className="text-yellow-700">analyst + research agent</strong> for thoughtful, fresh insights based on data.</li>
              <li>Pair <strong className="text-yellow-700">technical + research agent</strong> to quickly understand complex projects or technical documentation.</li>
              <li>For full potential and very deep insightful dives, use <strong className="text-yellow-700">research + analyst + (technical agent or legal jurist agent)</strong>.</li>
              <li>Use <strong className="text-yellow-700">brainstorming + research agent</strong> for very thoughtful and well-researched idea generation.</li>
            </ul>
          </div>
        </div>

        {/* Top Zone: Text Input Form */}
        <div className="w-full max-w-2xl mb-12 bg-white p-6 rounded-lg shadow-md">
          <PromptForm />
        </div>

        {/* Bottom Zone: Drag-and-Drop Playground */}
        <div className="w-full max-w-5xl bg-white p-6 rounded-lg shadow-md">
          <AgentPlayground />
        </div>
      </main>
    </div>
  );
}
