import React from 'react';
import Button from '../ui/Button';
import SegmentedControl from '../ui/SegmentedControl';
import RadioGroup from '../ui/RadioCard';
import OptionCard from '../ui/OptionCard';
import { useOnboarding } from '@/context/OnboardingContext';
import { ArrowLeft, Calendar } from 'lucide-react';
import { useAuth } from '@/context/AuthContext';

export default function Step3Time({ data, onContinue }) {
  const { formData, updateField, prevStep } = useOnboarding();
  const { user } = useAuth();
  
  // Check if professional (has description field in timeOptions)
  const isProfessional = data.timeOptions.some(opt => opt.description !== undefined);

  return (
    <div className="bg-[#151A23] border border-[#1F2633] rounded-2xl p-12 space-y-8">
      <div className="space-y-2">
        <h2 className="text-3xl font-bold text-white">
          {data.title}
        </h2>
        {data.subtitle && (
          <p className="text-[#9AA4B2]">
            {data.subtitle}
          </p>
        )}
      </div>

      {/* Time/Schedule Selection */}
      <div className="space-y-4">
        {isProfessional ? (
          // Professional: Option cards for schedule
          <div className="space-y-4">
            {data.timeOptions.map((option) => (
              <OptionCard
                key={option.id}
                icon={Calendar}
                title={option.label}
                description={option.description}
                selected={formData.dailyTime === option.id}
                onClick={() => updateField('dailyTime', option.id)}
              />
            ))}
          </div>
        ) : (
          // Student: Segmented control
          <SegmentedControl
            options={data.timeOptions}
            selected={formData.dailyTime}
            onChange={(value) => updateField('dailyTime', value)}
          />
        )}
      </div>

      {/* Timeline/Capacity */}
      <div className="space-y-4">
        <h3 className="text-lg font-medium text-white">
          {data.timelineTitle}
        </h3>
        {isProfessional ? (
          // Professional: Segmented control for hours
          <SegmentedControl
            options={data.timelineOptions}
            selected={formData.timeline}
            onChange={(value) => updateField('timeline', value)}
          />
        ) : (
          // Student: Radio group
          <RadioGroup
            options={data.timelineOptions}
            selected={formData.timeline}
            onChange={(value) => updateField('timeline', value)}
          />
        )}
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
          disabled={!formData.dailyTime || !formData.timeline}
          className="flex-1"
        >
          Continue
        </Button>
      </div>
    </div>
  );
}