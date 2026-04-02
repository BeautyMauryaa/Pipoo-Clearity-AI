// src/components/workspace/company/CompanyWorkspace.jsx
'use client';

import { useState } from 'react';
import WorkspaceLayout from '../WorkspaceLayout';

// Import all view components
import DashboardView from './views/DashboardView';
import CandidatesView from './views/CandidatesView';
import SkillProofView from './views/SkillProofView';
import ReportsView from './views/ReportsView';
import HistoryView from './views/HistoryView';

export default function CompanyWorkspace({ userData }) {
  const [currentView, setCurrentView] = useState('dashboard');

  // Render current view based on state
  const renderView = () => {
    switch (currentView) {
      case 'dashboard':
        return <DashboardView userData={userData} />;
      
      case 'candidates':
        return <CandidatesView userData={userData} />;
      
      case 'skillproof':
        return <SkillProofView userData={userData} />;
      
      case 'reports':
        return <ReportsView userData={userData} />;
      
      case 'history':
        return <HistoryView userData={userData} />;
      
      default:
        return <DashboardView userData={userData} />;
    }
  };

  return (
    <WorkspaceLayout 
      userRole="company" 
      currentView={currentView} 
      onViewChange={setCurrentView}
    >
      {renderView()}
    </WorkspaceLayout>
  );
}