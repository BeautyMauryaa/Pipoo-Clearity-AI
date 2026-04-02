// src/components/workspace/student/PipooMessage.jsx
'use client';

export default function PipooMessage({ message, type = 'default' }) {
  const typeStyles = {
    default: 'border-[#1F2633]',
    important: 'border-[#4F7CFF]',
    warning: 'border-[#F59E0B]'
  };

  return (
    <div className={`bg-[#151A23] border-l-4 ${typeStyles[type]} rounded-lg p-6 mb-6`}>
      {/* Pipoo Avatar and Message */}
      <div className="flex items-start gap-4">
        {/* Pipoo Avatar */}
        <div className="flex-shrink-0 w-12 h-12 rounded-full bg-gradient-to-br from-[#4F7CFF] to-[#8B5CF6] flex items-center justify-center">
          <div className="w-10 h-10 rounded-full bg-[#151A23] flex items-center justify-center">
            <div className="text-2xl">😊</div>
          </div>
        </div>

        {/* Message Content */}
        <div className="flex-1">
          <div className="mb-2">
            <span className="text-base font-semibold text-[#E6EAF2]">Pipoo</span>
          </div>
          
          <p className="text-[#E6EAF2] leading-relaxed text-base">
            {message}
          </p>
        </div>
      </div>
    </div>
  );
}