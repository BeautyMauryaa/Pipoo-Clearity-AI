'use client';

import React from 'react';
import Link from 'next/link';
import Button from '../onboarding/ui/Button';
import { ROUTES } from '@/lib/constants';

export default function FinalCTASection() {
  return (
    <section className="relative py-32 px-6 overflow-hidden">
      <div className="relative max-w-4xl mx-auto z-10">
        {/* CTA Card */}
        <div className="bg-[#151A23] border border-[#1F2633] rounded-2xl p-12 md:p-16 text-center shadow-2xl hover:border-[#4F7CFF]/30 transition-all duration-300">
          <h2 className="text-4xl md:text-5xl font-bold text-white mb-6 leading-tight">
            Start with clarity.<br />
            Let Pipoo handle the rest.
          </h2>

          <div className="flex flex-col items-center gap-4 mb-6">
            <Link href={ROUTES.SIGNUP}>
              <Button 
                variant="primary" 
                size="lg" 
                className="text-lg px-10 py-5 hover:scale-105 transition-transform duration-200"
              >
                Enter Pipoo Workspace
              </Button>
            </Link>
          </div>

          <p className="text-[#6B7280] text-sm">
            No hype. Just honesty.
          </p>

          {/* Subtle background glow */}
          <div className="absolute -inset-1 bg-gradient-to-r from-[#4F7CFF]/5 to-[#8B5CF6]/5 rounded-2xl blur-2xl -z-10 opacity-50" />
        </div>
      </div>
    </section>
  );
}