'use client';

import React, { useState } from 'react';
import { motion, useMotionValue, useMotionTemplate } from 'framer-motion';
import { useRouter } from 'next/navigation';
import Link from 'next/link';
import Input from './Input';
import Button from '../onboarding/ui/Button';
import { useAuth } from '@/context/AuthContext';
import { validateEmail } from '@/lib/auth';
import { ROUTES } from '@/lib/constants';

export default function LoginForm() {
  const router = useRouter();
  const { login, loading, error } = useAuth();

  const mouseX = useMotionValue(0);
  const mouseY = useMotionValue(0);

  const [formData, setFormData] = useState({
    email: '',
    password: '',
  });

  const [errors, setErrors] = useState({});

  function handleMouseMove(e) {
    const rect = e.currentTarget.getBoundingClientRect();
    mouseX.set(e.clientX - rect.left);
    mouseY.set(e.clientY - rect.top);
  }

  const handleChange = (field) => (e) => {
    setFormData((prev) => ({ ...prev, [field]: e.target.value }));
    if (errors[field]) {
      setErrors((prev) => ({ ...prev, [field]: null }));
    }
  };

  const validate = () => {
    const newErrors = {};
    if (!formData.email) newErrors.email = 'Email is required';
    else if (!validateEmail(formData.email))
      newErrors.email = 'Invalid email format';

    if (!formData.password) newErrors.password = 'Password is required';

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!validate()) return;

    const result = await login(formData.email, formData.password);
    if (result.success) {
      router.push(ROUTES.WORKSPACE);
    }
  };

  const isValid = formData.email && formData.password;

  return (
    <motion.div
      onMouseMove={handleMouseMove}
      initial={{ opacity: 0, y: 18 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.6, ease: 'easeOut' }}
      whileHover={{ scale: 1.005 }}
      className="
        relative overflow-hidden
        rounded-2xl
        p-[1px]
        bg-gradient-to-br
        from-white/15
        via-white/5
        to-transparent
      "
    >
      {/* Inner container */}
      <div
        className="
          relative rounded-2xl
          bg-[#0f1117]
          p-8
          border border-white/5
          overflow-hidden
        "
      >
        {/* Cursor-synced glow */}
        <motion.div
          className="pointer-events-none absolute inset-0"
          style={{
            background: useMotionTemplate`
              radial-gradient(
                260px circle at ${mouseX}px ${mouseY}px,
                rgba(79,124,255,0.14),
                transparent 65%
              )
            `,
          }}
        />

        {/* Breathing outline */}
        <div
          className="
            pointer-events-none absolute inset-0 rounded-2xl
            ring-1 ring-white/5
            animate-[pulse_9s_ease-in-out_infinite]
          "
          style={{
            boxShadow: '0 0 55px rgba(79,124,255,0.28)',
          }}
        />

        {/* Form */}
        <form
          onSubmit={handleSubmit}
          className="relative z-10 space-y-6"
        >
          <Input
            label="Email"
            type="email"
            placeholder="you@domain.com"
            value={formData.email}
            onChange={handleChange('email')}
            error={errors.email}
            required
          />

          <Input
            label="Password"
            type="password"
            placeholder="••••••••"
            value={formData.password}
            onChange={handleChange('password')}
            error={errors.password}
            required
          />

          {error && (
            <motion.div
              initial={{ opacity: 0, y: -6 }}
              animate={{ opacity: 1, y: 0 }}
              className="
                text-sm text-red-400
                bg-red-500/10
                border border-red-500/20
                rounded-lg p-3
              "
            >
              {error}
            </motion.div>
          )}

          <Button
            type="submit"
            variant="primary"
            size="md"
            className="w-full"
            disabled={!isValid || loading}
          >
            {loading ? 'Signing in…' : 'Enter Pipoo'}
          </Button>

          <div className="space-y-4 pt-2">
            <Link
              href="/forgot-password"
              className="
                block text-center text-sm
                text-[#9AA4B2]
                hover:text-white
                transition-colors
              "
            >
              Forgot password?
            </Link>

            <div className="border-t border-white/10 pt-4">
              <p className="text-sm text-[#9AA4B2] text-center">
                New here?{' '}
                <Link
                  href={ROUTES.SIGNUP}
                  className="text-[#4F7CFF] hover:underline"
                >
                  Create an account
                </Link>
              </p>
            </div>
          </div>
        </form>
      </div>
    </motion.div>
  );
}
