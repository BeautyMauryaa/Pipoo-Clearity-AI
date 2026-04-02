import React from 'react';

export default function Button({
  children,
  variant = 'primary',
  onClick,
  className = '',
  ...props
}) {
  const baseStyles = 'px-6 py-3 rounded-lg font-medium transition-all duration-200';

  const variants = {
    primary: 'bg-[#4F7CFF] text-white hover:bg-[#3D6AE8] shadow-lg shadow-blue-500/20',
    secondary: 'border-2 border-gray-600 text-gray-300 hover:border-gray-400 hover:text-white'
  };

  return (
    <button
      className={`${baseStyles} ${variants[variant]} ${className}`}
      onClick={onClick}
      {...props}
    >
      {children}
    </button>
  );
}
