import React from 'react';
import PipooMessage from './PipooMessage';
import InsightCard from './InsightCard';
import TaskCard from './TaskCard';
import { generateFirstDayMessage, generateClaritySnapshot, generateFirstTask } from '@/lib/workspaceData';
import { useAuth } from '@/context/AuthContext';

export default function FirstDayExperience() {
  const { user } = useAuth();
  
  // Generate personalized content based on onboarding data
  const firstMessage = generateFirstDayMessage(user || {});
  const claritySnapshot = generateClaritySnapshot(user || {});
  const firstTask = generateFirstTask(user || {});

  return (
    <div className="max-w-4xl mx-auto space-y-6">
      {/* Pipoo's First Message */}
      <PipooMessage message={firstMessage} />

      {/* Clarity Snapshot */}
      <InsightCard snapshot={claritySnapshot} />

      {/* Today's Main Task */}
      <TaskCard task={firstTask} />

      {/* Optional Secondary Task (Collapsed) */}
      <details className="bg-[#151A23] border border-[#1F2633] rounded-xl p-6">
        <summary className="text-[#9AA4B2] cursor-pointer hover:text-[#E6EAF2] transition-colors">
          Optional: Secondary task (if you have time)
        </summary>
        <div className="mt-4 pt-4 border-t border-[#1F2633]">
          <p className="text-[#9AA4B2]">
            Watch a 20-minute introductory video on your chosen technology stack.
          </p>
        </div>
      </details>
    </div>
  );
}