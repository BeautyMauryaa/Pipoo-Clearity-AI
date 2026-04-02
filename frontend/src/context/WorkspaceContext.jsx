// src/context/WorkspaceContext.jsx
'use client';

import { createContext, useContext, useState, useEffect } from 'react';
import { useAuth } from './AuthContext';

const WorkspaceContext = createContext();

export function WorkspaceProvider({ children }) {
  const { user } = useAuth();
  
  // Core workspace state
  const [role, setRole] = useState(null);
  const [activeView, setActiveView] = useState('overview');
  const [mode, setMode] = useState('career');
  const [workspaceData, setWorkspaceData] = useState(null);
  const [loading, setLoading] = useState(true);

  // Initialize workspace when user changes
  useEffect(() => {
    if (user) {
      setRole(user.role);
      setActiveView('overview'); // Reset to overview on role change
      loadWorkspaceData(user);
    } else {
      setRole(null);
      setWorkspaceData(null);
    }
    setLoading(false);
  }, [user]);

  // Load workspace data (mock for now, will be API call later)
  const loadWorkspaceData = (user) => {
    // This will be replaced with API call in Phase 2
    const mockData = {
      role: user.role,
      onboardingData: user.onboardingData || {},
      lastActive: new Date().toISOString()
    };
    setWorkspaceData(mockData);
  };

  // Change active view (sidebar click)
  const changeView = (viewId) => {
    console.log('Changing view to:', viewId);
    setActiveView(viewId);
  };

  // Change mode (topbar dropdown)
  const changeMode = (modeId) => {
    console.log('Changing mode to:', modeId);
    setMode(modeId);
  };

  // Refresh workspace data
  const refreshWorkspace = () => {
    if (user) {
      loadWorkspaceData(user);
    }
  };

  const value = {
    // State
    role,
    activeView,
    mode,
    workspaceData,
    loading,
    
    // Actions
    changeView,
    changeMode,
    refreshWorkspace,
    setActiveView,
    setMode
  };

  return (
    <WorkspaceContext.Provider value={value}>
      {children}
    </WorkspaceContext.Provider>
  );
}

export function useWorkspace() {
  const context = useContext(WorkspaceContext);
  if (!context) {
    throw new Error('useWorkspace must be used within WorkspaceProvider');
  }
  return context;
}