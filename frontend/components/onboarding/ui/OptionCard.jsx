import React from 'react';
import { Check } from 'lucide-react';

export default function OptionCard({ 
  icon: Icon, 
  title, 
  description, 
  selected, 
  onClick 
}) {
  return (
    <button
      onClick={onClick}
      className={`
        w-full p-4 rounded-lg border text-left transition-all duration-200
        ${selected 
          ? 'bg-[#4F7CFF]/10 border-[#4F7CFF]' 
          : 'bg-[#151A23] border-[#1F2633] hover:border-[#4F7CFF]/50'
        }
      `}
    >
      <div className="flex items-start gap-3">
        {Icon && (
          <div className={`
            w-8 h-8 rounded-full flex items-center justify-center flex-shrink-0 mt-1
            ${selected ? 'bg-[#4F7CFF]/20' : 'bg-[#1F2633]'}
          `}>
            <Icon className={`w-4 h-4 ${selected ? 'text-[#4F7CFF]' : 'text-[#6B7280]'}`} />
          </div>
        )}
        
        <div className="flex-1">
          <div className="flex items-center justify-between mb-1">
            <h3 className={`font-medium ${selected ? 'text-[#E6EAF2]' : 'text-[#9AA4B2]'}`}>
              {title}
            </h3>
            {selected && (
              <Check className="w-5 h-5 text-[#4F7CFF]" />
            )}
          </div>
          <p className="text-sm text-[#6B7280]">{description}</p>
        </div>
      </div>
    </button>
  );
}