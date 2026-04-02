import React from 'react';

export default function SegmentedControl({ options, selected, onChange }) {
  return (
    <div className="inline-flex rounded-lg border border-[#1F2633] p-1 bg-[#0F1117]">
      {options.map((option) => (
        <button
          key={option.id}
          onClick={() => onChange(option.id)}
          className={`
            px-4 py-2 rounded-md text-sm font-medium transition-all duration-200
            ${selected === option.id
              ? 'bg-[#4F7CFF] text-white'
              : 'text-[#9AA4B2] hover:text-[#E6EAF2]'
            }
          `}
        >
          {option.label}
        </button>
      ))}
    </div>
  );
}