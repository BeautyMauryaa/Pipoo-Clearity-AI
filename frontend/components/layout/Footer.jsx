import React from 'react';
import Logo from '../common/Logo';

export default function Footer() {
  const links = [
    { name: 'About', href: '#about' },
    { name: 'Privacy', href: '#privacy' },
    { name: 'Contact', href: '#contact' }
  ];

  return (
    <footer className="border-t border-gray-800 py-12 px-6 bg-[#0a0b0f]">
      <div className="max-w-7xl mx-auto">
        <div className="flex flex-col md:flex-row items-center justify-between gap-6">
          <Logo />

          <div className="flex gap-8">
            {links.map((link) => (
              <a
                key={link.name}
                href={link.href}
                className="text-gray-400 hover:text-white transition-colors text-sm"
              >
                {link.name}
              </a>
            ))}
          </div>
        </div>

        <div className="mt-8 pt-8 border-t border-gray-800 text-center">
          <p className="text-gray-500 text-sm">
            Built for decisions, execution, and trust.
          </p>
        </div>
      </div>
    </footer>
  );
}
