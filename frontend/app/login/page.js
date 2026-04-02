'use client';

import React from 'react';
import { motion } from 'framer-motion';
import AuthLayout from '@/components/auth/AuthLayout';
import LoginForm from '@/components/auth/LoginForm';

export default function LoginPage() {
  const leftContent = (
    <motion.div
      initial={{ opacity: 0, x: -24 }}
      animate={{ opacity: 1, x: 0 }}
      transition={{ duration: 0.7, ease: 'easeOut' }}
      className="space-y-8 max-w-lg"
    >
      {/* Headline */}
      <div className="space-y-3">
        <h2 className="text-4xl md:text-5xl font-semibold tracking-tight text-white">
          Welcome back
          <span className="text-[#4F7CFF]">.</span>
        </h2>

        <p className="text-lg leading-relaxed text-[#9AA4B2]">
          Pipoo is ready to continue where you left off —
          focused, private, and built for real execution.
        </p>
      </div>

      {/* Divider */}
      <div className="relative pt-6">
        <div className="absolute inset-x-0 top-0 h-px bg-gradient-to-r from-transparent via-white/20 to-transparent" />

        <p className="text-sm text-[#6B7280] leading-relaxed mt-6">
          Your data is private by design.
          <span className="text-[#9AA4B2]">
            {' '}
            No training on your conversations. No surveillance. Ever.
          </span>
        </p>
      </div>

      {/* Ambient accent */}
      <div className="relative h-20">
        <div
          className="
            absolute inset-0 rounded-2xl
            bg-gradient-to-br
            from-[#4F7CFF]/10
            via-transparent
            to-transparent
            blur-2xl
          "
        />
      </div>
    </motion.div>
  );

  return (
    <AuthLayout
      leftContent={leftContent}
      rightContent={
        <motion.div
          initial={{ opacity: 0, x: 24 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ duration: 0.7, ease: 'easeOut', delay: 0.05 }}
          className="relative"
        >
          {/* Glow behind form */}
          <div
            className="
              pointer-events-none absolute -inset-10
              bg-gradient-to-br
              from-[#4F7CFF]/15
              via-transparent
              to-transparent
              blur-3xl
            "
          />

          <LoginForm />
        </motion.div>
      }
    />
  );
}
