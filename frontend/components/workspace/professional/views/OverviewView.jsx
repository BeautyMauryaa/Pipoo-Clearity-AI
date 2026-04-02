// src/components/workspace/professional/views/OverviewView.jsx
'use client';

import PipooSummary from '../ui/PipooSummary';

export default function OverviewView({ userData }) {
  const overviewData = {
    pipooMessage: "You're working full-time with limited focus windows. Current priority: Backend depth & execution consistency.",
    priority: {
      role: 'Backend Developer',
      goal: 'Improve current role',
      risk: 'Context switching'
    },
    todayTask: {
      title: 'Refactor API service to reduce response latency.',
      estimatedTime: '45–60 min'
    },
    workload: {
      capacityUsed: 65,
      energyWindow: '2h remaining',
      status: 'on-track'
    }
  };

  return (
    <div className="max-w-4xl space-y-6">
      {/* Pipoo Summary */}
      <PipooSummary message={overviewData.pipooMessage} />

      {/* Priority Snapshot */}
      <div className="bg-[#151A23] border border-[#1F2633] rounded-lg p-6">
        <h3 className="text-lg font-semibold text-[#E6EAF2] mb-4">Priority Snapshot</h3>
        <div className="space-y-3">
          <div className="flex justify-between">
            <span className="text-[#9AA4B2]">Role:</span>
            <span className="text-[#E6EAF2]">{overviewData.priority.role}</span>
          </div>
          <div className="flex justify-between">
            <span className="text-[#9AA4B2]">Goal:</span>
            <span className="text-[#E6EAF2]">{overviewData.priority.goal}</span>
          </div>
          <div className="flex justify-between">
            <span className="text-[#9AA4B2]">Risk:</span>
            <span className="text-[#F59E0B]">{overviewData.priority.risk}</span>
          </div>
        </div>
      </div>

      {/* Today's High-Leverage Task */}
      <div className="bg-[#151A23] border-2 border-[#4F7CFF] rounded-lg p-6">
        <h3 className="text-lg font-semibold text-[#E6EAF2] mb-2">Today's High-Leverage Task</h3>
        <p className="text-[#E6EAF2] mb-4">{overviewData.todayTask.title}</p>
        
        <div className="flex items-center gap-2 mb-4">
          <svg className="w-4 h-4 text-[#9AA4B2]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
          <span className="text-sm text-[#9AA4B2]">
            Estimated time: {overviewData.todayTask.estimatedTime}
          </span>
        </div>

        <div className="flex gap-3">
          <button className="flex-1 bg-[#4F7CFF] hover:bg-[#6B8FFF] text-white px-4 py-2.5 rounded-lg font-medium transition-colors">
            Start Task
          </button>
          <button className="px-4 py-2.5 border border-[#1F2633] text-[#9AA4B2] hover:text-[#E6EAF2] hover:border-[#4F7CFF] rounded-lg transition-colors">
            Ask Pipoo
          </button>
        </div>
      </div>

      {/* Workload Status */}
      <div className="bg-[#151A23] border border-[#1F2633] rounded-lg p-6">
        <h3 className="text-lg font-semibold text-[#E6EAF2] mb-4">Workload Status</h3>
        
        <div className="mb-4">
          <div className="flex justify-between text-sm mb-2">
            <span className="text-[#9AA4B2]">Capacity used today</span>
            <span className="text-[#E6EAF2]">{overviewData.workload.capacityUsed}%</span>
          </div>
          <div className="w-full h-2 bg-[#1F2633] rounded-full overflow-hidden">
            <div 
              className="h-full bg-[#4F7CFF]"
              style={{ width: `${overviewData.workload.capacityUsed}%` }}
            />
          </div>
        </div>

        <div className="flex justify-between items-center">
          <span className="text-[#9AA4B2]">Energy window:</span>
          <span className="text-[#E6EAF2]">{overviewData.workload.energyWindow}</span>
        </div>

        <div className="mt-4 pt-4 border-t border-[#1F2633]">
          <div className="flex items-center gap-2">
            <div className="w-2 h-2 rounded-full bg-[#22C55E]" />
            <span className="text-[#22C55E] font-medium">On track</span>
          </div>
        </div>
      </div>
    </div>
  );
}