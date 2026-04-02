import React from 'react';
import { Check } from 'lucide-react';

export default function RadioGroup({ options, selected, onChange }) {
  return (
    <div className="space-y-3">
      {options.map((option) => (
        <button
          key={option.id}
          onClick={() => onChange(option.id)}
          className={`
            w-full p-4 rounded-lg border text-left transition-all duration-200 flex items-center gap-3
            ${selected === option.id
              ? 'bg-[#4F7CFF]/10 border-[#4F7CFF]'
              : 'bg-[#151A23] border-[#1F2633] hover:border-[#4F7CFF]/50'
            }
          `}
        >
          <div className={`
            w-5 h-5 rounded-full border-2 flex items-center justify-center flex-shrink-0
            ${selected === option.id
              ? 'border-[#4F7CFF] bg-[#4F7CFF]'
              : 'border-[#1F2633]'
            }
          `}>
            {selected === option.id && (
              <Check className="w-3 h-3 text-white" />
            )}
          </div>
          
          <span className={`
            font-medium
            ${selected === option.id ? 'text-[#E6EAF2]' : 'text-[#9AA4B2]'}
          `}>
            {option.label}
          </span>
        </button>
      ))}
    </div>
  );
}