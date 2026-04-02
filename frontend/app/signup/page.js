'use client';

import { motion } from 'framer-motion';
import AuthLayout from '@/components/auth/AuthLayout';
import SignupForm from '@/components/auth/SignupForm';

export default function SignupPage() {
  const leftContent = (
    <motion.div
      initial={{ opacity: 0, y: 16 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.6, ease: 'easeOut' }}
      className="relative max-w-md"
    >
      {/* Ambient glow behind text */}
      <div
        className="
          pointer-events-none absolute -inset-8
          rounded-full blur-3xl opacity-40
        "
        style={{
          background:
            'radial-gradient(circle at 30% 30%, rgba(79,124,255,0.25), transparent 70%)',
        }}
      />

      <div className="relative space-y-6">
        <h2 className="text-4xl font-bold leading-tight text-white">
          Create your workspace<span className="text-[#4F7CFF]">.</span>
        </h2>

        <p className="text-lg text-[#9AA4B2] leading-relaxed">
          Pipoo works best when you’re honest about your goals,
          your effort, and what you actually want to improve.
        </p>

        <div className="mt-10 border-l border-white/10 pl-6">
          <p className="text-sm text-[#9AA4B2] italic leading-relaxed">
            This is not a motivation app.<br />
            <span className="text-white font-medium">
              It’s a clarity system.
            </span>
          </p>
        </div>

        {/* Subtle signal */}
        <p className="text-xs text-[#6B7280] mt-8">
          No noise. No gamification. Just progress you can prove.
        </p>
      </div>
    </motion.div>
  );

  return (
    <AuthLayout
      leftContent={leftContent}
      rightContent={<SignupForm />}
    />
  );
}
