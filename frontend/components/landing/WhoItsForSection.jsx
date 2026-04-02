import { GraduationCap, Briefcase } from 'lucide-react';
import MotionCard from '../onboarding/ui/MotionCard';
import AmbientParticles from '../onboarding/ui/AmbientParticles';

export default function WhoItsForSection() {
  return (
    <section className="relative max-w-6xl mx-auto px-6 py-24">
      <AmbientParticles />

      <h2 className="text-4xl font-bold text-center mb-16">
        Who it's for
      </h2>

      <div className="grid md:grid-cols-2 gap-12 relative z-10">

        <MotionCard accent="#4F7CFF">
          <div className="flex items-center gap-4 mb-6">
            <div className="w-14 h-14 rounded-xl bg-[#4F7CFF]/10 flex items-center justify-center
              group-hover:shadow-[0_0_30px_#4F7CFF55] transition">
              <GraduationCap className="w-7 h-7 text-[#4F7CFF]" />
            </div>
            <h3 className="text-2xl font-bold">Individuals</h3>
          </div>

          <ul className="space-y-3 mb-6 text-[#9AA4B2]">
            <li>Students</li>
            <li>Job seekers</li>
            <li>Professionals</li>
          </ul>

          <p className="text-[#9AA4B2] text-sm">
            Get clarity, consistency, and proof without guessing or trends.
          </p>
        </MotionCard>

        <MotionCard accent="#22c55e">
          <div className="flex items-center gap-4 mb-6">
            <div className="w-14 h-14 rounded-xl bg-green-500/10 flex items-center justify-center
              group-hover:shadow-[0_0_30px_#22c55e55] transition">
              <Briefcase className="w-7 h-7 text-green-500" />
            </div>
            <h3 className="text-2xl font-bold">Companies</h3>
          </div>

          <ul className="space-y-3 mb-6 text-[#9AA4B2]">
            <li>Recruiters</li>
            <li>HR teams</li>
            <li>Startups</li>
          </ul>

          <p className="text-[#9AA4B2] text-sm">
            Evaluate real skills. Hire with confidence.
          </p>
        </MotionCard>

      </div>
    </section>
  );
}
