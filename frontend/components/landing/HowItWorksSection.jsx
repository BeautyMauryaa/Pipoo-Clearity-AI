'use client';

import React from 'react';
import { motion } from 'framer-motion';
import { ArrowRight } from 'lucide-react';
import MotionCard from '../onboarding/ui/MotionCard';
import AmbientParticles from '../onboarding/ui/AmbientParticles';

export default function HowItWorksSection() {
  const flow = [
    { label: 'You', color: '#9AA4B2' },
    { label: 'Pipoo', color: '#4F7CFF' },
    { label: 'Clarity AI Engine', color: '#4F7CFF' },
    { label: 'Decisions / Proof / Plans', color: '#22c55e' },
  ];

  return (
    <section
      id="how-it-works"
      className="relative py-24 px-6 bg-[#0a0b0f] overflow-hidden"
    >
      {/* Ambient particles */}
      <AmbientParticles />

      <div className="relative max-w-7xl mx-auto z-10">
        {/* Heading */}
        <motion.div
          initial={{ opacity: 0, y: 16 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
          className="text-center mb-12"
        >
          <h2 className="text-4xl md:text-5xl font-bold text-white mb-8">
            How Pipoo works
          </h2>
        </motion.div>

        {/* Flow steps */}
        <div className="flex flex-wrap items-center justify-center gap-4 mb-12">
          {flow.map((step, index) => (
            <React.Fragment key={index}>
              <MotionCard accent={step.color}>
                <motion.div
                  className="px-6 py-3 rounded-lg flex items-center justify-center"
                  whileHover={{ y: -2, scale: 1.02 }}
                  transition={{ type: 'spring', stiffness: 200, damping: 20 }}
                >
                  <span
                    className="text-base md:text-lg font-semibold"
                    style={{ color: step.color }}
                  >
                    {step.label}
                  </span>
                </motion.div>
              </MotionCard>

              {index < flow.length - 1 && (
                <motion.div
                  className="flex items-center justify-center"
                  initial={{ opacity: 0 }}
                  whileInView={{ opacity: 1 }}
                  viewport={{ once: true }}
                  transition={{
                    delay: index * 0.1,
                    duration: 0.5,
                    repeat: Infinity,
                    repeatType: 'mirror',
                  }}
                >
                  <ArrowRight className="w-5 h-5 text-gray-600 animate-pulse" />
                </motion.div>
              )}
            </React.Fragment>
          ))}
        </div>

        {/* Explanatory text */}
        <div className="max-w-2xl mx-auto space-y-4 text-center">
          <motion.p
            initial={{ opacity: 0, y: 10 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.5 }}
            className="text-gray-300 text-lg leading-relaxed"
          >
            Pipoo is the interface you talk to.<br />
            Clarity AI is the engine that decides.
          </motion.p>

          <motion.p
            initial={{ opacity: 0, y: 10 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.5, delay: 0.1 }}
            className="text-gray-400 text-lg leading-relaxed"
          >
            Pipoo doesn't motivate.<br />
            It guides, enforces, and evaluates.
          </motion.p>
        </div>
      </div>
    </section>
  );
}
