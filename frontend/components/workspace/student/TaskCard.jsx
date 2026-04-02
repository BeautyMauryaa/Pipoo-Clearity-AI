// src/components/workspace/student/TaskCard.jsx
'use client';

import { useState } from 'react';

export default function TaskCard({ task, optional = false }) {
  const [isExpanded, setIsExpanded] = useState(!optional);

  if (optional && !isExpanded) {
    return (
      <button
        onClick={() => setIsExpanded(true)}
        className="w-full bg-[#151A23] border border-[#1F2633] rounded-lg p-4 text-left hover:border-[#4F7CFF] transition-colors mb-6"
      >
        <div className="flex items-center justify-between">
          <span className="text-sm text-[#9AA4B2]">Optional task available</span>
          <svg className="w-5 h-5 text-[#9AA4B2]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
          </svg>
        </div>
      </button>
    );
  }

  return (
    <div className="bg-[#151A23] border-2 border-[#4F7CFF] rounded-lg p-6 mb-6">
      {/* Task Header */}
      <div className="flex items-start justify-between mb-4">
        <div>
          <div className="flex items-center gap-2 mb-2">
            <h3 className="text-lg font-semibold text-[#E6EAF2]">
              {optional ? "Optional Task" : "Today's One Task"}
            </h3>
            {optional && (
              <span className="px-2 py-0.5 bg-[#8B5CF6]/10 text-[#8B5CF6] text-xs rounded">
                Optional
              </span>
            )}
          </div>
          <p className="text-[#E6EAF2] leading-relaxed">
            {task.title}
          </p>
        </div>
      </div>

      {/* Time Estimate */}
      <div className="flex items-center gap-2 mb-4">
        <svg className="w-4 h-4 text-[#9AA4B2]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
        </svg>
        <span className="text-sm text-[#9AA4B2]">
          Estimated time: {task.estimatedTime}
        </span>
      </div>

      {/* Action Buttons */}
      <div className="flex gap-3">
        <button className="flex-1 bg-[#4F7CFF] hover:bg-[#6B8FFF] text-white px-4 py-2.5 rounded-lg font-medium transition-colors">
          Start Task
        </button>
        <button className="px-4 py-2.5 border border-[#1F2633] text-[#9AA4B2] hover:text-[#E6EAF2] hover:border-[#4F7CFF] rounded-lg transition-colors">
          Ask Pipoo
        </button>
      </div>

      {/* Optional: Collapse Button */}
      {optional && (
        <button
          onClick={() => setIsExpanded(false)}
          className="w-full mt-4 text-sm text-[#9AA4B2] hover:text-[#E6EAF2] transition-colors"
        >
          Hide optional task
        </button>
      )}
    </div>
  );
}