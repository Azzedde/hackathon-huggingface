'use client';

import { useState } from 'react';
import { DragDropContext, Droppable, Draggable, DropResult } from 'react-beautiful-dnd';
import { Popover, PopoverButton, PopoverPanel } from '@headlessui/react';
import { agents, Agent } from '../data/agents';

export default function AgentPlayground() {
  const [availableAgents, setAvailableAgents] = useState<Agent[]>(agents);
  const [selectedAgents, setSelectedAgents] = useState<Agent[]>([]);

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
      </div>
    </DragDropContext>
  );
}