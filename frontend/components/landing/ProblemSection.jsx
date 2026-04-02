'use client';

import { motion } from 'framer-motion';
import { Users, Building2, Zap } from 'lucide-react';
import MotionCard from '../onboarding/ui/MotionCard';
import AmbientParticles from '../onboarding/ui/AmbientParticles';

export default function ProblemSection() {
  const problems = [
    {
      icon: Users,
      title: 'For individuals',
      text: 'Too many paths. No direction.\nLearning a lot. Achieving little.',
      accent: '#4F7CFF',
    },
    {
      icon: Building2,
      title: 'For companies',
      text: 'AI-written resumes.\nNo reliable way to trust candidates.',
      accent: '#22c55e',
    },
    {
      icon: Zap,
      title: 'For everyone',
      text: 'Noise everywhere.\nFocus nowhere.',
      accent: '#f59e0b',
    },
  ];

  return (
    <section
      id="problem"
      className="relative py-28 px-6 bg-[#0a0b0f] overflow-hidden"
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
          className="text-center mb-16"
        >
          <h2 className="text-4xl md:text-5xl font-bold text-white mb-6">
            Everyone is overwhelmed.<br />
            No one has clarity.
          </h2>
        </motion.div>

        {/* Problem Cards */}
        <div className="grid md:grid-cols-3 gap-10 mb-12">
          {problems.map((problem, index) => {
            const Icon = problem.icon;
            return (
              <motion.div
                key={index}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ delay: index * 0.12, duration: 0.5 }}
              >
                <MotionCard accent={problem.accent}>
                  <div className="flex flex-col items-center text-center">
                    {/* Icon with subtle floating & glow */}
                    <motion.div
                      className="w-14 h-14 rounded-xl flex items-center justify-center mb-4"
                      whileHover={{ y: -4, scale: 1.05 }}
                      transition={{ type: 'spring', stiffness: 200, damping: 15 }}
                      style={{ backgroundColor: `${problem.accent}15` }}
                    >
                      <Icon className="w-7 h-7" style={{ color: problem.accent }} />
                    </motion.div>

                    {/* Title */}
                    <h3 className="text-xl md:text-2xl font-semibold text-white mb-3">
                      {problem.title}
                    </h3>

                    {/* Text */}
                    <p className="text-[#9AA4B2] whitespace-pre-line leading-relaxed">
                      {problem.text}
                    </p>
                  </div>
                </MotionCard>
              </motion.div>
            );
          })}
        </div>

        {/* Footer */}
        <motion.div
          initial={{ opacity: 0, y: 12 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.5 }}
          className="text-center"
        >
          <p className="text-[#9AA4B2] italic text-lg">
            This is not a motivation problem.<br />
            It's a clarity and trust problem.
          </p>
        </motion.div>
      </div>
    </section>
  );
}
