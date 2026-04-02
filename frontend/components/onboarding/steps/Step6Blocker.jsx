// src/components/onboarding/steps/Step6Blocker.jsx
'use client';

import React from 'react';
import Button from '../ui/Button';
import RadioGroup from '../ui/RadioCard';
import { useOnboarding } from '@/context/OnboardingContext';
import { AlertCircle, ArrowLeft } from 'lucide-react';

export default function Step6Blocker({ data, onComplete }) {
  const { formData, updateField, prevStep } = useOnboarding();

  const handleComplete = () => {
    // Set default blocker if none selected and options exist
    if (!formData.blocker && data?.options?.length > 0) {
      updateField('blocker', data.options[0].value);
    }
    
    // Call the completion handler
    if (onComplete) {
      onComplete();
    }
  };

  // Safety check - if no data, show error state
  if (!data) {
    return (
      <div className="bg-[#151A23] border border-[#1F2633] rounded-2xl p-12 space-y-8">
        <p className="text-[#EF4444]">Blocker step configuration missing</p>
      </div>
    );
  }

  return (
    <div className="bg-[#151A23] border border-[#1F2633] rounded-2xl p-12 space-y-8">
      {/* Blocker Section */}
      <div className="space-y-4">
        <div className="flex items-start gap-3">
          <AlertCircle className="w-8 h-8 text-[#4F7CFF] shrink-0 mt-1" />
          <div className="flex-1">
            <h2 className="text-3xl font-bold text-white mb-2">
              {data.title || "What's blocking you?"}
            </h2>
            <p className="text-[#9AA4B2]">
              {data.subtitle || "Select your biggest challenge"}
            </p>
          </div>
        </div>
        
        {/* Blocker Options */}
        {data.options && data.options.length > 0 ? (
          <div className="mt-6">
            <RadioGroup
              options={data.options}
              selected={formData.blocker}
              onChange={(value) => updateField('blocker', value)}
            />
          </div>
        ) : (
          <p className="text-[#9AA4B2] mt-4">No blocker options available</p>
        )}
        
        {data.note && (
          <p className="text-sm text-[#6B7280] mt-4 pl-11">
            {data.note}
          </p>
        )}
      </div>

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
          disabled={!formData.blocker && data.options && data.options.length > 0}
          className="flex-1"
        >
          Enter Workspace
        </Button>
      </div>
    </div>
  );
}