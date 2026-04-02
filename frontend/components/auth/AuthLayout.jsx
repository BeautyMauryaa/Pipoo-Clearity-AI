import React from 'react';
import Logo from '../common/Logo';

export default function AuthLayout({ 
  leftContent, 
  rightContent, 
  showLogo = true 
}) {
  return (
    <div className="min-h-screen bg-[#0F1117] text-[#E6EAF2]">
      {/* Logo at top */}
      {showLogo && (
        <div className="pt-8 pb-12 px-6">
          <div className="max-w-6xl mx-auto">
            <Logo />
          </div>
        </div>
      )}
      
      {/* Split Layout */}
      <div className="max-w-6xl mx-auto px-6 pb-24">
        <div className="grid lg:grid-cols-2 gap-16 items-center">
          {/* Left Side - Message */}
          <div className="space-y-6">
            {leftContent}
          </div>
          
          {/* Right Side - Form */}
          <div>
            {rightContent}
          </div>
        </div>
      </div>
    </div>
  );
}