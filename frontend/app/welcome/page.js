'use client';

import React from 'react';
import { useRouter } from 'next/navigation';
import Button from '@/components/onboarding/ui/Button';
import { ROUTES } from '@/lib/constants';

export default function WelcomePage() {
  const router = useRouter();

  return (
   <div className="min-h-screen bg-[#0F1117] text-[#E6EAF2] flex items-start justify-center px-6 pt-24 md:pt-28 relative overflow-hidden">

      
      {/* Ambient background effects */}
      <div className="absolute inset-0 overflow-hidden">
        <div className="absolute top-1/4 left-1/4 w-96 h-96 bg-[#4F7CFF]/10 rounded-full blur-[100px]" />
        <div className="absolute bottom-1/4 right-1/4 w-96 h-96 bg-[#8B5CF6]/10 rounded-full blur-[100px]" />
      </div>

      <div className="max-w-2xl w-full relative z-10">
        
        {/* Welcome Card */}
        <div className="bg-gradient-to-br from-[#151A23] to-[#0F1117] border border-[#1F2633] rounded-3xl p-8 text-center space-y-6 shadow-2xl">

          {/* Pipoo Avatar */}
          <div className="relative w-40 h-40 mx-auto mb-6">
            
            {/* Glow */}
            <div className="absolute inset-0 bg-[#4F7CFF] opacity-30 blur-3xl rounded-full animate-pulse" />

            {/* Avatar */}
            <div className="relative w-full h-full flex items-center justify-center">
              
              <div className="absolute inset-0 rounded-full bg-gradient-to-b from-[#4F7CFF]/30 to-transparent" />

              <div className="relative w-36 h-36 rounded-full bg-gradient-to-br from-[#5B8FFF] to-[#4F7CFF] flex items-center justify-center shadow-2xl">
                <div className="w-28 h-28 rounded-full bg-[#0F1117] flex items-center justify-center">
                  <div className="flex gap-5">
                    <div className="w-3.5 h-3.5 bg-white rounded-full shadow-lg" />
                    <div className="w-3.5 h-3.5 bg-white rounded-full shadow-lg" />
                  </div>
                </div>
              </div>

              {/* Bottom glow */}
              <div className="absolute bottom-0 left-1/2 -translate-x-1/2 w-3/4 h-1 bg-gradient-to-r from-transparent via-[#4F7CFF] to-transparent blur-sm" />
            </div>

            {/* Floating particles */}
            <div className="absolute top-4 left-4 w-1 h-1 bg-[#4F7CFF] rounded-full animate-pulse" />
            <div className="absolute top-8 right-8 w-1 h-1 bg-[#8B5CF6] rounded-full animate-pulse delay-300" />
            <div className="absolute bottom-8 left-12 w-1 h-1 bg-[#4F7CFF] rounded-full animate-pulse delay-700" />
          </div>

          {/* Greeting */}
          <div className="space-y-4">
            <h1 className="text-3xl md:text-4xl font-bold text-white">
              Hi, I'm Pipoo.
            </h1>

            <div className="space-y-2 text-base text-[#9AA4B2]">
              <p>I'll help you • <span className="text-[#E6EAF2]">Make clear decisions</span></p>
              <p>• <span className="text-[#E6EAF2]">Stay focused daily</span></p>
              <p>• <span className="text-[#E6EAF2]">Prove real skills</span></p>
            </div>

            <p className="text-[#6B7280] mt-6 text-sm">
              I won't motivate you. I'll be honest.
            </p>
          </div>

          {/* CTA */}
          <Button
            variant="primary"
            size="lg"
            onClick={() => router.push(ROUTES.ONBOARDING)}
            className="mx-auto mt-6 px-10 py-3 text-base hover:scale-105 transition-transform duration-200"
          >
            Start Setup
          </Button>
        </div>
      </div>
    </div>
  );
}
