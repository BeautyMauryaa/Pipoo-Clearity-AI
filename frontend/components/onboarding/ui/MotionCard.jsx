'use client';

import { motion, useMotionValue, useMotionTemplate } from 'framer-motion';

export default function MotionCard({ children, accent = '#4F7CFF' }) {
  const mouseX = useMotionValue(0);
  const mouseY = useMotionValue(0);

  function handleMouseMove(e) {
    const rect = e.currentTarget.getBoundingClientRect();
    mouseX.set(e.clientX - rect.left);
    mouseY.set(e.clientY - rect.top);
  }

  return (
    <motion.div
      onMouseMove={handleMouseMove}
      whileHover={{ y: -6 }}
      transition={{ type: 'spring', stiffness: 200, damping: 20 }}
      className="
        group relative rounded-2xl p-10
        bg-[#0f1117]
        border border-white/10
        overflow-hidden
      "
    >
      {/* Cursor glow */}
      <motion.div
        className="pointer-events-none absolute inset-0"
        style={{
          background: useMotionTemplate`
            radial-gradient(
              300px circle at ${mouseX}px ${mouseY}px,
              ${accent}25,
              transparent 60%
            )
          `,
        }}
      />

      {/* Breathing outline */}
      <div
        className="pointer-events-none absolute inset-0 rounded-2xl
                   ring-1 ring-white/5
                   animate-[pulse_7s_ease-in-out_infinite]"
        style={{ boxShadow: `0 0 50px ${accent}30` }}
      />

      <div className="relative z-10">{children}</div>
    </motion.div>
  );
}
