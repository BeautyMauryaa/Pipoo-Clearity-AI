// src/components/workspace/company/views/HistoryView.jsx
'use client';

export default function HistoryView({ userData }) {
  const hiringRounds = [
    { id: 1, date: 'Dec 2024', role: 'Backend Dev', screened: 38, hired: 3 },
    { id: 2, date: 'Nov 2024', role: 'Frontend Dev', screened: 42, hired: 5 },
    { id: 3, date: 'Oct 2024', role: 'AI/ML Engineer', screened: 28, hired: 2 }
  ];

  const systemUpdates = [
    { date: 'Dec 28, 2024', update: 'Plagiarism detection algorithm updated' },
    { date: 'Dec 15, 2024', update: 'New Python logic task added' },
    { date: 'Dec 1, 2024', update: 'Scoring threshold adjusted for consistency' }
  ];

  return (
    <div className="max-w-6xl space-y-6">
      {/* Header */}
      <div>
        <h2 className="text-2xl font-semibold text-[#E6EAF2] mb-2">History</h2>
        <p className="text-[#9AA4B2]">Transparency & accountability</p>
      </div>

      {/* Past Hiring Rounds */}
      <div className="bg-[#151A23] border border-[#1F2633] rounded-lg p-6">
        <h3 className="text-lg font-semibold text-[#E6EAF2] mb-4">Past Hiring Rounds</h3>
        <div className="space-y-3">
          {hiringRounds.map((round) => (
            <div 
              key={round.id}
              className="p-4 bg-[#1F2633] rounded-lg hover:bg-[#2A3441] transition-colors cursor-pointer"
            >
              <div className="flex justify-between items-start mb-2">
                <div>
                  <h4 className="text-[#E6EAF2] font-medium">{round.role}</h4>
                  <p className="text-sm text-[#9AA4B2]">{round.date}</p>
                </div>
                <button className="text-sm text-[#4F7CFF] hover:text-[#6B8FFF]">
                  View Details
                </button>
              </div>
              <div className="flex gap-6 text-sm">
                <div>
                  <span className="text-[#9AA4B2]">Screened: </span>
                  <span className="text-[#E6EAF2]">{round.screened}</span>
                </div>
                <div>
                  <span className="text-[#9AA4B2]">Hired: </span>
                  <span className="text-[#22C55E]">{round.hired}</span>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Candidate Outcomes */}
      <div className="bg-[#151A23] border border-[#1F2633] rounded-lg p-6">
        <h3 className="text-lg font-semibold text-[#E6EAF2] mb-4">Recent Candidate Outcomes</h3>
        <div className="space-y-2 text-sm">
          <div className="flex justify-between items-center p-3 bg-[#1F2633] rounded-lg">
            <span className="text-[#E6EAF2]">Aman S. - Backend</span>
            <span className="text-[#F59E0B]">Flagged</span>
          </div>
          <div className="flex justify-between items-center p-3 bg-[#1F2633] rounded-lg">
            <span className="text-[#E6EAF2]">Priya K. - Frontend</span>
            <span className="text-[#22C55E]">Shortlisted</span>
          </div>
          <div className="flex justify-between items-center p-3 bg-[#1F2633] rounded-lg">
            <span className="text-[#E6EAF2]">Rohit M. - AI/ML</span>
            <span className="text-[#EF4444]">Rejected</span>
          </div>
          <div className="flex justify-between items-center p-3 bg-[#1F2633] rounded-lg">
            <span className="text-[#E6EAF2]">Neha P. - Backend</span>
            <span className="text-[#22C55E]">Hired</span>
          </div>
        </div>
      </div>

      {/* Evaluation Changes */}
      <div className="bg-[#151A23] border border-[#1F2633] rounded-lg p-6">
        <h3 className="text-lg font-semibold text-[#E6EAF2] mb-4">Evaluation System Updates</h3>
        <div className="space-y-3">
          {systemUpdates.map((item, index) => (
            <div key={index} className="flex gap-4">
              <div className="w-2 h-2 rounded-full bg-[#4F7CFF] mt-2" />
              <div className="flex-1">
                <p className="text-sm text-[#9AA4B2] mb-1">{item.date}</p>
                <p className="text-[#E6EAF2]">{item.update}</p>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Audit Trail Note */}
      <div className="bg-[#151A23] border border-[#1F2633] rounded-lg p-6">
        <h3 className="text-lg font-semibold text-[#E6EAF2] mb-2">Audit Trail</h3>
        <p className="text-[#9AA4B2] text-sm">
          All evaluation decisions and system changes are logged for compliance and transparency. 
          Full audit reports can be generated for organizational review.
        </p>
      </div>
    </div>
  );
}