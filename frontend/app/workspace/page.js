// src/app/workspace/page.js
'use client';

import { useAuth } from '@/context/AuthContext';
import { useRouter } from 'next/navigation';
import { useEffect } from 'react';
import StudentWorkspace from '@/components/workspace/student/StudentWorkspace';
import ProfessionalWorkspace from '@/components/workspace/professional/ProfessionalWorkspace';
import CompanyWorkspace from '@/components/workspace/company/CompanyWorkspace';

export default function WorkspacePage() {
  const { user, isAuthenticated, isOnboardingComplete, loading } = useAuth();
  const router = useRouter();

  // ==========================================
  // FLOW ENFORCEMENT (CRITICAL)
  // ==========================================
  useEffect(() => {
    console.log('=== WORKSPACE PAGE - FLOW CHECK ===');
    console.log('isAuthenticated:', isAuthenticated);
    console.log('user:', user);
    console.log('loading:', loading);
    
    // Wait for auth to load
    if (loading) {
      return;
    }

    // NOT LOGGED IN → Redirect to login
    if (!isAuthenticated || !user) {
      console.log('❌ Not authenticated, redirecting to /login');
      router.push('/login');
      return;
    }

    // LOGGED IN, ONBOARDING NOT DONE → Redirect to onboarding
    if (!isOnboardingComplete()) {
      console.log('❌ Onboarding not complete, redirecting to /onboarding');
      router.push('/onboarding');
      return;
    }

    console.log('✅ Auth + Onboarding complete, loading workspace');
  }, [isAuthenticated, loading, user, router]);

  // Loading state
  if (loading) {
    return (
      <div className="h-screen flex items-center justify-center bg-[#0F1117]">
        <div className="text-[#9AA4B2]">Loading workspace...</div>
      </div>
    );
  }

  // User not found
  if (!user) {
    return null; // Will redirect via useEffect
  }

  // Onboarding not complete
  if (!isOnboardingComplete()) {
    return null; // Will redirect via useEffect
  }

  console.log('✅ Rendering workspace for role:', user.role);

  // ==========================================
  // ROLE-BASED WORKSPACE RENDERING
  // ==========================================
  const renderWorkspace = () => {
    switch (user.role) {
      case 'student':
        return <StudentWorkspace userData={user} />;
      
      case 'professional':
        return <ProfessionalWorkspace userData={user} />;
      
      case 'company':
        return <CompanyWorkspace userData={user} />;
      
      default:
        return (
          <div className="h-screen flex items-center justify-center bg-[#0F1117]">
            <p className="text-[#EF4444]">Invalid user role: {user.role}</p>
          </div>
        );
    }
  };

  return renderWorkspace();
}