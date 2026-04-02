// src/components/workspace/student/views/CareerView.jsx
'use client';

export default function CareerView({ userData }) {
  // Mock data - will be replaced with real analysis
  const careerData = {
    targetRole: 'Junior Backend / AI Support',
    readiness: 35,
    missing: ['Python depth', 'DSA basics', 'Git workflows'],
    stopDoing: ['Random ML tutorials', 'Too many side projects', 'Watching without coding']
  };

  return (
    <div className="max-w-4xl space-y-6">
      {/* Header */}
      <div>
        <h2 className="text-2xl font-bold text-[#E6EAF2] mb-2">Career Direction</h2>
        <p className="text-[#9AA4B2]">Honest assessment of where you stand</p>
      </div>

      {/* Role Fit Summary */}
      <div className="bg-[#151A23] border border-[#1F2633] rounded-lg p-6">
        <h3 className="text-lg font-semibold text-[#E6EAF2] mb-4">Role Fit Summary</h3>
        
        <div className="space-y-3">
          <div>
            <span className="text-[#9AA4B2]">Target role: </span>
            <span className="text-[#E6EAF2]">{careerData.targetRole}</span>
          </div>
          
          <div>
            <span className="text-[#9AA4B2]">Readiness: </span>
            <span className="text-[#E6EAF2] font-medium">{careerData.readiness}%</span>
            <div className="mt-2 w-full h-2 bg-[#1F2633] rounded-full overflow-hidden">
              <div 
                className="h-full bg-[#4F7CFF]" 
                style={{ width: `${careerData.readiness}%` }}
              />
            </div>
          </div>
        </div>
      </div>

      {/* Skill Gap */}
      <div className="bg-[#151A23] border border-[#1F2633] rounded-lg p-6">
        <h3 className="text-lg font-semibold text-[#E6EAF2] mb-4">What You're Missing</h3>
        <ul className="space-y-2">
          {careerData.missing.map((item, index) => (
            <li key={index} className="flex items-start gap-2">
              <span className="text-[#F59E0B]">•</span>
              <span className="text-[#E6EAF2]">{item}</span>
            </li>
          ))}
        </ul>
      </div>

      {/* What to Ignore */}
      <div className="bg-[#151A23] border border-[#EF4444]/20 rounded-lg p-6">
        <h3 className="text-lg font-semibold text-[#E6EAF2] mb-2">Stop Doing</h3>
        <p className="text-sm text-[#9AA4B2] mb-4">These waste your time</p>
        <ul className="space-y-2">
          {careerData.stopDoing.map((item, index) => (
            <li key={index} className="flex items-start gap-2">
              <span className="text-[#EF4444]">✕</span>
              <span className="text-[#E6EAF2]">{item}</span>
            </li>
          ))}
        </ul>
      </div>

      {/* 30-60 Day Direction */}
      <div className="bg-[#151A23] border border-[#1F2633] rounded-lg p-6">
        <h3 className="text-lg font-semibold text-[#E6EAF2] mb-4">30-60 Day Direction</h3>
        <div className="space-y-3 text-[#E6EAF2]">
          <p>Focus on Python fundamentals and build 2-3 small projects that demonstrate core skills.</p>
          <p>Learn basic DSA patterns. Skip advanced algorithms for now.</p>
          <p>Practice Git daily with real commits, not tutorials.</p>
        </div>
      </div>
    </div>
  );
}