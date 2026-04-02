// import React from 'react';
// import { Home, Compass, Target, TestTube, History } from 'lucide-react';
// import { useWorkspace } from '@/context/WorkspaceContext';
// import { WORKSPACE_MODES } from '@/lib/workspaceData';

// export default function Sidebar() {
//   const { currentMode, switchMode } = useWorkspace();

//   const menuItems = [
//     { id: WORKSPACE_MODES.OVERVIEW, label: 'Overview', icon: Home },
//     { id: WORKSPACE_MODES.CAREER, label: 'Career', icon: Compass },
//     { id: WORKSPACE_MODES.FOCUS, label: 'Focus', icon: Target },
//     { id: WORKSPACE_MODES.SKILL_PROOF, label: 'Skill Proof', icon: TestTube },
//     { id: WORKSPACE_MODES.HISTORY, label: 'History', icon: History }
//   ];

//   return (
//     <div className="w-64 bg-[#0F1117] border-r border-[#1F2633] flex flex-col">
//       <nav className="flex-1 p-4 space-y-2">
//         {menuItems.map((item) => {
//           const Icon = item.icon;
//           const isActive = currentMode === item.id;

//           return (
//             <button
//               key={item.id}
//               onClick={() => switchMode(item.id)}
//               className={`
//                 w-full flex items-center gap-3 px-4 py-3 rounded-lg transition-all duration-200
//                 ${isActive
//                   ? 'bg-[#4F7CFF]/10 text-[#4F7CFF] border border-[#4F7CFF]'
//                   : 'text-[#9AA4B2] hover:bg-[#151A23] hover:text-[#E6EAF2]'
//                 }
//               `}
//             >
//               <Icon className="w-5 h-5" />
//               <span className="font-medium">{item.label}</span>
//             </button>
//           );
//         })}
//       </nav>
//     </div>
//   );
// }


// src/components/workspace/FocusBar.jsx
'use client';

export default function FocusBar({ userRole = 'student' }) {
  // Mock data - will be replaced with real context data
  const focusData = {
    status: 'on-track', // 'on-track' | 'at-risk' | 'needs-attention'
    streak: 3,
    todayProgress: 'Not started' // 'Not started' | 'In progress' | 'Completed'
  };

  const statusConfig = {
    'on-track': {
      color: 'text-[#22C55E]',
      bg: 'bg-[#22C55E]/10',
      icon: '🟢',
      label: 'On track'
    },
    'at-risk': {
      color: 'text-[#F59E0B]',
      bg: 'bg-[#F59E0B]/10',
      icon: '🟡',
      label: 'At risk'
    },
    'needs-attention': {
      color: 'text-[#EF4444]',
      bg: 'bg-[#EF4444]/10',
      icon: '🔴',
      label: 'Needs attention'
    }
  };

  const currentStatus = statusConfig[focusData.status];

  return (
    <div className="h-14 bg-[#151A23] border-t border-[#1F2633] flex items-center justify-between px-6">
      {/* Left: Focus Status */}
      <div className="flex items-center gap-4">
        <div className={`flex items-center gap-2 px-3 py-1.5 rounded-full ${currentStatus.bg}`}>
          <span className="text-sm">{currentStatus.icon}</span>
          <span className={`text-sm font-medium ${currentStatus.color}`}>
            {currentStatus.label}
          </span>
        </div>

        {/* Streak */}
        <div className="flex items-center gap-2 text-[#9AA4B2]">
          <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17.657 18.657A8 8 0 016.343 7.343S7 9 9 10c0-2 .5-5 2.986-7C14 5 16.09 5.777 17.656 7.343A7.975 7.975 0 0120 13a7.975 7.975 0 01-2.343 5.657z" />
          </svg>
          <span className="text-sm">Day {focusData.streak}</span>
        </div>
      </div>

      {/* Right: Today's Progress */}
      <div className="flex items-center gap-2">
        <span className="text-sm text-[#9AA4B2]">Today:</span>
        <span className="text-sm text-[#E6EAF2] font-medium">
          {focusData.todayProgress}
        </span>
      </div>
    </div>
  );
}