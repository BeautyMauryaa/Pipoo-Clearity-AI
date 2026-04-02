'use client';

import React from 'react';
import { OnboardingProvider } from '@/context/OnboardingContext';
import { useAuth } from '@/context/AuthContext';
import OnboardingWizard from '@/components/onboarding/OnboardingWizard';

export default function OnboardingPage() {
  const { user } = useAuth();
  
  // Get user role or default to student
  const role = user?.role || 'student';

  return (
    <OnboardingProvider>
      <OnboardingWizard role={role} />
    </OnboardingProvider>
  );
}