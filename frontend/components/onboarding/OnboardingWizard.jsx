// src/components/onboarding/OnboardingWizard.jsx
'use client';

import React from 'react';
import { useRouter } from 'next/navigation';
import { useOnboarding } from '@/context/OnboardingContext';
import { getOnboardingData } from '@/lib/onboardingData';
import OnboardingLayout from './OnboardingLayout';
import Step1Intro from './steps/Step1Intro';
import Step2Goal from './steps/Step2Goal';
import Step3Time from './steps/Step3Time';
import Step4Skills from './steps/Step4Skills';
import Step5Stage from './steps/Step5Stage';
import { ROUTES } from '@/lib/constants';

export default function OnboardingWizard({ role = 'student' }) {
  const router = useRouter();
  const { currentStep, nextStep, completeOnboarding } = useOnboarding();
  
  const data = getOnboardingData(role);

  // Debug: Log the data structure
  console.log('OnboardingWizard role:', role);
  console.log('OnboardingWizard data:', data);
  console.log('Step 5 (stage) data:', data.stage);

  const handleComplete = async () => {
    console.log('=== WIZARD HANDLE COMPLETE CALLED ===');
    
    try {
      const result = await completeOnboarding();
      console.log('completeOnboarding result:', result);
      
      if (result.success) {
        console.log('✅ Onboarding completed successfully');
        console.log('Redirecting to workspace in 200ms...');
        
        // Force redirect after short delay
        setTimeout(() => {
          console.log('🚀 Executing redirect to:', ROUTES.WORKSPACE);
          window.location.href = '/workspace';  // Use window.location as fallback
        }, 200);
      } else {
        console.error('❌ Onboarding completion failed:', result.error);
        alert(`Failed to complete onboarding: ${result.error}`);
      }
    } catch (error) {
      console.error('❌ Error in handleComplete:', error);
      alert('An unexpected error occurred. Please try again.');
    }
  };

  const renderStep = () => {
    switch (currentStep) {
      case 1:
        return <Step1Intro data={data.intro} onContinue={nextStep} />;
      case 2:
        return <Step2Goal data={data.goal} onContinue={nextStep} />;
      case 3:
        return <Step3Time data={data.time} onContinue={nextStep} />;
      case 4:
        return <Step4Skills data={data.skills} onContinue={nextStep} />;
      case 5:
        // For company/professional: stage IS the final step, no blocker
        // For student: stage + blocker combined
        return <Step5Stage data={data.stage} onComplete={handleComplete} />;
      default:
        return <Step1Intro data={data.intro} onContinue={nextStep} />;
    }
  };

  return (
    <OnboardingLayout 
      currentStep={currentStep} 
      totalSteps={5}  // Changed from 6 to 5
      showProgress={currentStep > 1}
    >
      {renderStep()}
    </OnboardingLayout>
  );
}