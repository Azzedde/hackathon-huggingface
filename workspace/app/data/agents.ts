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
    id: 'research',
    name: 'Research Agent',
    iconUrl: '/icons/alpha.png',
    description: 'Conducts research to find fresh insights and information.',
  },
  {
    id: 'technical',
    name: 'Technical Agent',
    iconUrl: '/icons/alpha.png',
    description: 'Helps understand complex technical projects and documentation.',
  },
  {
    id: 'legal_jurist',
    name: 'Legal Jurist Agent',
    iconUrl: '/icons/alpha.png',
    description: 'Provides legal analysis and jurisprudence insights.',
  },

];