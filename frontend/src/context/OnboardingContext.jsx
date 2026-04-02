// src/context/OnboardingContext.jsx
'use client';

import { createContext, useContext, useState } from 'react';

const OnboardingContext = createContext();

export function OnboardingProvider({ children }) {
  const [currentStep, setCurrentStep] = useState(1);
  const [formData, setFormData] = useState({
    // Student/Professional fields
    goal: '',
    timeline: '',
    timePerDay: '',
    skills: [],
    interests: [],
    stage: '',
    blocker: '',
    
    // Company fields
    hiringGoal: '',
    teamSize: '',
    evaluationFocus: []
  });

  const updateField = (field, value) => {
    setFormData(prev => ({
      ...prev,
      [field]: value
    }));
  };

  const nextStep = () => {
    setCurrentStep(prev => prev + 1);
  };

  const prevStep = () => {
    setCurrentStep(prev => Math.max(1, prev - 1));
  };

  const completeOnboarding = async () => {
    try {
      console.log('=== ONBOARDING COMPLETION STARTED ===');
      console.log('formData:', formData);
      
      // Get current user from localStorage
      const storedUser = localStorage.getItem('user');
      console.log('storedUser from localStorage:', storedUser);
      
      let user;
      
      if (!storedUser) {
        console.warn('⚠️ No user found in localStorage - creating temporary user');
        
        // Create a temporary user object if none exists
        const tempUser = {
          id: Date.now().toString(),
          email: 'demo@clarity.ai',
          name: 'Demo User',
          role: 'student',
          createdAt: new Date().toISOString()
        };
        
        console.log('Created tempUser:', tempUser);
        user = tempUser;
      } else {
        user = JSON.parse(storedUser);
        console.log('Parsed existing user:', user);
      }

      // Merge onboarding data with user
      const completedUser = {
        ...user,
        onboardingData: formData,
        onboardingCompleted: true,
        isFirstDay: true,
        completedAt: new Date().toISOString()
      };

      console.log('completedUser object:', completedUser);

      // Save back to localStorage
      localStorage.setItem('user', JSON.stringify(completedUser));
      console.log('✅ Saved user to localStorage');

      // Also save to a separate userData key for workspace access
      localStorage.setItem('userData', JSON.stringify(formData));
      console.log('✅ Saved userData to localStorage');

      // Verify it was saved
      const verification = localStorage.getItem('user');
      console.log('Verification - user in localStorage:', verification);

      console.log('=== ONBOARDING COMPLETION SUCCESSFUL ===');
      return { success: true, user: completedUser };
    } catch (error) {
      console.error('❌ Onboarding completion error:', error);
      return { success: false, error: error.message || 'Failed to complete onboarding' };
    }
  };

  const resetOnboarding = () => {
    setCurrentStep(1);
    setFormData({
      goal: '',
      timeline: '',
      timePerDay: '',
      skills: [],
      interests: [],
      stage: '',
      blocker: '',
      hiringGoal: '',
      teamSize: '',
      evaluationFocus: []
    });
  };

  return (
    <OnboardingContext.Provider
      value={{
        currentStep,
        formData,
        updateField,
        nextStep,
        prevStep,
        completeOnboarding,
        resetOnboarding
      }}
    >
      {children}
    </OnboardingContext.Provider>
  );
}

export function useOnboarding() {
  const context = useContext(OnboardingContext);
  if (!context) {
    throw new Error('useOnboarding must be used within OnboardingProvider');
  }
  return context;
}