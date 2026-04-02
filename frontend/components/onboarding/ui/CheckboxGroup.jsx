import React from 'react';
import { Check } from 'lucide-react';

export default function CheckboxGroup({ 
  options, 
  selected, 
  onChange, 
  maxSelection = 2 
}) {
  const handleToggle = (id) => {
    if (selected.includes(id)) {
      // Remove if already selected
      onChange(selected.filter(item => item !== id));
    } else {
      // Add if not at max limit
      if (selected.length < maxSelection) {
        onChange([...selected, id]);
      }
    }
  };

  const isDisabled = (id) => {
    return !selected.includes(id) && selected.length >= maxSelection;
  };

  return (
    <div className="space-y-3">
      {options.map((option) => {
        const checked = selected.includes(option.id);
        const disabled = isDisabled(option.id);
        
        return (
          <button
            key={option.id}
            type="button"
            onClick={() => !disabled && handleToggle(option.id)}
            disabled={disabled}
            className={`
              w-full text-left p-4 rounded-lg border transition-all duration-200 flex items-center gap-3
              ${checked 
                ? 'border-[#4F7CFF] bg-[#4F7CFF]/10' 
                : disabled
                  ? 'border-[#1F2633] bg-[#0F1117] opacity-50 cursor-not-allowed'
                  : 'border-[#1F2633] bg-[#151A23] hover:border-[#4F7CFF]/50'
              }
            `}
          >
            {/* Checkbox */}
            <div className={`
              w-5 h-5 rounded border-2 flex items-center justify-center flex-shrink-0 transition-all duration-200
              ${checked 
                ? 'border-[#4F7CFF] bg-[#4F7CFF]' 
                : 'border-[#1F2633]'
              }
            `}>
              {checked && <Check className="w-3 h-3 text-white" />}
            </div>
            
            {/* Label */}
            <span className={`font-medium ${checked ? 'text-[#E6EAF2]' : 'text-[#9AA4B2]'}`}>
              {option.label}
            </span>
          </button>
        );
      })}
    </div>
  );
}