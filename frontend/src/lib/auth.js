// src/lib/auth.js

// Email validation
export const validateEmail = (email) => {
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return regex.test(email);
};

// Password validation (min 8 characters)
export const validatePassword = (password) => {
  return password.length >= 8;
};

// Mock authentication (replace with real API calls later)
export const mockLogin = async (email, password) => {
  // Simulate API call
  await new Promise(resolve => setTimeout(resolve, 1000));
  
  console.log('mockLogin called with:', { email, password });
  
  // Check if user exists in localStorage
  const storedUser = localStorage.getItem('user');
  
  if (storedUser) {
    try {
      const user = JSON.parse(storedUser);
      console.log('Found existing user:', user);
      
      // Check if email matches
      if (user.email === email) {
        return {
          success: true,
          user
        };
      }
    } catch (err) {
      console.error('Failed to parse stored user:', err);
    }
  }
  
  // If no user exists, create a demo user
  const demoUser = {
    id: Date.now().toString(),
    name: 'Demo User',
    email: email,
    role: 'student',
    createdAt: new Date().toISOString(),
    onboardingCompleted: false,
    isFirstDay: false
  };
  
  localStorage.setItem('user', JSON.stringify(demoUser));
  console.log('Created demo user:', demoUser);
  
  return {
    success: true,
    user: demoUser
  };
};

// Mock signup
export const mockSignup = async (name, email, password, role) => {
  // Simulate API call
  await new Promise(resolve => setTimeout(resolve, 1000));
  
  console.log('mockSignup called with:', { name, email, role });
  
  // Create new user object
  const newUser = {
    id: Date.now().toString(),
    name: name,
    email: email,
    role: role,
    createdAt: new Date().toISOString(),
    onboardingCompleted: false,
    isFirstDay: false
  };
  
  // Save to localStorage
  localStorage.setItem('user', JSON.stringify(newUser));
  console.log('User created and saved:', newUser);
  
  return {
    success: true,
    user: newUser
  };
};

// Check if user is authenticated
export const isAuthenticated = () => {
  const storedUser = localStorage.getItem('user');
  return !!storedUser;
};

// Get current user from localStorage
export const getCurrentUser = () => {
  const storedUser = localStorage.getItem('user');
  if (storedUser) {
    try {
      return JSON.parse(storedUser);
    } catch (err) {
      console.error('Failed to parse user:', err);
      return null;
    }
  }
  return null;
};

// Clear user from localStorage
export const clearCurrentUser = () => {
  localStorage.removeItem('user');
  localStorage.removeItem('userData');
  console.log('User cleared from localStorage');
};