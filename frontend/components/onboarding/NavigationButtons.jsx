import React from 'react';
import { ArrowLeft, ArrowRight } from 'lucide-react';
import Button from './ui/Button';

export default function NavigationButtons({ 
  currentStep, 
  canContinue, 
  onBack, 
  onContinue,
  isLastStep = false
}) {
  return (
    <div className="flex items-center justify-between gap-4 mt-8">
      {/* Back Button (hidden on step 1) */}
      {currentStep > 1 ? (
        <button
          type="button"
          onClick={onBack}
          className="flex items-center gap-2 px-4 py-2 text-[#9AA4B2] hover:text-[#E6EAF2] transition-colors"
        >
          <ArrowLeft className="w-4 h-4" />
          <span>Back</span>
        </button>
      ) : (
        <div /> // Empty div for spacing
      )}

      {/* Continue Button */}
      <Button
        variant="primary"
        size="md"
        onClick={onContinue}
        disabled={!canContinue}
        className="ml-auto"
      >
        {isLastStep ? 'Enter Workspace' : 'Continue'}
        {!isLastStep && <ArrowRight className="w-4 h-4 ml-2" />}
      </Button>
    </div>
  );
}