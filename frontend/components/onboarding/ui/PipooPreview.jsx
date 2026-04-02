import React from 'react';

export default function PipooPreview() {
  return (
    <div className="relative">
      <div className="bg-[#151A23] border border-[#1F2633] rounded-2xl p-6 shadow-2xl">
        <div className="space-y-4">
          {/* Mock Pipoo Message */}
          <div className="flex items-start gap-3">
            <div className="w-8 h-8 bg-[#4F7CFF] rounded-full flex-shrink-0"></div>
            <div className="flex-1">
              <p className="text-sm font-semibold mb-1">Pipoo</p>
              <p className="text-sm text-[#9AA4B2] leading-relaxed">
                Not let you set<br />
                Too many peoplim your seadl hiebfn?
              </p>
            </div>
          </div>
          
          {/* Mock Analysis Card */}
          <div className="bg-[#0F1117] border border-[#1F2633] rounded-lg p-4">
            <div className="flex justify-between items-center mb-3">
              <span className="text-xs font-semibold text-[#E6EAF2]">Strengths</span>
              <span className="text-xs font-semibold text-[#E6EAF2]">Requldes</span>
            </div>
            <div className="space-y-2 text-xs text-[#9AA4B2]">
              <div className="flex justify-between">
                <span>Strengtb</span>
                <span>Diango</span>
              </div>
              <div className="flex justify-between">
                <span>Delames, badsland</span>
                <span>Sulppotis The new</span>
              </div>
              <div className="flex justify-between">
                <span>unteleom tichne</span>
                <span>tofth fleaded</span>
              </div>
            </div>
          </div>
          
          {/* Typing Indicator */}
          <div className="flex items-center gap-2 text-sm text-[#6B7280]">
            <div className="w-2 h-2 bg-[#4F7CFF] rounded-full animate-pulse"></div>
            <span>Stori own imaning</span>
          </div>
        </div>
      </div>
      
      {/* Glow effect */}
      <div className="absolute inset-0 bg-[#4F7CFF] opacity-5 blur-3xl rounded-2xl -z-10"></div>
    </div>
  );
}