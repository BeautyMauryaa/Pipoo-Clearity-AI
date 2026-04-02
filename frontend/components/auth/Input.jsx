'use client';

import React, { useState } from 'react';
import { Eye, EyeOff } from 'lucide-react';

export default function Input({
  label,
  type = 'text',
  placeholder,
  value,
  onChange,
  error,
  hint,
  required = false,
  ...props
}) {
  const [showPassword, setShowPassword] = useState(false);
  const isPassword = type === 'password';

  return (
    <div className="space-y-2">
      {label && (
        <label className="block text-sm font-medium text-[#E6EAF2]">
          {label}
          {required && <span className="text-[#EF4444] ml-1">*</span>}
        </label>
      )}
      
      <div className="relative">
        <input
          type={isPassword && showPassword ? 'text' : type}
          placeholder={placeholder}
          value={value}
          onChange={onChange}
          className={`
            w-full px-4 py-3 rounded-lg
            bg-[#0F1117] 
            border ${error ? 'border-[#EF4444]' : 'border-[#1F2633]'}
            text-[#E6EAF2] placeholder-[#6B7280]
            focus:outline-none focus:border-[#4F7CFF]
            transition-colors duration-200
          `}
          {...props}
        />
        
        {isPassword && (
          <button
            type="button"
            onClick={() => setShowPassword(!showPassword)}
            className="absolute right-3 top-1/2 -translate-y-1/2 text-[#6B7280] hover:text-[#9AA4B2] transition-colors"
          >
            {showPassword ? (
              <EyeOff className="w-5 h-5" />
            ) : (
              <Eye className="w-5 h-5" />
            )}
          </button>
        )}
      </div>
      
      {hint && !error && (
        <p className="text-xs text-[#6B7280]">{hint}</p>
      )}
      
      {error && (
        <p className="text-xs text-[#EF4444]">{error}</p>
      )}
    </div>
  );
}