// src/components/workspace/student/StudentWorkspace.jsx
'use client';

import { useState, useEffect } from 'react';
import { getFirstDayWorkspace } from '@/lib/workspaceData';
import WorkspaceLayout from '../WorkspaceLayout';

// Import all view components
import OverviewView from './views/OverviewView';
import CareerView from './views/CareerView';
import FocusView from './views/FocusView';
import SkillProofView from './views/SkillProofView';
import HistoryView from './views/HistoryView';

export default function StudentWorkspace({ userData }) {
  const [currentView, setCurrentView] = useState('overview');
  const [workspaceData, setWorkspaceData] = useState(null);

  useEffect(() => {
    if (userData) {
      const data = getFirstDayWorkspace(userData);
      setWorkspaceData(data);
    }
  }, [userData]);

  if (!workspaceData) {
    return (
      <WorkspaceLayout userRole="student" currentView={currentView} onViewChange={setCurrentView}>
        <div className="flex items-center justify-center py-12">
          <div className="text-[#9AA4B2]">Loading your workspace...</div>
        </div>
      </WorkspaceLayout>
    );
  }

  const isFirstDay = workspaceData.isFirstDay;

  // Render current view based on state
  const renderView = () => {
    switch (currentView) {
      case 'overview':
        return <OverviewView workspaceData={workspaceData} isFirstDay={isFirstDay} />;
      
      case 'career':
        return <CareerView userData={userData} />;
      
      case 'focus':
        return <FocusView userData={userData} />;
      
      case 'skillproof':
        return <SkillProofView userData={userData} />;
      
      case 'history':
        return <HistoryView userData={userData} />;
      
      default:
        return <OverviewView workspaceData={workspaceData} isFirstDay={isFirstDay} />;
    }
  };

  return (
    <WorkspaceLayout 
      userRole="student" 
      currentView={currentView} 
      onViewChange={setCurrentView}
    >
      {renderView()}
    </WorkspaceLayout>
  );
}