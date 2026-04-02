import React from 'react';
import Logo from '../common/Logo';
import ProgressIndicator from './ProgressIndicator';

export default function OnboardingLayout({ children, currentStep, totalSteps, showProgress = true }) {
  return (
    <div className="min-h-screen bg-[#0F1117] text-[#E6EAF2] flex items-center justify-center px-6">
      <div className="max-w-2xl w-full">
        {/* Header */}
        <div className="flex items-center justify-between mb-8">
          <Logo className="text-xl" />
          {showProgress && (
            <ProgressIndicator current={currentStep} total={totalSteps} />
          )}
        </div>
        
        {/* Content */}
        {children}
      </div>
    </div>
  );
}