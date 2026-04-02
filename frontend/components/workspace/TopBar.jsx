// src/components/workspace/TopBar.jsx
'use client';

import { useState, useRef, useEffect } from 'react';
import Logo from '../common/Logo';

const MODES = {
  student: [
    { id: 'overview', label: 'Overview' },
    { id: 'career', label: 'Career Truth' },
    { id: 'focus', label: 'Focus & Accountability' },
    { id: 'skillproof', label: 'Skill Proof' }
  ],
  professional: [
    { id: 'overview', label: 'Overview' },
    { id: 'career', label: 'Career Clarity' },
    { id: 'focus', label: 'Daily Focus' },
    { id: 'skillproof', label: 'Skill Proof' }
  ],
  company: [
    { id: 'dashboard', label: 'Dashboard' },
    { id: 'candidates', label: 'Candidates' },
    { id: 'reports', label: 'Reports' }
  ]
};

export default function TopBar({ currentMode, onModeChange, userRole = 'student' }) {
  const [isDropdownOpen, setIsDropdownOpen] = useState(false);
  const dropdownRef = useRef(null);

  const modes = MODES[userRole] || MODES.student;
  const currentModeLabel = modes.find(m => m.id === currentMode)?.label || 'Overview';

  // Close dropdown when clicking outside
  useEffect(() => {
    function handleClickOutside(event) {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target)) {
        setIsDropdownOpen(false);
      }
    }
    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  const handleModeSelect = (modeId) => {
    onModeChange(modeId);
    setIsDropdownOpen(false);
  };

  return (
    <header className="h-16 bg-[#151A23] border-b border-[#1F2633] flex items-center justify-between px-6">
      {/* Left: Logo */}
      <div className="flex items-center gap-4">
        <Logo size="sm" />
      </div>

      {/* Center: Mode Selector */}
      <div className="relative" ref={dropdownRef}>
        <button
          onClick={() => setIsDropdownOpen(!isDropdownOpen)}
          className="flex items-center gap-2 px-4 py-2 bg-[#0F1117] border border-[#1F2633] rounded-lg text-[#E6EAF2] hover:border-[#4F7CFF] transition-colors"
        >
          <span className="text-sm font-medium">{currentModeLabel}</span>
          <svg 
            className={`w-4 h-4 transition-transform ${isDropdownOpen ? 'rotate-180' : ''}`}
            fill="none" 
            stroke="currentColor" 
            viewBox="0 0 24 24"
          >
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
          </svg>
        </button>

        {/* Dropdown Menu */}
        {isDropdownOpen && (
          <div className="absolute top-full mt-2 w-56 bg-[#151A23] border border-[#1F2633] rounded-lg shadow-lg overflow-hidden z-50">
            {modes.map((mode) => (
              <button
                key={mode.id}
                onClick={() => handleModeSelect(mode.id)}
                className={`w-full px-4 py-3 text-left text-sm transition-colors ${
                  currentMode === mode.id
                    ? 'bg-[#4F7CFF] text-white'
                    : 'text-[#E6EAF2] hover:bg-[#1F2633]'
                }`}
              >
                {mode.label}
              </button>
            ))}
          </div>
        )}
      </div>

      {/* Right: Profile */}
      <div className="flex items-center gap-3">
        <button className="w-9 h-9 rounded-full bg-[#4F7CFF] flex items-center justify-center text-white text-sm font-medium">
          P
        </button>
      </div>
    </header>
  );
}