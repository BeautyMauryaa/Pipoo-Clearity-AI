// src/components/workspace/professional/views/FocusView.jsx
'use client';

export default function FocusView({ userData }) {
  return (
    <div className="max-w-4xl space-y-6">
      {/* Header */}
      <div>
        <h2 className="text-2xl font-semibold text-[#E6EAF2] mb-2">Focus</h2>
        <p className="text-[#9AA4B2]">Execution control & burnout prevention</p>
      </div>

      {/* Focus Check-in */}
      <div className="bg-[#151A23] border border-[#1F2633] rounded-lg p-6">
        <h3 className="text-lg font-semibold text-[#E6EAF2] mb-4">Focus Check-in</h3>
        <p className="text-[#9AA4B2] mb-4">How focused were you yesterday?</p>
        
        <div className="space-y-2">
          <button className="w-full p-4 bg-[#1F2633] hover:bg-[#2A3441] rounded-lg text-left text-[#E6EAF2] transition-colors">
            Clear
          </button>
          <button className="w-full p-4 bg-[#1F2633] hover:bg-[#2A3441] rounded-lg text-left text-[#E6EAF2] transition-colors">
            Distracted
          </button>
          <button className="w-full p-4 bg-[#1F2633] hover:bg-[#2A3441] rounded-lg text-left text-[#E6EAF2] transition-colors">
            Exhausted
          </button>
        </div>
      </div>

      {/* Disruption Analysis */}
      <div className="bg-[#151A23] border-l-4 border-[#F59E0B] rounded-lg p-6">
        <h3 className="text-lg font-semibold text-[#E6EAF2] mb-3">Disruption Analysis</h3>
        <p className="text-[#E6EAF2]">
          Context switching reduced output by ~30% last week.
        </p>
      </div>

      {/* Adjusted Plan */}
      <div className="bg-[#151A23] border border-[#1F2633] rounded-lg p-6">
        <h3 className="text-lg font-semibold text-[#E6EAF2] mb-4">Adjusted Plan</h3>
        <div className="space-y-4">
          <div>
            <h4 className="text-sm font-medium text-[#9AA4B2] mb-2">Reduced scope</h4>
            <p className="text-[#E6EAF2]">
              Today's task capped at 60 minutes to prevent overload.
            </p>
          </div>
          <div>
            <h4 className="text-sm font-medium text-[#9AA4B2] mb-2">Protected deep-work blocks</h4>
            <p className="text-[#E6EAF2]">
              Morning 9-11 AM reserved for high-focus work. No meetings.
            </p>
          </div>
        </div>
      </div>

      {/* Execution Pattern */}
      <div className="bg-[#151A23] border border-[#1F2633] rounded-lg p-6">
        <h3 className="text-lg font-semibold text-[#E6EAF2] mb-4">Last 7 Days</h3>
        <div className="flex gap-2">
          {[
            { day: 'Mon', status: 'clear' },
            { day: 'Tue', status: 'clear' },
            { day: 'Wed', status: 'distracted' },
            { day: 'Thu', status: 'clear' },
            { day: 'Fri', status: 'exhausted' },
            { day: 'Sat', status: 'skip' },
            { day: 'Sun', status: 'skip' }
          ].map((item) => (
            <div key={item.day} className="flex-1">
              <div className={`h-16 rounded-lg flex items-center justify-center ${
                item.status === 'clear' ? 'bg-[#22C55E]/20 text-[#22C55E]' :
                item.status === 'distracted' ? 'bg-[#F59E0B]/20 text-[#F59E0B]' :
                item.status === 'exhausted' ? 'bg-[#EF4444]/20 text-[#EF4444]' :
                'bg-[#1F2633] text-[#9AA4B2]'
              }`}>
                {item.status === 'clear' ? '✓' : 
                 item.status === 'distracted' ? '~' :
                 item.status === 'exhausted' ? '✕' : '—'}
              </div>
              <p className="text-xs text-[#9AA4B2] text-center mt-1">{item.day}</p>
            </div>
          ))}
        </div>
      </div>

      {/* Advisory Note */}
      <div className="bg-[#151A23] border border-[#1F2633] rounded-lg p-6">
        <p className="text-[#E6EAF2]">
          Your output drops when tasks exceed 90 minutes. We'll cap deep work at 60 minutes.
        </p>
      </div>
    </div>
  );
}