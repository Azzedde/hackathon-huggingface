'use client';

import { useState, useEffect } from 'react';
import { DragDropContext, Droppable, Draggable, DropResult } from 'react-beautiful-dnd';
import { Popover, PopoverButton, PopoverPanel } from '@headlessui/react';
import { agents, Agent } from '../data/agents';
import { useAppContext } from '../contexts/AppContext';

export default function AgentPlayground() {
  const { selectedAgents, setSelectedAgents, selectedBrainstormingMethod, setSelectedBrainstormingMethod } = useAppContext();
  const [availableAgents, setAvailableAgents] = useState<Agent[]>([]);
 
  useEffect(() => {
    // Initialize available agents by filtering out already selected ones
    setAvailableAgents(agents.filter(agent =>
      !selectedAgents.some(selected => selected.id === agent.id)
    ));
  }, [selectedAgents]);

  const onDragEnd = (result: DropResult) => {
    const { source, destination } = result;

    if (!destination) {
      return;
    }

    if (source.droppableId === destination.droppableId) {
      // Reordering within the same list (not needed for this basic implementation)
      return;
    }

    const sourceList = source.droppableId === 'available' ? availableAgents : selectedAgents;
    const destinationList = destination.droppableId === 'available' ? availableAgents : selectedAgents;
    const setSourceList = source.droppableId === 'available' ? setAvailableAgents : setSelectedAgents;
    const setDestinationList = destination.droppableId === 'available' ? setAvailableAgents : setSelectedAgents;

    const [movedItem] = sourceList.splice(source.index, 1);
    destinationList.splice(destination.index, 0, movedItem);

    setSourceList([...sourceList]);
    setDestinationList([...destinationList]);
  };

  return (
    <DragDropContext onDragEnd={onDragEnd}>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
        {/* Available Agents */}
        <Droppable droppableId="available" isDropDisabled={false} isCombineEnabled={false} ignoreContainerClipping={false}>
          {(provided) => (
            <div
              ref={provided.innerRef}
              {...provided.droppableProps}
              className="min-h-[300px] border border-gray-200 rounded-lg p-4 bg-gray-50 shadow-inner"
            >
              <h3 className="text-xl font-semibold mb-4 text-gray-700">Available Agents</h3>
              {availableAgents.map((agent, index) => (
                <Draggable key={agent.id} draggableId={agent.id} index={index}>
                  {(provided) => (
                    <div
                      ref={provided.innerRef}
                      {...provided.draggableProps}
                      {...provided.dragHandleProps}
                      className="flex items-center justify-between p-3 bg-white rounded-md shadow-sm mb-3 cursor-move border border-gray-200 hover:shadow-md transition-shadow"
                    >
                      <div className="flex items-center">
                        {/* Agent Icon */}
                        <img src={agent.iconUrl} alt={`${agent.name} icon`} className="w-6 h-6 rounded-full mr-3 object-cover" />
                        <span className="text-gray-800 font-medium">{agent.name}</span>
                      </div>
                      <Popover className="relative">
                        <PopoverButton className="text-gray-500 hover:text-gray-700 focus:outline-none">
                          ?
                        </PopoverButton>
                        <PopoverPanel
                          anchor="right"
                          className="max-w-52 rounded-lg border border-gray-200 bg-white bg-opacity-65 p-4 text-sm shadow-lg transition duration-200 ease-in-out [--anchor-gap:8px] data-[closed]:-translate-y-1 data-[closed]:opacity-0"
                        >
                          <div className="text-gray-700 leading-relaxed">
                            <p>{agent.description}</p>
                          </div>
                        </PopoverPanel>
                      </Popover>
                    </div>
                  )}
                </Draggable>
              ))}
              {provided.placeholder}
            </div>
          )}
        </Droppable>

        {/* Selected Agents */}
        <Droppable droppableId="selected" isDropDisabled={false} isCombineEnabled={false} ignoreContainerClipping={false}>
          {(provided) => (
            <div
              ref={provided.innerRef}
              {...provided.droppableProps}
              className="min-h-[300px] border border-gray-200 rounded-lg p-4 bg-blue-50 shadow-inner"
            >
              <h3 className="text-xl font-semibold mb-4 text-gray-700">Selected Agents</h3>
              {selectedAgents.map((agent, index) => (
                <Draggable key={agent.id} draggableId={agent.id} index={index}>
                  {(provided) => (
                    <div
                      ref={provided.innerRef}
                      {...provided.draggableProps}
                      {...provided.dragHandleProps}
                      className={`flex flex-col p-3 bg-white rounded-md shadow-sm mb-3 cursor-move border border-gray-200 hover:shadow-md transition-all duration-200 ${
                        agent.id === 'brainstorming' ? 'border-yellow-400' : ''
                      }`}
                    >
                      <div className="flex items-center justify-between">
                        <div className="flex items-center">
                          {/* Agent Icon */}
                          <img src={agent.iconUrl} alt={`${agent.name} icon`} className="w-6 h-6 rounded-full mr-3 object-cover" />
                          <span className="text-gray-800 font-medium">{agent.name}</span>
                        </div>
                        <Popover className="relative">
                          <PopoverButton className="text-gray-500 hover:text-gray-700 focus:outline-none">
                            ?
                          </PopoverButton>
                          <PopoverPanel
                            anchor="right"
                            className="max-w-52 rounded-lg border border-gray-200 bg-white bg-opacity-65 p-4 text-sm shadow-lg transition duration-200 ease-in-out [--anchor-gap:8px] data-[closed]:-translate-y-1 data-[closed]:opacity-0"
                          >
                            <div className="text-gray-700 leading-relaxed">
                              <p>{agent.description}</p>
                            </div>
                          </PopoverPanel>
                        </Popover>
                      </div>
                      {agent.id === 'brainstorming' && (
                        <div className="mt-3 animate-fadeIn">
                          <label className="block text-xs font-medium text-gray-600 mb-1">
                            Brainstorming Method:
                          </label>
                          <div className="relative">
                            <select
                              className="w-full appearance-none bg-gradient-to-r from-yellow-50 to-orange-50 border border-yellow-300 rounded-lg px-3 py-2 pr-8 text-sm text-gray-700 shadow-sm hover:border-yellow-400 focus:outline-none focus:ring-2 focus:ring-yellow-400 focus:border-transparent transition-all duration-200"
                              value={selectedBrainstormingMethod}
                              onChange={(e) => setSelectedBrainstormingMethod(e.target.value)}
                              onClick={(e) => e.stopPropagation()}
                            >
                              <option value="Starbursting">🌟 Starbursting - Question-based exploration</option>
                              <option value="Mind Mapping">🧠 Mind Mapping - Hierarchical idea expansion</option>
                              <option value="Reverse Brainstorming">🔄 Reverse Brainstorming - Problem identification</option>
                              <option value="Role Storming">🎭 Role Storming - Multiple perspectives</option>
                              <option value="SCAMPER">🔧 SCAMPER - Systematic variations</option>
                              <option value="Six Thinking Hats">🎩 Six Thinking Hats - Six viewpoints</option>
                            </select>
                            <div className="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700">
                              <svg className="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                                <path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z"/>
                              </svg>
                            </div>
                          </div>
                          <p className="mt-1 text-xs text-gray-500 italic">
                            {selectedBrainstormingMethod === 'Starbursting' && 'Uses 5W+1H questions to explore topics'}
                            {selectedBrainstormingMethod === 'Mind Mapping' && 'Expands ideas into related sub-ideas'}
                            {selectedBrainstormingMethod === 'Reverse Brainstorming' && 'Identifies potential problems and challenges'}
                            {selectedBrainstormingMethod === 'Role Storming' && 'Adopts different personas for diverse insights'}
                            {selectedBrainstormingMethod === 'SCAMPER' && 'Applies systematic creative modifications'}
                            {selectedBrainstormingMethod === 'Six Thinking Hats' && 'Analyzes from six distinct perspectives'}
                          </p>
                        </div>
                      )}
                    </div>
                  )}
                </Draggable>
              ))}
              {provided.placeholder}
            </div>
          )}
        </Droppable>
      </div>
    </DragDropContext>
  );
}