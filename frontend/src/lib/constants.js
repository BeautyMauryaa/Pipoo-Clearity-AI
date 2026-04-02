// User Roles
export const USER_ROLES = {
  STUDENT: 'student',
  PROFESSIONAL: 'professional',
  COMPANY: 'company'
};

// Role Display Names
export const ROLE_LABELS = {
  [USER_ROLES.STUDENT]: 'Student / Job Seeker',
  [USER_ROLES.PROFESSIONAL]: 'Professional',
  [USER_ROLES.COMPANY]: 'Company / Recruiter'
};

// Routes
export const ROUTES = {
  LANDING: '/',
  LOGIN: '/login',
  SIGNUP: '/signup',
  WELCOME: '/welcome',
  ONBOARDING: '/onboarding',
  WORKSPACE: '/workspace'
};

// Onboarding Steps
export const ONBOARDING_STEPS = {
  ABOUT: 1,
  SKILLS: 2,
  CONFIRMATION: 3
};

// Colors (for reference)
export const COLORS = {
  BASE_PRIMARY: '#0F1117',
  BASE_SECONDARY: '#151A23',
  BASE_BORDER: '#1F2633',
  TEXT_PRIMARY: '#E6EAF2',
  TEXT_SECONDARY: '#9AA4B2',
  TEXT_MUTED: '#6B7280',
  ACCENT_BLUE: '#4F7CFF',
  ACCENT_VIOLET: '#8B5CF6',
  STATUS_SUCCESS: '#22C55E',
  STATUS_WARNING: '#F59E0B',
  STATUS_ERROR: '#EF4444'
};