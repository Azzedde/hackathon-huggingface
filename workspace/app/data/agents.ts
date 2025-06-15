export type Agent = {
  id: string;
  name: string;
  iconUrl: string;
  description: string;
  locked?: boolean;
};

export const agents: Agent[] = [
  {
    id: 'brainstorming',
    name: 'Office Hours Agent',
    iconUrl: '/icons/brain-process.png',
    description: 'Generates ideas using various brainstorming techniques.',
  },
  {
    id: 'analyst',
    name: 'Analyst Agent',
    iconUrl: '/icons/une-analyse.png',
    description: 'Provides thoughtful analysis and insights based on data.',
  },

  {
    id: 'technical',
    name: 'Technical Agent',
    iconUrl: '/icons/technical-service.png',
    description: 'Helps understand complex technical projects and documentation.',
  },


  {
    id: 'legal_assistant',
    name: 'Legal Assistant Agent',
    iconUrl: '/icons/document-legal.png', // Assuming a default icon for now
    description: 'Provides comprehensive legal analysis, risk evaluation, and regulatory research.',
  },
  {
    id: 'stress_test',
    name: 'Stress Test Agent',
    iconUrl: '/icons/street-market.png',
    description: 'Tests system resilience under high load conditions.',
    locked: true,
  },
  {
    id: 'hr_agent',
    name: 'HR Agent',
    iconUrl: '/icons/humanisme.png',
    description: 'Coordinates and manages multi-agent workflows.',
    locked: true,
  },
  {
    id: 'market_research',
    name: 'Market Research Agent',
    iconUrl: '/icons/street-market.png',
    description: 'Conducts in-depth research and provides data-driven insights.',
    locked: true,
  },
];