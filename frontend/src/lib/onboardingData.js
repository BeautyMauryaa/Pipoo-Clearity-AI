import { Compass, FlaskConical, HelpCircle, Target, Zap, AlertCircle, Focus, Clock, TrendingUp, RefreshCw, Calendar, Timer, Users, Filter, Brain, Package, ShieldAlert, UserCheck } from 'lucide-react';

// Student/Job Seeker Onboarding Data
export const studentOnboarding = {
  intro: {
    title: 'Student / Job Seeker Setup',
    subtitle: 'Pipoo will help you get job-ready with clarity and consistency.',
    note: 'You can change preferences later.'
  },
  
  goal: {
    title: "What's your current career goal?",
    options: [
      {
        id: 'job-ready',
        icon: Target,
        title: 'Get job-ready',
        description: 'Become ready for a full-time role.'
      },
      {
        id: 'internship',
        icon: FlaskConical,
        title: 'Find internship',
        description: 'Gain experience during studies.'
      },
      {
        id: 'explore',
        icon: HelpCircle,
        title: 'Explore career direction',
        description: 'Understand work options and skills.'
      }
    ]
  },
  
  time: {
    title: 'Your current skill level?',
    subtitle: 'How much time can you realistically give daily?',
    timeOptions: [
      { id: 'less-1h', label: '< 1 hour' },
      { id: '1-2h', label: '1–2 hours' },
      { id: '3plus', label: '3+ hours' }
    ],
    timelineTitle: 'When do you want to be job-ready?',
    timelineOptions: [
      { id: '3-6m', label: '3–6 months' },
      { id: '6-12m', label: '6–12 months' },
      { id: 'no-timeline', label: 'No fixed timeline' }
    ]
  },
  
  skills: {
    title: 'Your current skill level?',
    levelOptions: [
      { id: 'beginner', label: 'Beginner' },
      { id: 'intermediate', label: 'Intermediate' },
      { id: 'advanced', label: 'Advanced' }
    ],
    interestTitle: 'Which areas interest you?',
    interestSubtitle: '(Optional)',
    interestOptions: [
      { id: 'ai-ml', label: 'AI / ML' },
      { id: 'web', label: 'Web Development' },
      { id: 'backend', label: 'Backend' },
      { id: 'data', label: 'Data / Analytics' },
      { id: 'not-sure', label: 'Not sure yet' }
    ],
    note: 'You can change this later.'
  },
  
  stage: {
    title: 'Where are you right now?',
    options: [
      { id: '1st-2nd', label: '1st / 2nd year' },
      { id: '3rd', label: '3rd year' },
      { id: 'final', label: 'Final year' },
      { id: 'graduate', label: 'Graduate' }
    ],
    blockerTitle: 'What usually stops you?',
    blockerSubtitle: 'Lack of discipline, routine breaks.',
    blockerNote: 'Pipoo will actively address this.',
    blockerIcon: AlertCircle,
    // Added blocker options
    blockerOptions: [
      { id: 'consistency', label: 'Consistency / Discipline' },
      { id: 'confusion', label: 'Don\'t know what to focus on' },
      { id: 'motivation', label: 'Staying motivated' },
      { id: 'time', label: 'Finding time' },
      { id: 'getting-started', label: 'Just getting started' }
    ]
  }
};

