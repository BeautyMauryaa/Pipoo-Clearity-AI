import React from 'react';

export default function Card({ 
  children, 
  hover = false,
  className = '' 
}) {
  const hoverStyles = hover 
    ? 'hover:border-[#4F7CFF] transition-colors duration-300' 
    : '';
  
  return (
    <div className={`bg-[#151A23] border border-[#1F2633] rounded-xl p-8 ${hoverStyles} ${className}`}>
      {children}
    </div>
  );
}