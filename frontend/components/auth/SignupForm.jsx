'use client';

import React, { useState } from 'react';
import { motion, useMotionValue, useMotionTemplate } from 'framer-motion';
import { useRouter } from 'next/navigation';
import Link from 'next/link';
import Input from './Input';
import Button from '../onboarding/ui/Button';
import { useAuth } from '@/context/AuthContext';
import { validateEmail, validatePassword } from '@/lib/auth';
import { ROUTES, USER_ROLES, ROLE_LABELS } from '@/lib/constants';

export default function SignupForm() {
  const router = useRouter();
  const { signup, loading } = useAuth();

  const mouseX = useMotionValue(0);
  const mouseY = useMotionValue(0);

  const [formData, setFormData] = useState({
    name: '',
    email: '',
    password: '',
    role: USER_ROLES.STUDENT,
  });

  const [consent, setConsent] = useState(false);
  const [errors, setErrors] = useState({});

  function handleMouseMove(e) {
    const rect = e.currentTarget.getBoundingClientRect();
    mouseX.set(e.clientX - rect.left);
    mouseY.set(e.clientY - rect.top);
  }

  const handleChange = (field) => (e) => {
    setFormData((prev) => ({ ...prev, [field]: e.target.value }));
    if (errors[field]) setErrors((prev) => ({ ...prev, [field]: null }));
  };

  const validate = () => {
    const newErrors = {};
    if (!formData.name.trim()) newErrors.name = 'Name is required';
    if (!formData.email) newErrors.email = 'Email is required';
    else if (!validateEmail(formData.email)) newErrors.email = 'Invalid email';
    if (!formData.password) newErrors.password = 'Password is required';
    else if (!validatePassword(formData.password))
      newErrors.password = 'At least 8 characters';

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!validate() || !consent) return;

    const result = await signup(
      formData.name,
      formData.email,
      formData.password,
      formData.role
    );

    if (result.success) router.push(ROUTES.WELCOME);
  };

  const isValid =
    formData.name && formData.email && formData.password && consent;

  return (
    <motion.div
      onMouseMove={handleMouseMove}
      initial={{ opacity: 0, y: 16 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5, ease: 'easeOut' }}
      className="
        relative rounded-2xl p-8
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
              280px circle at ${mouseX}px ${mouseY}px,
              rgba(79,124,255,0.15),
              transparent 65%
            )
          `,
        }}
      />

      {/* Breathing outline */}
      <div
        className="pointer-events-none absolute inset-0 rounded-2xl
                   ring-1 ring-white/5
                   animate-[pulse_8s_ease-in-out_infinite]"
        style={{ boxShadow: '0 0 40px rgba(79,124,255,0.25)' }}
      />

      <form onSubmit={handleSubmit} className="relative z-10 space-y-6">
        <Input
          label="Full name"
          placeholder="Your name"
          value={formData.name}
          onChange={handleChange('name')}
          error={errors.name}
          required
        />

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
          hint="Use something secure. Your progress matters."
          required
        />

        {/* Role Selection */}
        <div className="space-y-3">
          <label className="text-sm font-medium text-white/90">Role</label>

          <div className="grid grid-cols-2 gap-3">
            {Object.values(USER_ROLES).map((role) => {
              const active = formData.role === role;
              return (
                <button
                  key={role}
                  type="button"
                  onClick={() =>
                    setFormData((prev) => ({ ...prev, role }))
                  }
                  className={`
                    relative rounded-lg p-4 text-sm
                    border transition-all duration-300
                    ${
                      active
                        ? 'border-[#4F7CFF] text-white bg-[#4F7CFF]/10 shadow-[0_0_20px_rgba(79,124,255,0.35)]'
                        : 'border-white/10 text-[#9AA4B2] hover:border-[#4F7CFF]/50'
                    }
                  `}
                >
                  {ROLE_LABELS[role]}
                </button>
              );
            })}
          </div>
        </div>

        <Button
          type="submit"
          variant="primary"
          size="md"
          className="w-full"
          disabled={!isValid || loading}
        >
          {loading ? 'Creating workspace…' : 'Create Workspace'}
        </Button>

        {/* Consent */}
        <label className="flex items-start gap-3 cursor-pointer">
          <input
            type="checkbox"
            checked={consent}
            onChange={(e) => setConsent(e.target.checked)}
            className="mt-1 w-4 h-4 rounded bg-[#0f1117]
                       border-white/20 text-[#4F7CFF]
                       focus:ring-[#4F7CFF] focus:ring-offset-0"
          />
          <span className="text-sm text-[#9AA4B2]">
            I understand Pipoo gives honest feedback — not motivation.
          </span>
        </label>

        <div className="border-t border-white/10 pt-4">
          <p className="text-sm text-center text-[#9AA4B2]">
            Already have an account?{' '}
            <Link
              href={ROUTES.LOGIN}
              className="text-[#4F7CFF] hover:underline"
            >
              Log in
            </Link>
          </p>
        </div>
      </form>
    </motion.div>
  );
}
