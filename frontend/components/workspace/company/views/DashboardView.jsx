// src/components/workspace/company/views/DashboardView.jsx
'use client';

import MetricCard from '../ui/MetricCard';
import PipooNote from '../ui/PipooNote';

export default function DashboardView({ userData }) {
  const metrics = {
    activeCandidates: 38,
    passedSkillProof: 12,
    rejected: 14,
    avgEvalTime: '18 min'
  };

  const attentionRequired = [
    { id: 1, candidate: 'Aman S.', issue: 'Incomplete skill proof', priority: 'high' },
    { id: 2, candidate: 'Priya K.', issue: 'Failed plagiarism check', priority: 'high' },
    { id: 3, candidate: 'Rohit M.', issue: 'Pending review', priority: 'medium' }
  ];

  return (
    <div className="max-w-6xl space-y-6">
      {/* Header */}
      <div>
        <h2 className="text-2xl font-semibold text-[#E6EAF2] mb-2">Dashboard</h2>
        <p className="text-[#9AA4B2]">Hiring system overview</p>
      </div>

      {/* Pipoo Summary */}
      <PipooNote 
        message="This week: 38 candidates screened. 12 passed skill proof. 6 flagged for inconsistencies."
        type="info"
      />

      {/* Key Metrics */}
      <div className="grid grid-cols-4 gap-4">
        <MetricCard 
          label="Active Candidates" 
          value={metrics.activeCandidates}
          color="default"
        />
        <MetricCard 
          label="Passed Skill Proof" 
          value={metrics.passedSkillProof}
          color="success"
        />
        <MetricCard 
          label="Rejected" 
          value={metrics.rejected}
          subtext="Reason-based"
          color="error"
        />
        <MetricCard 
          label="Avg Eval Time" 
          value={metrics.avgEvalTime}
          color="default"
        />
      </div>

      {/* Attention Required */}
      <div className="bg-[#151A23] border border-[#1F2633] rounded-lg p-6">
        <h3 className="text-lg font-semibold text-[#E6EAF2] mb-4">Attention Required</h3>
        <div className="space-y-3">
          {attentionRequired.map((item) => (
            <div 
              key={item.id}
              className="flex items-center justify-between p-3 bg-[#1F2633] rounded-lg hover:bg-[#2A3441] transition-colors"
            >
              <div className="flex items-center gap-3">
                <div className={`w-2 h-2 rounded-full ${
                  item.priority === 'high' ? 'bg-[#EF4444]' : 'bg-[#F59E0B]'
                }`} />
                <div>
                  <p className="text-[#E6EAF2] font-medium">{item.candidate}</p>
                  <p className="text-sm text-[#9AA4B2]">{item.issue}</p>
                </div>
              </div>
              <button className="text-sm text-[#4F7CFF] hover:text-[#6B8FFF] transition-colors">
                Review
              </button>
            </div>
          ))}
        </div>
      </div>

      {/* Recent Activity */}
      <div className="bg-[#151A23] border border-[#1F2633] rounded-lg p-6">
        <h3 className="text-lg font-semibold text-[#E6EAF2] mb-4">Recent Activity</h3>
        <div className="space-y-2 text-sm">
          <div className="flex justify-between text-[#9AA4B2]">
            <span>Aman S. completed Python task</span>
            <span>2 hours ago</span>
          </div>
          <div className="flex justify-between text-[#9AA4B2]">
            <span>Priya K. flagged for plagiarism</span>
            <span>4 hours ago</span>
          </div>
          <div className="flex justify-between text-[#9AA4B2]">
            <span>Rohit M. passed skill proof</span>
            <span>6 hours ago</span>
          </div>
        </div>
      </div>
    </div>
  );
}