// Professional Onboarding Data
export const professionalOnboarding = {
  intro: {
    title: 'Professional Setup',
    subtitle: 'Pipoo will help you optimize growth, clarity and execution — without noise.',
    note: 'This is not beginner guidance.'
  },
  
  goal: {
    title: "What's your primary objective?",
    options: [
      {
        id: 'improve-role',
        icon: TrendingUp,
        title: 'Improve current role',
        description: 'Increase efficiency, impact, or seniority'
      },
      {
        id: 'switch-role',
        icon: RefreshCw,
        title: 'Switch role/domain',
        description: 'Move to a different tech or position'
      },
      {
        id: 'increase-output',
        icon: Zap,
        title: 'Increase output & focus',
        description: 'Better execution, less burnout'
      }
    ]
  },
  
  time: {
    title: 'When can you realistically work on growth?',
    subtitle: '',
    timeOptions: [
      { id: 'weekdays', label: 'Weekdays only', description: 'Increase efficiency, impact, or seniority' },
      { id: 'weekends', label: 'Weekends only', description: '' },
      { id: 'flexible', label: 'Flexible (short daily sessions)', description: '' }
    ],
    timelineTitle: 'How much focused time can you give?',
    timelineOptions: [
      { id: 'less-1h', label: '< 1 hour' },
      { id: '1-2h', label: '1–2 hours' },
      { id: '3plus', label: '3+ hours' }
    ]
  },
  
  skills: {
    title: 'Your experience level?',
    levelOptions: [
      { id: '0-1y', label: '0–1 years' },
      { id: '1-3y', label: '1–3 years' },
      { id: '3-5y', label: '3–5 years' },
      { id: '5plus', label: '5+ years' }
    ],
    interestTitle: 'Current domain?',
    interestSubtitle: '',
    interestOptions: [
      { id: 'frontend', label: 'Frontend' },
      { id: 'backend', label: 'Backend' },
      { id: 'ai-ml', label: 'AI / ML' },
      { id: 'data', label: 'Data' },
      { id: 'product', label: 'Product / Tech hybrid' }
    ],
    note: 'Pipoo adapts guidance based on this.'
  },
  
  stage: {
    title: 'What slows your growth most?',
    options: [
      { id: 'time', label: 'Lack of time' },
      { id: 'context-switching', label: 'Context switching' },
      { id: 'burnout', label: 'Burnout' },
      { id: 'unclear-next', label: 'Unclear next step' },
      { id: 'inconsistent', label: 'Inconsistent execution' }
    ],
    blockerTitle: '',
    blockerSubtitle: '',
    blockerNote: 'Pipoo will actively optimize for this.',
    blockerIcon: AlertCircle,
    // No additional blocker options for professionals (stage IS the blocker)
    blockerOptions: []
  }
};

// Company/Recruiter Onboarding Data
export const companyOnboarding = {
  intro: {
    title: 'Company / Recruiter Setup',
    subtitle: 'Pipoo helps you evaluate real skills — not resumes or hype.',
    note: 'Designed for structured, unbiased hiring.'
  },
  
  goal: {
    title: 'What is your primary hiring goal?',
    options: [
      {
        id: 'screen-candidates',
        icon: Filter,
        title: 'Screen candidates efficiently',
        description: 'Quick filtering with high accuracy'
      },
      {
        id: 'evaluate-skills',
        icon: Brain,
        title: 'Evaluate real skills deeply',
        description: 'In-depth technical assessment'
      },
      {
        id: 'talent-pool',
        icon: Package,
        title: 'Build a long-term talent pool',
        description: 'Maintain verified candidate database'
      }
    ]
  },
  
  time: {
    title: 'How often do you hire?',
    subtitle: '',
    timeOptions: [
      { id: 'occasionally', label: 'Occasionally', description: '' },
      { id: 'monthly', label: 'Monthly', description: '' },
      { id: 'continuous', label: 'Continuous', description: '' }
    ],
    timelineTitle: 'Team size you usually hire for?',
    timelineOptions: [
      { id: '1-5', label: '1–5' },
      { id: '6-20', label: '6–20' },
      { id: '20plus', label: '20+' }
    ]
  },
  
  skills: {
    title: 'Seniority level you hire for?',
    levelOptions: [
      { id: 'intern', label: 'Intern' },
      { id: 'junior', label: 'Junior' },
      { id: 'mid', label: 'Mid-level' },
      { id: 'senior', label: 'Senior' }
    ],
    interestTitle: 'Primary roles you hire for?',
    interestSubtitle: '(Select all that apply)',
    interestOptions: [
      { id: 'frontend', label: 'Frontend' },
      { id: 'backend', label: 'Backend' },
      { id: 'ai-ml', label: 'AI / ML' },
      { id: 'data', label: 'Data' },
      { id: 'product', label: 'Product / Hybrid' }
    ],
    note: 'Pipoo adjusts difficulty and scoring accordingly.'
  },
  
  stage: {
    title: "What's your biggest hiring challenge?",
    options: [
      { id: 'fake-resumes', label: 'Fake or inflated resumes' },
      { id: 'interview-cheating', label: 'Interview cheating' },
      { id: 'skill-fit', label: 'Poor skill-to-role fit' },
      { id: 'time-consuming', label: 'Time-consuming screening' },
      { id: 'reliability', label: 'Low candidate reliability' }
    ],
    blockerTitle: '',
    blockerSubtitle: '',
    blockerNote: 'Pipoo will optimize evaluation for this.',
    blockerIcon: ShieldAlert,
    // Empty array - no additional blocker for companies
    blockerOptions: []
  }
};

// Helper function to get onboarding data by role
export const getOnboardingData = (role) => {
  const dataMap = {
    student: studentOnboarding,
    professional: professionalOnboarding,
    company: companyOnboarding
  };
  
  return dataMap[role] || studentOnboarding;
};