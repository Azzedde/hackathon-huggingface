'use client';

import React, { createContext, useContext, useState, ReactNode } from 'react';
import { Agent } from '../data/agents';

interface Message {
  id: string;
  role: 'system' | 'user';
  content: string;
  timestamp: Date;
}

interface Conversation {
  id: string;
  prompt: string;
  agents: Agent[];
  messages: Message[];
  createdAt: Date;
}

interface AppContextType {
  selectedAgents: Agent[];
  setSelectedAgents: (agents: Agent[]) => void;
  selectedBrainstormingMethod: string;
  setSelectedBrainstormingMethod: (method: string) => void;
  currentConversation: Conversation | null;
  setCurrentConversation: (conversation: Conversation | null) => void;
  conversations: Conversation[];
  addConversation: (conversation: Conversation) => void;
  addMessageToCurrentConversation: (message: Message) => void;
}

const AppContext = createContext<AppContextType | undefined>(undefined);

export function AppProvider({ children }: { children: ReactNode }) {
  const [selectedAgents, setSelectedAgents] = useState<Agent[]>([]);
  const [selectedBrainstormingMethod, setSelectedBrainstormingMethod] = useState<string>("Starbursting"); // Default method
  const [currentConversation, setCurrentConversation] = useState<Conversation | null>(null);
  const [conversations, setConversations] = useState<Conversation[]>([]);

  const addConversation = (conversation: Conversation) => {
    setConversations(prev => [...prev, conversation]);
    setCurrentConversation(conversation);
  };

  const addMessageToCurrentConversation = (message: Message) => {
    if (currentConversation) {
      const updatedConversation = {
        ...currentConversation,
        messages: [...currentConversation.messages, message]
      };
      setCurrentConversation(updatedConversation);
      setConversations(prev => 
        prev.map(conv => conv.id === currentConversation.id ? updatedConversation : conv)
      );
    }
  };

  return (
    <AppContext.Provider value={{
      selectedAgents,
      setSelectedAgents,
      selectedBrainstormingMethod,
      setSelectedBrainstormingMethod,
      currentConversation,
      setCurrentConversation,
      conversations,
      addConversation,
      addMessageToCurrentConversation
    }}>
      {children}
    </AppContext.Provider>
  );
}

export function useAppContext() {
  const context = useContext(AppContext);
  if (context === undefined) {
    throw new Error('useAppContext must be used within an AppProvider');
  }
  return context;
}