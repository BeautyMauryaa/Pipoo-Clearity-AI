// src/components/workspace/student/views/FocusView.jsx
'use client';

export default function FocusView({ userData }) {
  // Mock data - will be replaced with real tracking
  const focusData = {
    missedDays: 2,
    lastWeek: 'inconsistency',
    todayScope: 'reduced',
    consistencyTrend: 'improving'
  };

  return (
    <div className="max-w-4xl space-y-6">
      {/* Header */}
      <div>
        <h2 className="text-2xl font-bold text-[#E6EAF2] mb-2">Focus & Accountability</h2>
        <p className="text-[#9AA4B2]">Your execution tracker</p>
      </div>

      {/* Pipoo's Observation */}
      <div className="bg-[#151A23] border-l-4 border-[#F59E0B] rounded-lg p-6">
        <div className="flex items-start gap-4">
          <div className="flex-shrink-0 w-12 h-12 rounded-full bg-gradient-to-br from-[#4F7CFF] to-[#8B5CF6] flex items-center justify-center">
            <div className="w-10 h-10 rounded-full bg-[#151A23] flex items-center justify-center">
              <div className="text-2xl">😊</div>
            </div>
          </div>
          <div className="flex-1">
            <p className="text-[#E6EAF2] mb-3">
              You skipped {focusData.missedDays} days last week.
            </p>
            <p className="text-[#E6EAF2] mb-3">
              Reason detected: <span className="text-[#F59E0B]">{focusData.lastWeek}</span>
            </p>
            <p className="text-[#E6EAF2]">
              Today's scope <span className="text-[#4F7CFF] font-medium">reduced</span>: One 25-min task only.
            </p>
          </div>
        </div>
      </div>

      {/* Daily Check-in */}
      <div className="bg-[#151A23] border border-[#1F2633] rounded-lg p-6">
        <h3 className="text-lg font-semibold text-[#E6EAF2] mb-4">Today's Check-in</h3>
        <p className="text-[#9AA4B2] mb-4">How are you feeling about today?</p>
        
        <div className="space-y-2">
          <button className="w-full p-3 bg-[#1F2633] hover:bg-[#2A3441] rounded-lg text-left text-[#E6EAF2] transition-colors">
            Ready to focus
          </button>
          <button className="w-full p-3 bg-[#1F2633] hover:bg-[#2A3441] rounded-lg text-left text-[#E6EAF2] transition-colors">
            Feeling overwhelmed
          </button>
          <button className="w-full p-3 bg-[#1F2633] hover:bg-[#2A3441] rounded-lg text-left text-[#E6EAF2] transition-colors">
            Low energy today
          </button>
        </div>
      </div>

      {/* Missed Days Summary */}
      <div className="bg-[#151A23] border border-[#1F2633] rounded-lg p-6">
        <h3 className="text-lg font-semibold text-[#E6EAF2] mb-4">Last 7 Days</h3>
        <div className="flex gap-2">
          {['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'].map((day, index) => {
            const status = index === 1 || index === 3 ? 'missed' : 'done';
            return (
              <div key={day} className="flex-1">
                <div className={`h-16 rounded-lg flex items-center justify-center ${
                  status === 'done' ? 'bg-[#22C55E]/20 text-[#22C55E]' : 'bg-[#EF4444]/20 text-[#EF4444]'
                }`}>
                  {status === 'done' ? '✓' : '✕'}
                </div>
                <p className="text-xs text-[#9AA4B2] text-center mt-1">{day}</p>
              </div>
            );
          })}
        </div>
      </div>

      {/* Consistency Trend */}
      <div className="bg-[#151A23] border border-[#1F2633] rounded-lg p-6">
        <h3 className="text-lg font-semibold text-[#E6EAF2] mb-2">Consistency Trend</h3>
        <p className="text-[#22C55E]">Improving - Keep going</p>
      </div>
    </div>
  );
}