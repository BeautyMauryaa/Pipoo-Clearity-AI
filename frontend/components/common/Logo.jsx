import React from 'react';

export default function Logo({ className = "" }) {
  return (
    <div className={`text-2xl font-bold ${className}`}>
      Clarity AI
    </div>
  );
}