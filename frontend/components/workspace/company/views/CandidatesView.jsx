// src/components/workspace/company/views/CandidatesView.jsx
'use client';

import { useState } from 'react';

export default function CandidatesView({ userData }) {
  const [filter, setFilter] = useState('all');
  const [selectedCandidate, setSelectedCandidate] = useState(null);

  const candidates = [
    { id: 1, name: 'Aman S.', role: 'Backend', score: 68, status: 'flagged' },
    { id: 2, name: 'Priya K.', role: 'Frontend', score: 82, status: 'passed' },
    { id: 3, name: 'Rohit M.', role: 'AI/ML', score: 45, status: 'rejected' },
    { id: 4, name: 'Neha P.', role: 'Backend', score: 91, status: 'passed' },
    { id: 5, name: 'Karan V.', role: 'Data', score: 38, status: 'flagged' }
  ];

  const getStatusColor = (status) => {
    switch (status) {
      case 'passed': return 'text-[#22C55E] bg-[#22C55E]/10';
      case 'flagged': return 'text-[#F59E0B] bg-[#F59E0B]/10';
      case 'rejected': return 'text-[#EF4444] bg-[#EF4444]/10';
      default: return 'text-[#9AA4B2] bg-[#1F2633]';
    }
  };

  return (
    <div className="max-w-6xl space-y-6">
      {/* Header */}
      <div>
        <h2 className="text-2xl font-semibold text-[#E6EAF2] mb-2">Candidates</h2>
        <p className="text-[#9AA4B2]">Pipeline management</p>
      </div>

      {/* Filters */}
      <div className="flex gap-2">
        {['all', 'passed', 'flagged', 'rejected'].map((status) => (
          <button
            key={status}
            onClick={() => setFilter(status)}
            className={`px-4 py-2 rounded-lg text-sm transition-colors ${
              filter === status
                ? 'bg-[#4F7CFF] text-white'
                : 'bg-[#1F2633] text-[#9AA4B2] hover:bg-[#2A3441]'
            }`}
          >
            {status.charAt(0).toUpperCase() + status.slice(1)}
          </button>
        ))}
      </div>

      {/* Candidate Table */}
      <div className="bg-[#151A23] border border-[#1F2633] rounded-lg overflow-hidden">
        <table className="w-full">
          <thead className="bg-[#1F2633]">
            <tr>
              <th className="px-6 py-3 text-left text-sm font-medium text-[#9AA4B2]">Name</th>
              <th className="px-6 py-3 text-left text-sm font-medium text-[#9AA4B2]">Role</th>
              <th className="px-6 py-3 text-left text-sm font-medium text-[#9AA4B2]">Score</th>
              <th className="px-6 py-3 text-left text-sm font-medium text-[#9AA4B2]">Status</th>
              <th className="px-6 py-3 text-left text-sm font-medium text-[#9AA4B2]">Action</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-[#1F2633]">
            {candidates.map((candidate) => (
              <tr key={candidate.id} className="hover:bg-[#1F2633] transition-colors">
                <td className="px-6 py-4 text-[#E6EAF2]">{candidate.name}</td>
                <td className="px-6 py-4 text-[#9AA4B2]">{candidate.role}</td>
                <td className="px-6 py-4 text-[#E6EAF2] font-medium">{candidate.score}</td>
                <td className="px-6 py-4">
                  <span className={`px-2 py-1 rounded text-xs font-medium ${getStatusColor(candidate.status)}`}>
                    {candidate.status}
                  </span>
                </td>
                <td className="px-6 py-4">
                  <button 
                    onClick={() => setSelectedCandidate(candidate)}
                    className="text-sm text-[#4F7CFF] hover:text-[#6B8FFF] transition-colors"
                  >
                    View
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {/* Candidate Detail Panel (Slide-in) */}
      {selectedCandidate && (
        <div className="fixed inset-0 bg-black/50 flex items-center justify-end z-50" onClick={() => setSelectedCandidate(null)}>
          <div 
            className="w-full max-w-md h-full bg-[#151A23] border-l border-[#1F2633] p-6 overflow-y-auto"
            onClick={(e) => e.stopPropagation()}
          >
            <div className="flex justify-between items-start mb-6">
              <div>
                <h3 className="text-xl font-semibold text-[#E6EAF2]">{selectedCandidate.name}</h3>
                <p className="text-[#9AA4B2]">{selectedCandidate.role}</p>
              </div>
              <button 
                onClick={() => setSelectedCandidate(null)}
                className="text-[#9AA4B2] hover:text-[#E6EAF2]"
              >
                ✕
              </button>
            </div>

            <div className="space-y-6">
              <div>
                <h4 className="text-sm font-medium text-[#9AA4B2] mb-2">Skill Proof Score</h4>
                <p className="text-2xl font-semibold text-[#E6EAF2]">{selectedCandidate.score} / 100</p>
              </div>

              <div>
                <h4 className="text-sm font-medium text-[#9AA4B2] mb-2">Pipoo Evaluation</h4>
                <p className="text-[#E6EAF2] text-sm">
                  Candidate shows {selectedCandidate.score > 70 ? 'consistent' : 'inconsistent'} problem-solving patterns. 
                  {selectedCandidate.status === 'flagged' && ' Flagged for potential AI assistance.'}
                </p>
              </div>

              <div className="flex gap-3">
                <button className="flex-1 bg-[#22C55E] hover:bg-[#1EA352] text-white py-2 rounded-lg transition-colors">
                  Shortlist
                </button>
                <button className="flex-1 bg-[#EF4444] hover:bg-[#DC2626] text-white py-2 rounded-lg transition-colors">
                  Reject
                </button>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}