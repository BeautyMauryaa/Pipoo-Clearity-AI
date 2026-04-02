// src/components/workspace/professional/views/HistoryView.jsx
'use client';

export default function HistoryView({ userData }) {
  const history = [
    { date: 'Dec 30', task: 'Refactored auth service', status: 'completed' },
    { date: 'Dec 29', task: 'Skipped focus day', status: 'missed', reason: 'Burnout' },
    { date: 'Dec 28', task: 'Completed design review', status: 'completed' },
    { date: 'Dec 27', task: 'Optimized database queries', status: 'completed' }
  ];

  const pipooDecisions = [
    { date: 'Dec 29', decision: 'Reduced scope due to context switching patterns' },
    { date: 'Dec 26', decision: 'Protected morning deep-work block' }
  ];

  return (
    <div className="max-w-4xl space-y-6">
      {/* Header */}
      <div>
        <h2 className="text-2xl font-semibold text-[#E6EAF2] mb-2">History</h2>
        <p className="text-[#9AA4B2]">Reflection & pattern awareness</p>
      </div>

      {/* Activity Timeline */}
      <div className="bg-[#151A23] border border-[#1F2633] rounded-lg p-6">
        <h3 className="text-lg font-semibold text-[#E6EAF2] mb-4">Recent Activity</h3>
        <div className="space-y-3">
          {history.map((item, index) => (
            <div 
              key={index}
              className="flex items-start gap-4 p-4 bg-[#1F2633] rounded-lg"
            >
              <div className={`w-6 h-6 rounded-full flex items-center justify-center flex-shrink-0 ${
                item.status === 'completed' ? 'bg-[#22C55E]/20 text-[#22C55E]' :
                'bg-[#EF4444]/20 text-[#EF4444]'
              }`}>
                {item.status === 'completed' ? '✓' : '✕'}
              </div>
              <div className="flex-1">
                <div className="flex justify-between items-start mb-1">
                  <p className="text-[#E6EAF2]">{item.task}</p>
                  <span className="text-sm text-[#9AA4B2]">{item.date}</span>
                </div>
                {item.reason && (
                  <p className="text-sm text-[#9AA4B2]">Reason: {item.reason}</p>
                )}
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Past Pipoo Decisions */}
      <div className="bg-[#151A23] border border-[#1F2633] rounded-lg p-6">
        <h3 className="text-lg font-semibold text-[#E6EAF2] mb-4">Past Pipoo Decisions</h3>
        <div className="space-y-3">
          {pipooDecisions.map((item, index) => (
            <div key={index} className="p-4 bg-[#1F2633] rounded-lg">
              <p className="text-sm text-[#9AA4B2] mb-2">{item.date}</p>
              <p className="text-[#E6EAF2]">{item.decision}</p>
            </div>
          ))}
        </div>
      </div>

      {/* Pattern Summary */}
      <div className="bg-[#151A23] border border-[#1F2633] rounded-lg p-6">
        <h3 className="text-lg font-semibold text-[#E6EAF2] mb-4">Pattern Summary</h3>
        <div className="space-y-3 text-[#E6EAF2]">
          <p>Your most productive days are Monday and Thursday mornings.</p>
          <p>Context switching consistently reduces output on Wednesdays.</p>
          <p>Tasks over 90 minutes lead to decreased quality and burnout risk.</p>
        </div>
      </div>

      {/* Note */}
      <div className="bg-[#151A23] border border-[#1F2633] rounded-lg p-5">
        <p className="text-sm text-[#9AA4B2]">
          This data is for self-awareness, not judgment. Use it to optimize your execution patterns.
        </p>
      </div>
    </div>
  );
}