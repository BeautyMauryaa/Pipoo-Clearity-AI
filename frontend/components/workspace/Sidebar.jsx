// src/components/workspace/Sidebar.jsx
'use client';

const STUDENT_SECTIONS = [
  { id: 'overview', label: 'Overview' },
  { id: 'career', label: 'Career' },
  { id: 'focus', label: 'Focus' },
  { id: 'skillproof', label: 'Skill Proof' },
  { id: 'history', label: 'History' }
];

const PROFESSIONAL_SECTIONS = [
  { id: 'overview', label: 'Overview' },
  { id: 'direction', label: 'Direction' },
  { id: 'focus', label: 'Focus' },
  { id: 'skilledge', label: 'Skill Edge' },
  { id: 'history', label: 'History' }
];

const COMPANY_SECTIONS = [
  { id: 'dashboard', label: 'Dashboard' },
  { id: 'candidates', label: 'Candidates' },
  { id: 'reports', label: 'Reports' },
  { id: 'settings', label: 'Settings' }
];

const SECTIONS_MAP = {
  student: STUDENT_SECTIONS,
  professional: PROFESSIONAL_SECTIONS,
  company: COMPANY_SECTIONS
};

export default function Sidebar({ activeSection, onSectionChange, userRole = 'student' }) {
  const sections = SECTIONS_MAP[userRole] || STUDENT_SECTIONS;

  return (
    <aside className="w-56 bg-[#151A23] border-r border-[#1F2633] flex flex-col">
      <nav className="flex-1 px-3 py-6 space-y-1">
        {sections.map((section) => (
          <button
            key={section.id}
            onClick={() => onSectionChange(section.id)}
            className={`w-full px-4 py-2.5 rounded-lg text-left text-sm transition-colors ${
              activeSection === section.id
                ? 'bg-[#4F7CFF] text-white font-medium'
                : 'text-[#9AA4B2] hover:text-[#E6EAF2] hover:bg-[#1F2633]'
            }`}
          >
            {section.label}
          </button>
        ))}
      </nav>
    </aside>
  );
}