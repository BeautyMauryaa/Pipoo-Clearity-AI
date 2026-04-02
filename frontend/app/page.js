import HeroSection from '@/components/landing/HeroSection';
import ProblemSection from '@/components/landing/ProblemSection';
import SolutionSection from '@/components/landing/SolutionSection';
import HowItWorksSection from '@/components/landing/HowItWorksSection';
import WhoItsForSection from '@/components/landing/WhoItsForSection';
import WhatNotSection from '@/components/landing/WhatNotSection';
import FinalCTASection from '@/components/landing/FinalCTASection';
import Footer from '@/components/layout/Footer';

export default function Home() {
  return (
    <div className="min-h-screen bg-[#0F1117] text-[#E6EAF2]">
      <HeroSection />
      <ProblemSection />
      <SolutionSection />
      <HowItWorksSection />
      <WhoItsForSection />
      <WhatNotSection />
      <FinalCTASection />
      <Footer />
    </div>
  );
}