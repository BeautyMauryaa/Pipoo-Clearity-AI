// src/lib/workspaceData.js

/**
 * Generate Pipoo's first message based on user's onboarding data
 */
export function generateFirstDayMessage(onboardingData) {
  const { goal, timeline, timePerDay, blocker, stage } = onboardingData;
  
  // Build personalized message
  let message = '';
  
  // Goal and timeline
  if (goal && timeline) {
    const goalText = goal === 'job-ready' ? 'be job-ready' : 
                     goal === 'skill-building' ? 'build specific skills' : 
                     'switch careers';
    message += `You want to ${goalText} in ${timeline}`;
  }
  
  // Time commitment
  if (timePerDay) {
    message += ` with ${timePerDay} a day`;
  }
  
  message += '. ';
  
  // Blocker acknowledgment
  if (blocker) {
    const blockerText = blocker === 'consistency' ? 'consistency' :
                       blocker === 'confusion' ? 'knowing what to focus on' :
                       blocker === 'motivation' ? 'staying motivated' :
                       blocker === 'time' ? 'finding enough time' :
                       'getting started';
    message += `Your biggest blocker is ${blockerText}. `;
  }
  
  // Closing promise
  message += "We'll keep tasks small and non-negotiable.";
  
  return message;
}

/**
 * Generate insight card data from onboarding
 */
export function generateInsightCard(onboardingData, role = 'student') {
  const { skills, interests, stage, blocker } = onboardingData;
  
  return {
    skillLevel: determineSkillLevel(skills),
    interests: formatInterests(interests),
    stage: formatStage(stage),
    focusRisk: formatBlocker(blocker)
  };
}

function determineSkillLevel(skills = []) {
  if (!skills || skills.length === 0) return 'Beginner';
  if (skills.length >= 5) return 'Intermediate';
  return 'Beginner';
}

function formatInterests(interests = []) {
  if (!interests || interests.length === 0) return 'Not specified';
  return interests.slice(0, 2).join(', ');
}

function formatStage(stage) {
  const stageMap = {
    'final-year': 'Final year',
    'recent-grad': 'Recent graduate',
    'working': 'Currently working',
    'career-switch': 'Career switcher'
  };
  return stageMap[stage] || stage || 'Not specified';
}

function formatBlocker(blocker) {
  const blockerMap = {
    'consistency': 'Consistency',
    'confusion': 'Focus clarity',
    'motivation': 'Motivation',
    'time': 'Time management',
    'getting-started': 'Getting started'
  };
  return blockerMap[blocker] || blocker || 'Not specified';
}

/**
 * Generate first task based on user profile
 */
export function generateFirstTask(onboardingData) {
  const { goal, skills } = onboardingData;
  
  // Default task for beginners
  const defaultTask = {
    title: 'Set up your development environment and write your first Python script.',
    estimatedTime: '30–40 minutes',
    type: 'setup'
  };
  
  // If user has some skills, give them a different task
  if (skills && skills.length > 2) {
    return {
      title: 'Review your existing projects and identify knowledge gaps.',
      estimatedTime: '20–30 minutes',
      type: 'assessment'
    };
  }
  
  return defaultTask;
}

/**
 * Generate optional task
 */
export function generateOptionalTask(onboardingData) {
  return {
    title: 'Watch a 20-minute introductory video on your chosen field',
    estimatedTime: '20 minutes',
    type: 'learning'
  };
}

/**
 * Get complete first day workspace data
 */
export function getFirstDayWorkspace(user) {
  const onboardingData = user.onboardingData || {};
  
  return {
    isFirstDay: user.isFirstDay ?? true,
    pipooMessage: generateFirstDayMessage(onboardingData),
    insight: generateInsightCard(onboardingData, user.role),
    mainTask: generateFirstTask(onboardingData),
    optionalTask: generateOptionalTask(onboardingData)
  };
}