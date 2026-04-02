// src/components/workspace/professional/ProfessionalWorkspace.jsx
'use client';

import { useState } from 'react';
import WorkspaceLayout from '../WorkspaceLayout';

// Import all view components
import OverviewView from './views/OverviewView';
import DirectionView from './views/DirectionView';
import FocusView from './views/FocusView';
import SkillEdgeView from './views/SkillEdgeView';
import HistoryView from './views/HistoryView';

export default function ProfessionalWorkspace({ userData }) {
  const [currentView, setCurrentView] = useState('overview');

  // Render current view based on state
  const renderView = () => {
    switch (currentView) {
      case 'overview':
        return <OverviewView userData={userData} />;
      
      case 'direction':
        return <DirectionView userData={userData} />;
      
      case 'focus':
        return <FocusView userData={userData} />;
      
      case 'skilledge':
        return <SkillEdgeView userData={userData} />;
      
      case 'history':
        return <HistoryView userData={userData} />;
      
      default:
        return <OverviewView userData={userData} />;
    }
  };

  return (
    <WorkspaceLayout 
      userRole="professional" 
      currentView={currentView} 
      onViewChange={setCurrentView}
    >
      {renderView()}
    </WorkspaceLayout>
  );
}