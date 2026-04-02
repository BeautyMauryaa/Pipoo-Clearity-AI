// src/components/workspace/WorkspaceLayout.jsx
'use client';

import { useState } from 'react';
import TopBar from './TopBar';
import Sidebar from './Sidebar';
import FocusBar from './FocusBar';

export default function WorkspaceLayout({ children, userRole, currentView, onViewChange }) {
  const [currentMode, setCurrentMode] = useState('overview');

  return (
    <div className="h-screen flex flex-col bg-[#0F1117]">
      {/* Top Bar */}
      <TopBar 
        currentMode={currentMode}
        onModeChange={setCurrentMode}
        userRole={userRole}
      />

      {/* Main Layout: Sidebar + Content */}
      <div className="flex-1 flex overflow-hidden">
        {/* Left Sidebar */}
        <Sidebar 
          activeSection={currentView}
          onSectionChange={onViewChange}
          userRole={userRole}
        />

        {/* Main Workspace Area (Pipoo Zone) */}
        <main className="flex-1 overflow-y-auto">
          <div className="max-w-5xl mx-auto p-6">
            {children}
          </div>
        </main>
      </div>

      {/* Bottom Focus Bar */}
      <FocusBar userRole={userRole} />
    </div>
  );
}