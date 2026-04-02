// src/components/onboarding/steps/Step5Stage.jsx
'use client';

import React from 'react';
import Button from '../ui/Button';
import RadioGroup from '../ui/RadioCard';
import { useOnboarding } from '@/context/OnboardingContext';
import { AlertCircle, ArrowLeft } from 'lucide-react';

export default function Step5Stage({ data, onComplete }) {
  const { formData, updateField, prevStep } = useOnboarding();

  const handleComplete = () => {
    console.log('=== STEP 5 COMPLETE CALLED ===');
    console.log('formData.stage:', formData.stage);
    console.log('data.blockerOptions:', data.blockerOptions);
    
    // Ensure stage is selected
    if (!formData.stage) {
      console.log('No stage selected');
      return;
    }
    
    // Only check blocker if blockerOptions exist and have items
    const hasBlockerOptions = data.blockerOptions && data.blockerOptions.length > 0;
    
    if (hasBlockerOptions) {
      console.log('Blocker options exist, checking blocker selection');
      // If blocker options exist but none selected, set default
      if (!formData.blocker) {
        console.log('Setting default blocker');
        updateField('blocker', data.blockerOptions[0].id);
        // Small delay to ensure state updates
        setTimeout(() => {
          if (onComplete) {
            console.log('Calling onComplete after blocker update');
            onComplete();
          }
        }, 50);
        return;
      }
    } else {
      console.log('No blocker options, proceeding without blocker');
    }
    
    // Call completion handler
    if (onComplete) {
      console.log('Calling onComplete');
      onComplete();
    } else {
      console.log('No onComplete handler provided');
    }
  };

  return (
    <div className="bg-[#151A23] border border-[#1F2633] rounded-2xl p-12 space-y-8">
      {/* Current Stage */}
      <div className="space-y-4">
        <h2 className="text-3xl font-bold text-white">
          {data.title}
        </h2>
        
        {data.subtitle && (
          <p className="text-[#9AA4B2]">
            {data.subtitle}
          </p>
        )}
        
        <RadioGroup
          options={data.options}
          selected={formData.stage}
          onChange={(value) => updateField('stage', value)}
        />
      </div>

      {/* Blocker Section (if exists) */}
      {data.blockerTitle && (
        <div className="space-y-4 pt-8 border-t border-[#1F2633]">
          <div className="flex items-start gap-3">
            <AlertCircle className="w-6 h-6 text-[#6B7280] shrink-0 mt-1" />
            <div className="flex-1">
              <h3 className="text-xl font-bold text-white mb-2">
                {data.blockerTitle}
              </h3>
              {data.blockerSubtitle && (
                <p className="text-sm text-[#6B7280] mb-4">
                  {data.blockerSubtitle}
                </p>
              )}
            </div>
          </div>
          
          {/* Blocker Options */}
          {data.blockerOptions && data.blockerOptions.length > 0 && (
            <RadioGroup
              options={data.blockerOptions}
              selected={formData.blocker}
              onChange={(value) => updateField('blocker', value)}
            />
          )}
          
          {data.blockerNote && (
            <p className="text-sm text-[#6B7280] mt-4">
              {data.blockerNote}
            </p>
          )}
        </div>
      )}

      {/* Action Buttons */}
      <div className="flex gap-4">
        <Button
          variant="secondary"
          size="lg"
          onClick={prevStep}
          className="w-auto"
        >
          <ArrowLeft className="w-5 h-5 mr-2" />
          Back
        </Button>
        <Button
          variant="primary"
          size="lg"
          onClick={handleComplete}
          disabled={!formData.stage || (data.blockerOptions && data.blockerOptions.length > 0 && !formData.blocker)}
          className="flex-1"
        >
          Enter Workspace
        </Button>
      </div>
    </div>
  );
}