'use client';

import React from 'react';
import Link from 'next/link';
import { motion, useMotionValue, useMotionTemplate } from 'framer-motion';
import { MessageSquare, BarChart3, CheckCircle2 } from 'lucide-react';
import Button from '../onboarding/ui/Button';
import { ROUTES } from '@/lib/constants';

export default function HeroSection() {
  const scrollToHowItWorks = () => {
    const element = document.getElementById('how-it-works');
    if (element) {
      const offset = 80;
      const elementPosition = element.getBoundingClientRect().top;
      const offsetPosition = elementPosition + window.pageYOffset - offset;
      window.scrollTo({ top: offsetPosition, behavior: 'smooth' });
    }
  };

  // Cursor position for glow
  const mouseX = useMotionValue(0);
  const mouseY = useMotionValue(0);

  const handleMouseMove = (e) => {
    const rect = e.currentTarget.getBoundingClientRect();
    mouseX.set(e.clientX - rect.left);
    mouseY.set(e.clientY - rect.top);
  };

  const miniCards = [
    {
      icon: MessageSquare,
      iconBg: '#4F7CFF20',
      iconColor: '#4F7CFF',
      title: 'Pipoo',
      content: "You're learning React, Django, and exploring ML. That's 3 different stacks."
    },
    {
      icon: BarChart3,
      iconBg: '#374151',
      iconColor: '#9CA3AF',
      title: 'Analysis',
      content: 'Strengths: React basics\nRequired: Focus'
    },
    {
      icon: CheckCircle2,
      iconBg: '#22c55e20',
      iconColor: '#22c55e',
      title: 'Recommendation',
      content: 'Pick one. Frontend or backend. Master it first.'
    }
  ];

  return (
    <section
      className="relative max-w-7xl mx-auto px-6 pt-32 pb-32 overflow-hidden"
      onMouseMove={handleMouseMove}
    >
      {/* Ambient particles behind everything */}
      <div className="absolute inset-0 pointer-events-none overflow-hidden">
        {[...Array(10)].map((_, i) => (
          <motion.span
            key={i}
            className="absolute w-1 h-1 rounded-full bg-[#4F7CFF]/20"
            initial={{ x: `${Math.random() * 100}%`, y: `${Math.random() * 100}%` }}
            animate={{
              y: ['0%', '-15%', '0%'],
              opacity: [0.2, 0.5, 0.2]
            }}
            transition={{
              duration: 15 + Math.random() * 5,
              repeat: Infinity,
              ease: 'easeInOut'
            }}
          />
        ))}
      </div>

      <div className="grid lg:grid-cols-2 gap-16 items-center relative z-10">
        
        {/* Left content */}
        <motion.div
          initial={{ opacity: 0, x: -30 }}
          whileInView={{ opacity: 1, x: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.7 }}
          className="space-y-8"
        >
          <h1 className="text-5xl lg:text-6xl font-bold leading-tight">
            Clarity for people.<br />
            Trust for companies.
          </h1>

          <p className="text-xl text-[#9AA4B2] leading-relaxed">
            An AI companion that tells the truth about your career, keeps you focused daily,
            and proves your real skills.
          </p>

          <p className="text-sm text-[#6B7280] italic">
            Not motivation. Not generic AI.<br />
            This system is built for decisions, execution, and proof.
          </p>

          <div className="flex gap-4 pt-4">
            <motion.div whileHover={{ scale: 1.05 }} transition={{ type: 'spring', stiffness: 200 }}>
              <Link href={ROUTES.SIGNUP}>
                <Button variant="primary" size="md">
                  Start with Pipoo
                </Button>
              </Link>
            </motion.div>
            <motion.div whileHover={{ scale: 1.05 }} transition={{ type: 'spring', stiffness: 200 }}>
              <Button variant="secondary" size="md" onClick={scrollToHowItWorks}>
                See how it works
              </Button>
            </motion.div>
          </div>
        </motion.div>

        {/* Right preview */}
        <motion.div
          initial={{ opacity: 0, x: 30 }}
          whileInView={{ opacity: 1, x: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.7 }}
        >
          <div className="relative bg-[#151A23] border border-[#1F2633] rounded-2xl p-6 shadow-2xl">
            
            {/* Cursor-synced glow */}
            <motion.div
              className="absolute inset-0 pointer-events-none"
              style={{
                background: useMotionTemplate`
                  radial-gradient(
                    300px circle at ${mouseX}px ${mouseY}px,
                    #4F7CFF25,
                    transparent 60%
                  )
                `
              }}
            />

            <div className="space-y-6 relative z-10">
              {miniCards.map((item, idx) => {
                const Icon = item.icon;
                return (
                  <motion.div
                    key={idx}
                    whileHover={{ scale: 1.03 }}
                    transition={{ type: 'spring', stiffness: 150 }}
                    className="flex items-start gap-3"
                  >
                    <div
                      className="w-8 h-8 rounded-full flex items-center justify-center shrink-0 mt-1 transition-all duration-300 group hover:shadow-[0_0_20px_#4F7CFF55]"
                      style={{ backgroundColor: item.iconBg }}
                    >
                      <Icon className="w-4 h-4" style={{ color: item.iconColor }} />
                    </div>
                    <div className="flex-1">
                      <div className={`text-sm font-medium ${item.title === 'Analysis' ? 'text-gray-400' : 'text-white'} mb-2`}>
                        {item.title}
                      </div>
                      <div className="bg-[#0F1117] rounded-lg p-3 border border-[#1F2633]">
                        <p className="text-sm text-[#9AA4B2] whitespace-pre-line">{item.content}</p>
                      </div>
                    </div>
                  </motion.div>
                );
              })}
            </div>

            {/* Breathing outline glow */}
            <div className="absolute -inset-1 rounded-2xl bg-gradient-to-r from-[#4F7CFF]/20 to-purple-500/20 blur-xl -z-10 animate-pulse" />
          </div>
        </motion.div>
      </div>
    </section>
  );
}
