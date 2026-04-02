// src/components/workspace/company/views/ReportsView.jsx
'use client';

export default function ReportsView({ userData }) {
  const reportData = {
    backendRole: {
      failedLogic: '62%',
      failedConsistency: '21%',
      flaggedPlagiarism: '8%'
    },
    overallStats: {
      totalScreened: 142,
      passed: 48,
      rejected: 94,
      avgScore: 58
    }
  };

  return (
    <div className="max-w-6xl space-y-6">
      {/* Header */}
      <div>
        <h2 className="text-2xl font-semibold text-[#E6EAF2] mb-2">Reports</h2>
        <p className="text-[#9AA4B2]">Decision & audit trail</p>
      </div>

      {/* Hiring Cycle Summary */}
      <div className="bg-[#151A23] border border-[#1F2633] rounded-lg p-6">
        <h3 className="text-lg font-semibold text-[#E6EAF2] mb-4">Current Hiring Cycle</h3>
        <div className="grid grid-cols-4 gap-4">
          <div>
            <p className="text-[#9AA4B2] text-sm mb-1">Total Screened</p>
            <p className="text-2xl font-semibold text-[#E6EAF2]">{reportData.overallStats.totalScreened}</p>
          </div>
          <div>
            <p className="text-[#9AA4B2] text-sm mb-1">Passed</p>
            <p className="text-2xl font-semibold text-[#22C55E]">{reportData.overallStats.passed}</p>
          </div>
          <div>
            <p className="text-[#9AA4B2] text-sm mb-1">Rejected</p>
            <p className="text-2xl font-semibold text-[#EF4444]">{reportData.overallStats.rejected}</p>
          </div>
          <div>
            <p className="text-[#9AA4B2] text-sm mb-1">Avg Score</p>
            <p className="text-2xl font-semibold text-[#E6EAF2]">{reportData.overallStats.avgScore}</p>
          </div>
        </div>
      </div>

      {/* Role-wise Analysis */}
      <div className="bg-[#151A23] border border-[#1F2633] rounded-lg p-6">
        <h3 className="text-lg font-semibold text-[#E6EAF2] mb-4">Backend Role Analysis</h3>
        <div className="space-y-3 text-[#E6EAF2]">
          <div className="flex justify-between items-center">
            <span className="text-[#9AA4B2]">Failed logic:</span>
            <span className="font-medium">{reportData.backendRole.failedLogic}</span>
          </div>
          <div className="flex justify-between items-center">
            <span className="text-[#9AA4B2]">Failed consistency:</span>
            <span className="font-medium">{reportData.backendRole.failedConsistency}</span>
          </div>
          <div className="flex justify-between items-center">
            <span className="text-[#9AA4B2]">Flagged for plagiarism:</span>
            <span className="font-medium text-[#EF4444]">{reportData.backendRole.flaggedPlagiarism}</span>
          </div>
        </div>
      </div>

      {/* Pass/Fail Reasons */}
      <div className="bg-[#151A23] border border-[#1F2633] rounded-lg p-6">
        <h3 className="text-lg font-semibold text-[#E6EAF2] mb-4">Top Rejection Reasons</h3>
        <div className="space-y-2">
          {[
            { reason: 'Incomplete skill proof', count: 24 },
            { reason: 'Below threshold score', count: 18 },
            { reason: 'Plagiarism detected', count: 12 },
            { reason: 'Inconsistent patterns', count: 8 }
          ].map((item, index) => (
            <div 
              key={index}
              className="flex justify-between items-center p-3 bg-[#1F2633] rounded-lg"
            >
              <span className="text-[#E6EAF2]">{item.reason}</span>
              <span className="text-[#9AA4B2]">{item.count} cases</span>
            </div>
          ))}
        </div>
      </div>

      {/* Bias-free Stats */}
      <div className="bg-[#151A23] border border-[#1F2633] rounded-lg p-6">
        <h3 className="text-lg font-semibold text-[#E6EAF2] mb-4">Bias-Free Evaluation</h3>
        <p className="text-[#E6EAF2] mb-4">
          All evaluations are skill-based only. No demographic data is collected or used in scoring.
        </p>
        <div className="p-4 bg-[#1F2633] rounded-lg">
          <p className="text-sm text-[#9AA4B2]">
            Evaluation criteria: Code quality, problem-solving approach, consistency, originality
          </p>
        </div>
      </div>

      {/* Export Options */}
      <div className="flex gap-3">
        <button className="px-4 py-2 bg-[#4F7CFF] hover:bg-[#6B8FFF] text-white text-sm rounded-lg transition-colors">
          Export PDF Report
        </button>
        <button className="px-4 py-2 bg-[#1F2633] hover:bg-[#2A3441] text-[#E6EAF2] text-sm rounded-lg transition-colors">
          Export CSV Data
        </button>
      </div>
    </div>
  );
}