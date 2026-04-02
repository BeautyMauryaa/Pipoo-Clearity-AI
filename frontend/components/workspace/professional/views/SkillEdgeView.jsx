// src/components/workspace/professional/views/SkillEdgeView.jsx
'use client';

export default function SkillEdgeView({ userData }) {
  const skillTracks = [
    { 
      name: 'Backend System Design', 
      depthLevel: 'Intermediate', 
      nextTask: 'Design a scalable queue system (conceptual)'
    },
    { 
      name: 'Performance Optimization', 
      depthLevel: 'Beginner', 
      nextTask: 'Profile and optimize API response times'
    }
  ];

  return (
    <div className="max-w-4xl space-y-6">
      {/* Header */}
      <div>
        <h2 className="text-2xl font-semibold text-[#E6EAF2] mb-2">Skill Edge</h2>
        <p className="text-[#9AA4B2]">Maintain professional relevance</p>
      </div>

      {/* Active Skill Tracks */}
      <div className="bg-[#151A23] border border-[#1F2633] rounded-lg p-6">
        <h3 className="text-lg font-semibold text-[#E6EAF2] mb-4">Active Skill Tracks</h3>
        <div className="space-y-4">
          {skillTracks.map((track, index) => (
            <div key={index} className="p-4 bg-[#1F2633] rounded-lg">
              <div className="flex justify-between items-start mb-3">
                <h4 className="text-[#E6EAF2] font-medium">{track.name}</h4>
                <span className="text-xs px-2 py-1 bg-[#4F7CFF]/20 text-[#4F7CFF] rounded">
                  {track.depthLevel}
                </span>
              </div>
              <div>
                <p className="text-sm text-[#9AA4B2] mb-2">Next edge task:</p>
                <p className="text-[#E6EAF2]">{track.nextTask}</p>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Skill Edge Tasks */}
      <div className="bg-[#151A23] border border-[#1F2633] rounded-lg p-6">
        <h3 className="text-lg font-semibold text-[#E6EAF2] mb-2">Optional High-Impact Tasks</h3>
        <p className="text-sm text-[#9AA4B2] mb-4">
          Non-daily tasks that deepen expertise
        </p>
        
        <div className="space-y-3">
          <div className="p-4 bg-[#1F2633] rounded-lg hover:bg-[#2A3441] transition-colors cursor-pointer">
            <h4 className="text-[#E6EAF2] font-medium mb-2">
              Design a scalable queue system
            </h4>
            <p className="text-sm text-[#9AA4B2] mb-3">
              Conceptual exercise to strengthen system design thinking
            </p>
            <button className="text-sm text-[#4F7CFF] hover:text-[#6B8FFF] transition-colors">
              Start Task →
            </button>
          </div>

          <div className="p-4 bg-[#1F2633] rounded-lg hover:bg-[#2A3441] transition-colors cursor-pointer">
            <h4 className="text-[#E6EAF2] font-medium mb-2">
              Analyze production performance bottleneck
            </h4>
            <p className="text-sm text-[#9AA4B2] mb-3">
              Real-world profiling and optimization challenge
            </p>
            <button className="text-sm text-[#4F7CFF] hover:text-[#6B8FFF] transition-colors">
              Start Task →
            </button>
          </div>
        </div>
      </div>

      {/* Credibility Signals */}
      <div className="bg-[#151A23] border border-[#1F2633] rounded-lg p-6">
        <h3 className="text-lg font-semibold text-[#E6EAF2] mb-4">Credibility Signals</h3>
        <div className="space-y-3">
          <div className="flex justify-between items-center">
            <span className="text-[#9AA4B2]">Skill depth trend:</span>
            <span className="text-[#22C55E]">Improving</span>
          </div>
          <div className="flex justify-between items-center">
            <span className="text-[#9AA4B2]">Consistency trend:</span>
            <span className="text-[#22C55E]">Stable</span>
          </div>
        </div>
        <p className="text-sm text-[#9AA4B2] mt-4">
          No scores. No gamification. Just directional signals.
        </p>
      </div>
    </div>
  );
}