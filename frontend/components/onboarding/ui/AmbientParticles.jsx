'use client';

import { motion } from 'framer-motion';
import { useMounted } from '@/hooks/useMounted';
import { useMemo } from 'react';

export default function AmbientParticles({ count = 10 }) {
  const mounted = useMounted();

  const particles = useMemo(() => {
    if (!mounted) return [];
    return Array.from({ length: count }).map(() => ({
      x: Math.random() * 100,
      y: Math.random() * 100,
      delay: Math.random() * 2,
    }));
  }, [mounted, count]);

  if (!mounted) return null;

  return (
    <div className="pointer-events-none absolute inset-0">
      {particles.map((p, i) => (
        <motion.span
          key={i}
          className="absolute w-1 h-1 rounded-full bg-[#4F7CFF]/40"
          style={{
            left: `${p.x}%`,
            top: `${p.y}%`,
          }}
          animate={{ opacity: [0.2, 0.6, 0.2] }}
          transition={{
            duration: 4,
            delay: p.delay,
            repeat: Infinity,
          }}
        />
      ))}
    </div>
  );
}
