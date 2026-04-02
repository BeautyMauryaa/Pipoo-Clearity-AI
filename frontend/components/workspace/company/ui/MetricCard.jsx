// src/components/workspace/company/ui/MetricCard.jsx
'use client';

export default function MetricCard({ label, value, subtext, color = 'default' }) {
  const colors = {
    default: 'text-[#E6EAF2]',
    success: 'text-[#22C55E]',
    warning: 'text-[#F59E0B]',
    error: 'text-[#EF4444]'
  };

  return (
    <div className="bg-[#151A23] border border-[#1F2633] rounded-lg p-4">
      <p className="text-sm text-[#9AA4B2] mb-1">{label}</p>
      <p className={`text-2xl font-semibold ${colors[color]} mb-1`}>{value}</p>
      {subtext && (
        <p className="text-xs text-[#6B7280]">{subtext}</p>
      )}
    </div>
  );
}