// src/components/workspace/professional/views/DirectionView.jsx
'use client';

export default function DirectionView({ userData }) {
  const directionData = {
    summary: "Your next 90 days should prioritize depth, not expansion.",
    strengths: ['Backend APIs', 'System debugging', 'Code reviews'],
    gaps: ['Advanced system design', 'Performance tuning', 'Distributed systems'],
    avoid: ['Random AI tutorials', 'Too many side projects', 'Shallow learning']
  };

  return (
    <div className="max-w-4xl space-y-6">
      {/* Header */}
      <div>
        <h2 className="text-2xl font-semibold text-[#E6EAF2] mb-2">Direction</h2>
        <p className="text-[#9AA4B2]">Strategic clarity</p>
      </div>

      {/* Current Direction Summary */}
      <div className="bg-[#151A23] border border-[#1F2633] rounded-lg p-6">
        <h3 className="text-lg font-semibold text-[#E6EAF2] mb-3">Current Direction</h3>
        <p className="text-[#E6EAF2]">{directionData.summary}</p>
      </div>

      {/* Skill Leverage Map */}
      <div className="grid grid-cols-3 gap-4">
        {/* Strengths */}
        <div className="bg-[#151A23] border border-[#1F2633] rounded-lg p-5">
          <h4 className="text-sm font-semibold text-[#22C55E] mb-3">Strengths</h4>
          <ul className="space-y-2">
            {directionData.strengths.map((item, index) => (
              <li key={index} className="text-[#E6EAF2] text-sm">
                {item}
              </li>
            ))}
          </ul>
        </div>

        {/* Gaps */}
        <div className="bg-[#151A23] border border-[#1F2633] rounded-lg p-5">
          <h4 className="text-sm font-semibold text-[#F59E0B] mb-3">Gaps</h4>
          <ul className="space-y-2">
            {directionData.gaps.map((item, index) => (
              <li key={index} className="text-[#E6EAF2] text-sm">
                {item}
              </li>
            ))}
          </ul>
        </div>

        {/* Avoid */}
        <div className="bg-[#151A23] border border-[#1F2633] rounded-lg p-5">
          <h4 className="text-sm font-semibold text-[#EF4444] mb-3">Avoid</h4>
          <ul className="space-y-2">
            {directionData.avoid.map((item, index) => (
              <li key={index} className="text-[#E6EAF2] text-sm">
                {item}
              </li>
            ))}
          </ul>
        </div>
      </div>

      {/* 30-60 Day Direction */}
      <div className="bg-[#151A23] border border-[#1F2633] rounded-lg p-6">
        <h3 className="text-lg font-semibold text-[#E6EAF2] mb-4">30–60 Day Direction</h3>
        <div className="space-y-4">
          <div>
            <h4 className="text-sm font-medium text-[#9AA4B2] mb-2">What to deepen</h4>
            <p className="text-[#E6EAF2]">
              Backend system architecture and performance optimization. Focus on real production problems.
            </p>
          </div>
          <div>
            <h4 className="text-sm font-medium text-[#9AA4B2] mb-2">What to delay</h4>
            <p className="text-[#E6EAF2]">
              Frontend frameworks, DevOps tooling. These are secondary to your core growth path.
            </p>
          </div>
          <div>
            <h4 className="text-sm font-medium text-[#9AA4B2] mb-2">What to stop</h4>
            <p className="text-[#E6EAF2]">
              Tutorial consumption without application. Switch to building real solutions.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}