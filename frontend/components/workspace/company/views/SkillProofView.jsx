// src/components/workspace/company/views/SkillProofView.jsx
'use client';

export default function SkillProofView({ userData }) {
  const activeTasks = [
    { id: 1, name: 'Python Logic Test', difficulty: 'Medium', passRate: '68%', avgTime: '24 min' },
    { id: 2, name: 'Backend API Task', difficulty: 'Hard', passRate: '42%', avgTime: '38 min' },
    { id: 3, name: 'AI Reasoning Task', difficulty: 'Medium', passRate: '55%', avgTime: '28 min' }
  ];

  const integritySignals = [
    { type: 'Plagiarism detected', count: 3, severity: 'high' },
    { type: 'AI-assisted behavior flagged', count: 7, severity: 'medium' },
    { type: 'Pattern similarity', count: 12, severity: 'low' }
  ];

  return (
    <div className="max-w-6xl space-y-6">
      {/* Header */}
      <div>
        <h2 className="text-2xl font-semibold text-[#E6EAF2] mb-2">Skill Proof</h2>
        <p className="text-[#9AA4B2]">Evaluation system control</p>
      </div>

      {/* Active Skill Tasks */}
      <div className="bg-[#151A23] border border-[#1F2633] rounded-lg p-6">
        <div className="flex justify-between items-center mb-4">
          <h3 className="text-lg font-semibold text-[#E6EAF2]">Active Skill Tasks</h3>
          <button className="px-4 py-2 bg-[#4F7CFF] hover:bg-[#6B8FFF] text-white text-sm rounded-lg transition-colors">
            Add New Task
          </button>
        </div>

        <div className="space-y-3">
          {activeTasks.map((task) => (
            <div 
              key={task.id}
              className="p-4 bg-[#1F2633] rounded-lg hover:bg-[#2A3441] transition-colors"
            >
              <div className="flex justify-between items-start mb-3">
                <div>
                  <h4 className="text-[#E6EAF2] font-medium mb-1">{task.name}</h4>
                  <span className={`text-xs px-2 py-1 rounded ${
                    task.difficulty === 'Hard' 
                      ? 'bg-[#EF4444]/20 text-[#EF4444]'
                      : task.difficulty === 'Medium'
                      ? 'bg-[#F59E0B]/20 text-[#F59E0B]'
                      : 'bg-[#22C55E]/20 text-[#22C55E]'
                  }`}>
                    {task.difficulty}
                  </span>
                </div>
                <button className="text-sm text-[#9AA4B2] hover:text-[#E6EAF2]">
                  Edit
                </button>
              </div>

              <div className="grid grid-cols-2 gap-4 text-sm">
                <div>
                  <span className="text-[#9AA4B2]">Pass Rate: </span>
                  <span className="text-[#E6EAF2]">{task.passRate}</span>
                </div>
                <div>
                  <span className="text-[#9AA4B2]">Avg Time: </span>
                  <span className="text-[#E6EAF2]">{task.avgTime}</span>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Integrity Signals */}
      <div className="bg-[#151A23] border border-[#1F2633] rounded-lg p-6">
        <h3 className="text-lg font-semibold text-[#E6EAF2] mb-4">Integrity Signals</h3>
        <div className="space-y-3">
          {integritySignals.map((signal, index) => (
            <div 
              key={index}
              className="flex justify-between items-center p-4 bg-[#1F2633] rounded-lg"
            >
              <div className="flex items-center gap-3">
                <div className={`w-2 h-2 rounded-full ${
                  signal.severity === 'high' ? 'bg-[#EF4444]' :
                  signal.severity === 'medium' ? 'bg-[#F59E0B]' :
                  'bg-[#9AA4B2]'
                }`} />
                <span className="text-[#E6EAF2]">{signal.type}</span>
              </div>
              <span className="text-[#9AA4B2]">{signal.count} cases</span>
            </div>
          ))}
        </div>
      </div>

      {/* Task Creation Guide */}
      <div className="bg-[#151A23] border border-[#1F2633] rounded-lg p-6">
        <h3 className="text-lg font-semibold text-[#E6EAF2] mb-4">Task Creation Guidelines</h3>
        <ul className="space-y-2 text-sm text-[#E6EAF2]">
          <li className="flex items-start gap-2">
            <span className="text-[#9AA4B2]">•</span>
            <span>Tasks should test applied skills, not memorization</span>
          </li>
          <li className="flex items-start gap-2">
            <span className="text-[#9AA4B2]">•</span>
            <span>Include time limits to detect AI assistance patterns</span>
          </li>
          <li className="flex items-start gap-2">
            <span className="text-[#9AA4B2]">•</span>
            <span>Vary task structure to prevent pattern recognition</span>
          </li>
        </ul>
      </div>
    </div>
  );
}