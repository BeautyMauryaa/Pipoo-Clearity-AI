'use client';

import React, { useState, useEffect } from 'react';
import Link from 'next/link';
import Logo from '../common/Logo';
import Button from '../onboarding/ui/Button';
import { ROUTES } from '@/lib/constants';

export default function Navbar() {
  const [isScrolled, setIsScrolled] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 20);
    };
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const scrollToSection = (sectionId) => {
    const element = document.getElementById(sectionId);
    if (element) {
      const offset = 80;
      const elementPosition = element.getBoundingClientRect().top;
      const offsetPosition = elementPosition + window.pageYOffset - offset;

      window.scrollTo({
        top: offsetPosition,
        behavior: 'smooth',
      });
    }
  };

  const navLinks = [
    { name: 'How it works', id: 'how-it-works' },
    { name: 'Features', id: 'solution' },
    { name: "Who it's for", id: 'who-its-for' },
    { name: 'About', id: 'about' },
  ];

  return (
    <nav
      className={`fixed top-0 left-0 right-0 z-50 backdrop-blur-lg border-b transition-all duration-300 ${
        isScrolled
          ? 'bg-[#0F1117]/80 border-[#1f2937]'
          : 'bg-transparent border-transparent'
      }`}
    >
      <div className="max-w-7xl mx-auto px-6 py-4">
        <div className="flex items-center justify-between">
          {/* Logo */}
          <button
            onClick={() =>
              window.scrollTo({ top: 0, behavior: 'smooth' })
            }
            className="cursor-pointer hover:opacity-80 transition-opacity"
          >
            <Logo />
          </button>

          {/* Desktop nav links */}
          <div className="hidden md:flex items-center gap-8">
            {navLinks.map((link) => (
              <button
                key={link.id}
                onClick={() => scrollToSection(link.id)}
                className="text-gray-300 hover:text-white transition-colors cursor-pointer font-medium"
              >
                {link.name}
              </button>
            ))}
          </div>

          {/* Action buttons */}
          <div className="flex items-center gap-4">
            <Link href={ROUTES.LOGIN}>
              <Button variant="ghost" size="sm">
                Login
              </Button>
            </Link>
            <Link href={ROUTES.SIGNUP}>
              <Button variant="primary" size="sm">
                Start with Pipoo
              </Button>
            </Link>
          </div>
        </div>
      </div>
    </nav>
  );
}
