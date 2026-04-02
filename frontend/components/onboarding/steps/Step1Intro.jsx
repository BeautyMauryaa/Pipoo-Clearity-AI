import React from 'react';
import Button from '../ui/Button';

export default function Step1Intro({ data, onContinue, onBack }) {
  return (
    <div className="bg-[#151A23] border border-[#1F2633] rounded-2xl p-12 space-y-8">
      <div className="space-y-4">
        <h1 className="text-3xl font-bold text-white">
          {data.title}
        </h1>
        <p className="text-lg text-[#9AA4B2]">
          {data.subtitle}
        </p>
        <p className="text-sm text-[#6B7280]">
          {data.note}
        </p>
      </div>

      {/* Action Buttons */}
      <div className="flex gap-4">
        <Button
          variant="secondary"
          size="lg"
          onClick={onBack}
          className="w-full"
        >
          Back
        </Button>

        <Button
          variant="primary"
          size="lg"
          onClick={onContinue}
          className="w-full"
        >
          Continue
        </Button>
      </div>
    </div>
  );
}
