// src/components/workspace/student/InsightCard.jsx
'use client';

export default function InsightCard({ data }) {
  return (
    <div className="bg-[#151A23] border border-[#1F2633] rounded-lg p-6 mb-6">
      {/* Card Title */}
      <h3 className="text-lg font-semibold text-[#E6EAF2] mb-4">
        Your Current Position
      </h3>

      {/* Insight Grid */}
      <div className="grid grid-cols-2 gap-4 mb-4">
        <div>
          <span className="text-sm text-[#9AA4B2]">Skill Level</span>
          <p className="text-[#E6EAF2] font-medium mt-1">{data.skillLevel}</p>
        </div>

        <div>
          <span className="text-sm text-[#9AA4B2]">Interests</span>
          <p className="text-[#E6EAF2] font-medium mt-1">{data.interests}</p>
        </div>

        <div>
          <span className="text-sm text-[#9AA4B2]">Stage</span>
          <p className="text-[#E6EAF2] font-medium mt-1">{data.stage}</p>
        </div>

        <div>
          <span className="text-sm text-[#9AA4B2]">Focus Risk</span>
          <p className="text-[#E6EAF2] font-medium mt-1">{data.focusRisk}</p>
        </div>
      </div>

      {/* CTA */}
      <button className="text-sm text-[#4F7CFF] hover:text-[#6B8FFF] transition-colors">
        View detailed analysis →
      </button>
    </div>
  );
}