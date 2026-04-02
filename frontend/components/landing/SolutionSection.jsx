'use client';

import { motion } from 'framer-motion';
import { Compass, Target, FlaskConical } from 'lucide-react';
import { useMounted } from '@/hooks/useMounted';
import MotionCard from '../onboarding/ui/MotionCard';

export default function SolutionSection() {
  const mounted = useMounted();

  if (!mounted) {
    return (
      <section id="solution" className="py-28 px-6">
        <div className="max-w-7xl mx-auto" />
      </section>
    );
  }

  const solutions = [
    {
      icon: Compass,
      title: 'Career Truth',
      description:
        "Pipoo analyzes your skills and goals and tells you what actually fits — and what doesn’t.",
      accent: '#4F7CFF',
    },
    {
      icon: Target,
      title: 'Focus & Accountability',
      description:
        'Daily execution, adaptive planning, and honest feedback when you drift.',
      accent: '#22c55e',
    },
    {
      icon: FlaskConical,
      title: 'Skill Proof',
      description:
        'Real tasks. Real evaluation. A credibility score companies can trust.',
      accent: '#a855f7',
    },
  ];

  return (
    <section id="solution" className="py-28 px-6">
      <div className="max-w-7xl mx-auto">

        {/* Heading */}
        <motion.div
          initial={{ opacity: 0, y: 16 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
          className="text-center mb-20"
        >
          <h2 className="text-4xl md:text-5xl font-bold text-white mb-4">
            One AI system. Three responsibilities.
          </h2>
        </motion.div>

        {/* Cards */}
        <div className="grid md:grid-cols-3 gap-10 mb-16">
          {solutions.map((solution, index) => {
            const Icon = solution.icon;

            return (
              <motion.div
                key={solution.title}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ delay: index * 0.12, duration: 0.5 }}
              >
                <MotionCard accent={solution.accent}>

                  {/* Icon */}
                  <div className="mb-8">
                    <div
                      className="w-14 h-14 rounded-xl flex items-center justify-center transition-all duration-500 group-hover:scale-110"
                      style={{
                        backgroundColor: `${solution.accent}15`,
                      }}
                    >
                      <Icon
                        className="w-7 h-7"
                        style={{ color: solution.accent }}
                      />
                    </div>
                  </div>

                  {/* Content */}
                  <h3 className="text-2xl font-bold text-white mb-4">
                    {solution.title}
                  </h3>

                  <p className="text-[#9AA4B2] leading-relaxed mb-4">
                    {solution.description}
                  </p>

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
          <p className="text-[#9AA4B2] text-lg">
            Same AI. Same standards. No bias.
          </p>
        </motion.div>

      </div>
    </section>
  );
}
