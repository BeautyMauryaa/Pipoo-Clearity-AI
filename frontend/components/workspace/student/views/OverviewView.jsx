// src/components/workspace/student/views/OverviewView.jsx
'use client';

import PipooMessage from '../PipooMessage';
import InsightCard from '../InsightCard';
import TaskCard from '../TaskCard';

export default function OverviewView({ workspaceData, isFirstDay }) {
  return (
    <div className="max-w-4xl">
      {/* First Day Badge */}
      {isFirstDay && (
        <div className="mb-6 px-4 py-2 bg-[#4F7CFF]/10 border border-[#4F7CFF]/20 rounded-lg inline-block">
          <span className="text-sm text-[#4F7CFF] font-medium">Day 1 - Welcome to Clarity AI</span>
        </div>
      )}

      {/* Pipoo's First Message */}
      <PipooMessage 
        message={workspaceData.pipooMessage}
        type={isFirstDay ? 'important' : 'default'}
      />

      {/* Clarity Snapshot */}
      <InsightCard data={workspaceData.insight} />

      {/* Today's Main Task */}
      <TaskCard task={workspaceData.mainTask} />

      {/* Optional Task (Collapsed by default) */}
      <TaskCard task={workspaceData.optionalTask} optional={true} />

      {/* Empty State for Later Days */}
      {!isFirstDay && (
        <div className="mt-8 text-center">
          <p className="text-[#9AA4B2] text-sm">
            Complete today's task to see tomorrow's plan
          </p>
        </div>
      )}
    </div>
  );
}