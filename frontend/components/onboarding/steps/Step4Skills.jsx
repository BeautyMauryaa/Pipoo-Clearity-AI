import React from 'react';
import Button from '../ui/Button';
import SegmentedControl from '../ui/SegmentedControl';
import RadioGroup from '../ui/RadioCard';
import InterestChips from '../ui/InterestChips';
import { useOnboarding } from '@/context/OnboardingContext';
import { ArrowLeft } from 'lucide-react';

export default function Step4Skills({ data, onContinue }) {
  const { formData, updateField, prevStep } = useOnboarding();
  
  // Check if professional (4 level options instead of 3)
  const isProfessional = data.levelOptions.length > 3;

  return (
    <div className="bg-[#151A23] border border-[#1F2633] rounded-2xl p-12 space-y-8">
      {/* Skill/Experience Level */}
      <div className="space-y-4">
        <h2 className="text-3xl font-bold text-white">
          {data.title}
        </h2>
        {isProfessional ? (
          // Professional: Radio group for experience years
          <RadioGroup
            options={data.levelOptions}
            selected={formData.skillLevel}
            onChange={(value) => updateField('skillLevel', value)}
          />
        ) : (
          // Student: Segmented control
          <SegmentedControl
            options={data.levelOptions}
            selected={formData.skillLevel}
            onChange={(value) => updateField('skillLevel', value)}
          />
        )}
      </div>

      {/* Interest/Domain Areas */}
      <div className="space-y-4">
        <div>
          <h3 className="text-lg font-medium text-white">
            {data.interestTitle}{' '}
            {data.interestSubtitle && (
              <span className="text-[#6B7280] text-sm font-normal">
                {data.interestSubtitle}
              </span>
            )}
          </h3>
        </div>
        
        <InterestChips
          options={data.interestOptions}
          selected={formData.interests}
          onChange={(value) => updateField('interests', value)}
          maxSelection={isProfessional ? 2 : undefined}
        />
        
        <p className="text-sm text-[#6B7280]">
          {data.note}
        </p>
      </div>

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
          onClick={onContinue}
          disabled={!formData.skillLevel}
          className="flex-1"
        >
          Continue
        </Button>
      </div>
    </div>
  );
}