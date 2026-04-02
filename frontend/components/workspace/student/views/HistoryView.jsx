// src/components/workspace/student/views/HistoryView.jsx
'use client';

export default function HistoryView({ userData }) {
  const history = [
    { day: 1, date: 'Dec 28', task: 'Python setup', status: 'completed' },
    { day: 2, date: 'Dec 29', task: 'Missed', status: 'missed' },
    { day: 3, date: 'Dec 30', task: 'Logic task', status: 'completed' },
    { day: 4, date: 'Today', task: 'In progress', status: 'current' }
  ];

  return (
    <div className="max-w-4xl space-y-6">
      {/* Header */}
      <div>
        <h2 className="text-2xl font-bold text-[#E6EAF2] mb-2">History</h2>
        <p className="text-[#9AA4B2]">Your journey so far</p>
      </div>

      {/* Timeline */}
      <div className="bg-[#151A23] border border-[#1F2633] rounded-lg p-6">
        <h3 className="text-lg font-semibold text-[#E6EAF2] mb-6">Activity Timeline</h3>
        <div className="space-y-4">
          {history.map((item) => (
            <div key={item.day} className="flex gap-4">
              {/* Status Icon */}
              <div className="flex flex-col items-center">
                <div className={`w-8 h-8 rounded-full flex items-center justify-center ${
                  item.status === 'completed' ? 'bg-[#22C55E]/20 text-[#22C55E]' :
                  item.status === 'missed' ? 'bg-[#EF4444]/20 text-[#EF4444]' :
                  'bg-[#4F7CFF]/20 text-[#4F7CFF]'
                }`}>
                  {item.status === 'completed' ? '✓' : 
                   item.status === 'missed' ? '✕' : 
                   '○'}
                </div>
                {item.day < history.length && (
                  <div className="w-0.5 h-full bg-[#1F2633] mt-2" />
                )}
              </div>

              {/* Content */}
              <div className="flex-1 pb-6">
                <div className="flex items-center gap-3 mb-1">
                  <span className="text-[#E6EAF2] font-medium">Day {item.day}</span>
                  <span className="text-[#9AA4B2] text-sm">{item.date}</span>
                </div>
                <p className="text-[#E6EAF2]">{item.task}</p>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Stats Summary */}
      <div className="grid grid-cols-3 gap-4">
        <div className="bg-[#151A23] border border-[#1F2633] rounded-lg p-4">
          <p className="text-[#9AA4B2] text-sm mb-1">Completed</p>
          <p className="text-2xl font-bold text-[#22C55E]">2</p>
        </div>
        <div className="bg-[#151A23] border border-[#1F2633] rounded-lg p-4">
          <p className="text-[#9AA4B2] text-sm mb-1">Missed</p>
          <p className="text-2xl font-bold text-[#EF4444]">1</p>
        </div>
        <div className="bg-[#151A23] border border-[#1F2633] rounded-lg p-4">
          <p className="text-[#9AA4B2] text-sm mb-1">Streak</p>
          <p className="text-2xl font-bold text-[#4F7CFF]">3</p>
        </div>
      </div>

      {/* Past Insights */}
      <div className="bg-[#151A23] border border-[#1F2633] rounded-lg p-6">
        <h3 className="text-lg font-semibold text-[#E6EAF2] mb-4">Past Insights from Pipoo</h3>
        <div className="space-y-4">
          <div className="p-4 bg-[#1F2633] rounded-lg">
            <p className="text-sm text-[#9AA4B2] mb-2">Day 1</p>
            <p className="text-[#E6EAF2]">Focus on building consistency first. Skills come after discipline.</p>
          </div>
          <div className="p-4 bg-[#1F2633] rounded-lg">
            <p className="text-sm text-[#9AA4B2] mb-2">Day 3</p>
            <p className="text-[#E6EAF2]">You're back on track. Small wins matter.</p>
          </div>
        </div>
      </div>
    </div>
  );
}