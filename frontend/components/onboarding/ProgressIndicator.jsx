import React from 'react';

export default function ProgressIndicator({ current, total }) {
  return (
    <div className="text-sm text-[#6B7280]">
      Step {current} of {total}
    </div>
  );
}