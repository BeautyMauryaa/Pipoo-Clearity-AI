'use client';

import { motion, useMotionValue, useMotionTemplate } from 'framer-motion';
import { X } from 'lucide-react';

export default function WhatNotSection() {
  const notList = [
    'Not a chatbot',
    'Not a motivation app',
    'Not a generic roadmap generator',
  ];

  const mouseX = useMotionValue(0);
  const mouseY = useMotionValue(0);

  function handleMouseMove(e) {
    const rect = e.currentTarget.getBoundingClientRect();
    mouseX.set(e.clientX - rect.left);
    mouseY.set(e.clientY - rect.top);
  }

  return (
    <section
      id="about"
      onMouseMove={handleMouseMove}
      className="relative py-28 px-6 bg-[#0a0b0f] overflow-hidden"
    >
      {/* Ambient rejection glow */}
      <motion.div
        className="pointer-events-none absolute inset-0"
        style={{
          background: useMotionTemplate`
            radial-gradient(
              320px circle at ${mouseX}px ${mouseY}px,
              rgba(239,68,68,0.08),
              transparent 65%
            )
          `,
        }}
      />

      {/* Soft ambient particles (dimmed for seriousness) */}
      <div className="pointer-events-none absolute inset-0 opacity-40">
        {[...Array(6)].map((_, i) => (
          <motion.span
            key={i}
            className="absolute w-1 h-1 rounded-full bg-red-400/30"
            initial={{
              left: `${Math.random() * 100}%`,
              top: `${Math.random() * 100}%`,
            }}
            animate={{
              y: ['0%', '-25%', '0%'],
              opacity: [0.15, 0.35, 0.15],
            }}
            transition={{
              duration: 14 + Math.random() * 6,
              repeat: Infinity,
              ease: 'easeInOut',
            }}
          />
        ))}
      </div>

      <div className="relative max-w-4xl mx-auto text-center z-10">
        <h2 className="text-4xl md:text-5xl font-bold text-white mb-14">
          What this is not
        </h2>

        {/* Not list */}
        <div className="space-y-5 mb-14">
          {notList.map((item, index) => (
            <motion.div
              key={index}
              initial={{ opacity: 0, y: 12 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: index * 0.1, duration: 0.4 }}
              className="
                group mx-auto flex items-center justify-center gap-4
                text-lg text-[#9AA4B2]
                max-w-md
              "
            >
              <span
                className="
                  flex items-center justify-center
                  w-9 h-9 rounded-full
                  bg-red-500/10
                  transition-all duration-300
                  group-hover:bg-red-500/20
                  group-hover:shadow-[0_0_20px_rgba(239,68,68,0.35)]
                "
              >
                <X className="w-5 h-5 text-red-400" />
              </span>

              <span className="relative">
                {item}

                {/* subtle strike-on-hover */}
                <span
                  className="
                    absolute left-0 top-1/2 h-px w-0
                    bg-red-400/60
                    transition-all duration-500
                    group-hover:w-full
                  "
                />
              </span>
            </motion.div>
          ))}
        </div>

        {/* Divider */}
        <div className="relative border-t border-white/10 pt-14">
          <motion.p
            initial={{ opacity: 0, y: 10 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.5 }}
            className="text-[#9AA4B2] text-xl leading-relaxed"
          >
            This is a system built for<br />
            <span className="text-white font-semibold">
              clear decisions, real execution, and trust.
            </span>
          </motion.p>
        </div>
      </div>
    </section>
  );
}
