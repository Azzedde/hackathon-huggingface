export type Agent = {
  id: string;
  name: string;
  iconUrl: string;
  description: string;
};

export const agents: Agent[] = [
  {
    id: 'brainstorming',
    name: 'Brainstorming Agent',
    iconUrl: '/icons/alpha.png',
    description: 'Generates ideas using various brainstorming techniques.',
  },
  {
    id: 'analyst',
    name: 'Analyst Agent',
    iconUrl: '/icons/alpha.png',
    description: 'Provides thoughtful analysis and insights based on data.',
  },

  {
    id: 'technical',
    name: 'Technical Agent',
    iconUrl: '/icons/alpha.png',
    description: 'Helps understand complex technical projects and documentation.',
  },


  {
    id: 'legal_assistant',
    name: 'Legal Assistant Agent',
    iconUrl: '/icons/alpha.png', // Assuming a default icon for now
    description: 'Provides comprehensive legal analysis, risk evaluation, and regulatory research.',
  },
];