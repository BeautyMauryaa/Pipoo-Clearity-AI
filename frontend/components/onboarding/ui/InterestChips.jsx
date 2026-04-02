import React from 'react';
import { Check } from 'lucide-react';

export default function InterestChips({ options, selected, onChange, maxSelection }) {
  const handleToggle = (optionId) => {
    if (selected.includes(optionId)) {
      // Remove if already selected
      onChange(selected.filter(id => id !== optionId));
    } else {
      // Add if not selected (check max limit)
      if (!maxSelection || selected.length < maxSelection) {
        onChange([...selected, optionId]);
      }
    }
  };

  return (
    <div className="flex flex-wrap gap-3">
      {options.map((option) => {
        const isSelected = selected.includes(option.id);
        
        return (
          <button
            key={option.id}
            onClick={() => handleToggle(option.id)}
            className={`
              px-4 py-2 rounded-lg border text-sm font-medium transition-all duration-200 flex items-center gap-2
              ${isSelected
                ? 'bg-[#4F7CFF]/10 border-[#4F7CFF] text-[#4F7CFF]'
                : 'bg-[#151A23] border-[#1F2633] text-[#9AA4B2] hover:border-[#4F7CFF]/50'
              }
            `}
          >
            {isSelected && (
              <Check className="w-4 h-4" />
            )}
            {option.label}
          </button>
        );
      })}
    </div>
  );
}