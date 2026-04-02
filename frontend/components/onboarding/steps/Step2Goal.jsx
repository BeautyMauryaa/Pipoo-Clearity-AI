import React from 'react';
import Button from '../ui/Button';
import OptionCard from '../ui/OptionCard';
import { useOnboarding } from '@/context/OnboardingContext';
import { ArrowLeft } from 'lucide-react';

export default function Step2Goal({ data, onContinue }) {
  const { formData, updateField, prevStep, currentStep } = useOnboarding();

  const handleSelect = (goalId) => {
    updateField('goal', goalId);
  };

  return (
    <div className="bg-[#151A23] border border-[#1F2633] rounded-2xl p-12 space-y-8">
      <div className="space-y-2">
        <h2 className="text-3xl font-bold text-white">
          {data.title}
        </h2>
      </div>

      <div className="space-y-4">
        {data.options.map((option) => (
          <OptionCard
            key={option.id}
            icon={option.icon}
            title={option.title}
            description={option.description}
            selected={formData.goal === option.id}
            onClick={() => handleSelect(option.id)}
          />
        ))}
      </div>

      <div className="flex gap-4">
        {currentStep > 1 && (
          <Button
            variant="secondary"
            size="lg"
            onClick={prevStep}
            className="w-auto"
          >
            <ArrowLeft className="w-5 h-5 mr-2" />
            Back
          </Button>
        )}
        <Button
          variant="primary"
          size="lg"
          onClick={onContinue}
          disabled={!formData.goal}
          className="flex-1"
        >
          Continue
        </Button>
      </div>
    </div>
  );
}