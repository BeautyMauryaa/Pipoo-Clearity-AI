// src/components/workspace/student/views/SkillProofView.jsx
'use client';

export default function SkillProofView({ userData }) {
  const tasks = [
    { id: 1, title: 'Python Basics Task', difficulty: 'Easy', completed: false },
    { id: 2, title: 'Logic Challenge', difficulty: 'Medium', completed: false },
    { id: 3, title: 'Git Workflow Test', difficulty: 'Easy', completed: false }
  ];

  return (
    <div className="max-w-4xl space-y-6">
      {/* Header */}
      <div>
        <h2 className="text-2xl font-bold text-[#E6EAF2] mb-2">Skill Proof</h2>
        <p className="text-[#9AA4B2]">Prove what you know</p>
      </div>

      {/* Credibility Score */}
      <div className="bg-[#151A23] border border-[#1F2633] rounded-lg p-6">
        <h3 className="text-lg font-semibold text-[#E6EAF2] mb-4">Credibility Score</h3>
        <div className="flex items-baseline gap-2 mb-2">
          <span className="text-4xl font-bold text-[#4F7CFF]">12</span>
          <span className="text-[#9AA4B2]">/ 100</span>
        </div>
        <div className="w-full h-2 bg-[#1F2633] rounded-full overflow-hidden">
          <div className="h-full bg-[#4F7CFF]" style={{ width: '12%' }} />
        </div>
        <p className="text-sm text-[#9AA4B2] mt-2">
          Complete tasks to build trust with employers
        </p>
      </div>

      {/* Micro Tasks */}
      <div className="bg-[#151A23] border border-[#1F2633] rounded-lg p-6">
        <h3 className="text-lg font-semibold text-[#E6EAF2] mb-4">Available Tasks</h3>
        <div className="space-y-3">
          {tasks.map((task) => (
            <div 
              key={task.id}
              className="p-4 bg-[#1F2633] rounded-lg hover:bg-[#2A3441] transition-colors cursor-pointer"
            >
              <div className="flex items-center justify-between mb-2">
                <h4 className="text-[#E6EAF2] font-medium">{task.title}</h4>
                <span className={`text-xs px-2 py-1 rounded ${
                  task.difficulty === 'Easy' 
                    ? 'bg-[#22C55E]/20 text-[#22C55E]'
                    : 'bg-[#F59E0B]/20 text-[#F59E0B]'
                }`}>
                  {task.difficulty}
                </span>
              </div>
              <button className="text-sm text-[#4F7CFF] hover:text-[#6B8FFF] transition-colors">
                Start Task →
              </button>
            </div>
          ))}
        </div>
      </div>

      {/* How It Works */}
      <div className="bg-[#151A23] border border-[#1F2633] rounded-lg p-6">
        <h3 className="text-lg font-semibold text-[#E6EAF2] mb-4">How Skill Proof Works</h3>
        <ul className="space-y-2 text-[#E6EAF2]">
          <li className="flex items-start gap-2">
            <span className="text-[#4F7CFF]">1.</span>
            <span>Complete micro-tasks that test real skills</span>
          </li>
          <li className="flex items-start gap-2">
            <span className="text-[#4F7CFF]">2.</span>
            <span>Your work is analyzed for originality and quality</span>
          </li>
          <li className="flex items-start gap-2">
            <span className="text-[#4F7CFF]">3.</span>
            <span>Build a credibility score companies can trust</span>
          </li>
        </ul>
      </div>
    </div>
  );
}