// src/components/workspace/company/ui/PipooNote.jsx
'use client';

export default function PipooNote({ message, type = 'info' }) {
  const styles = {
    info: 'border-l-[#4F7CFF]',
    warning: 'border-l-[#F59E0B]',
    error: 'border-l-[#EF4444]'
  };

  return (
    <div className={`bg-[#151A23] border-l-4 ${styles[type]} rounded-lg p-5`}>
      <p className="text-[#E6EAF2] leading-relaxed text-sm">
        {message}
      </p>
    </div>
  );
}