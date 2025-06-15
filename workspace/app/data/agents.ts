export type Agent = {
  id: string;
  name: string;
  iconUrl: string;
  description: string;
};

export const agents: Agent[] = [
  {
    id: 'agent-1',
    name: 'Agent Alpha',
    iconUrl: '/icons/alpha.png', // Placeholder
    description: 'Agent Alpha is good at analyzing data.',
  },
  {
    id: 'agent-2',
    name: 'Agent Beta',
    iconUrl: '/icons/beta.png', // Placeholder
    description: 'Agent Beta is skilled in natural language processing.',
  },
  {
    id: 'agent-3',
    name: 'Agent Gamma',
    iconUrl: '/icons/gamma.png', // Placeholder
    description: 'Agent Gamma specializes in image recognition.',
  },
  {
    id: 'agent-4',
    name: 'Agent Delta',
    iconUrl: '/icons/delta.png', // Placeholder
    description: 'Agent Delta is an expert in machine learning.',
  },
];