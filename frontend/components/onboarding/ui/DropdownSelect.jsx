'use client';

import React, { useState } from 'react';
import { ChevronDown } from 'lucide-react';

export default function DropdownSelect({ 
  options, 
  selected, 
  onChange, 
  placeholder = "Select level" 
}) {
  const [isOpen, setIsOpen] = useState(false);
  
  const selectedOption = options.find(opt => opt.id === selected);

  return (
    <div className="relative">
      {/* Trigger Button */}
      <button
        type="button"
        onClick={() => setIsOpen(!isOpen)}
        className="w-full px-4 py-3 bg-[#0F1117] border border-[#1F2633] rounded-lg flex items-center justify-between hover:border-[#4F7CFF]/50 transition-colors"
      >
        <span className={selectedOption ? 'text-[#E6EAF2]' : 'text-[#6B7280]'}>
          {selectedOption ? selectedOption.label : placeholder}
        </span>
        <ChevronDown className={`w-5 h-5 text-[#6B7280] transition-transform ${isOpen ? 'rotate-180' : ''}`} />
      </button>

      {/* Dropdown Menu */}
      {isOpen && (
        <>
          {/* Backdrop */}
          <div 
            className="fixed inset-0 z-10" 
            onClick={() => setIsOpen(false)}
          />
          
          {/* Options */}
          <div className="absolute z-20 w-full mt-2 bg-[#151A23] border border-[#1F2633] rounded-lg shadow-2xl overflow-hidden">
            {options.map((option) => (
              <button
                key={option.id}
                type="button"
                onClick={() => {
                  onChange(option.id);
                  setIsOpen(false);
                }}
                className={`
                  w-full text-left px-4 py-3 transition-colors
                  ${selected === option.id 
                    ? 'bg-[#4F7CFF]/10 text-[#4F7CFF]' 
                    : 'text-[#9AA4B2] hover:bg-[#0F1117]'
                  }
                `}
              >
                <div className="font-medium">{option.label}</div>
                {option.description && (
                  <div className="text-xs text-[#6B7280] mt-1">
                    {option.description}
                  </div>
                )}
              </button>
            ))}
          </div>
        </>
      )}
    </div>
  );
}