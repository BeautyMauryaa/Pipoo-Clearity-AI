// src/components/workspace/professional/ui/PipooSummary.jsx
'use client';

export default function PipooSummary({ message }) {
  return (
    <div className="bg-[#151A23] border border-[#1F2633] rounded-lg p-5">
      <p className="text-[#E6EAF2] leading-relaxed">
        {message}
      </p>
    </div>
  );
}