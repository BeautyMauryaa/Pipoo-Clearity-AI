// src/context/AuthContext.jsx
'use client';

import React, { createContext, useContext, useState, useEffect } from 'react';
import { mockLogin, mockSignup } from '@/lib/auth';

const AuthContext = createContext();

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true); // Start with true to check localStorage
  const [error, setError] = useState(null);

  // Load user from localStorage on mount
  useEffect(() => {
    const storedUser = localStorage.getItem('user');
    if (storedUser) {
      try {
        const parsedUser = JSON.parse(storedUser);
        setUser(parsedUser);
      } catch (err) {
        console.error('Failed to parse stored user:', err);
        localStorage.removeItem('user');
      }
    }
    setLoading(false);
  }, []);

  const login = async (email, password) => {
    setLoading(true);
    setError(null);
    
    try {
      console.log('AuthContext login called');
      const result = await mockLogin(email, password);
      console.log('mockLogin result:', result);
      
      if (result.success) {
        setUser(result.user);
        // mockLogin already saves to localStorage, no need to do it again
        console.log('User logged in:', result.user);
        return { success: true };
      } else {
        setError(result.error);
        return { success: false, error: result.error };
      }
    } catch (err) {
      console.error('Login error:', err);
      setError('Something went wrong. Try again.');
      return { success: false, error: 'Something went wrong. Try again.' };
    } finally {
      setLoading(false);
    }
  };

  const signup = async (name, email, password, role) => {
    setLoading(true);
    setError(null);
    
    try {
      console.log('AuthContext signup called');
      const result = await mockSignup(name, email, password, role);
      console.log('mockSignup result:', result);
      
      if (result.success) {
        setUser(result.user);
        // mockSignup already saves to localStorage, no need to do it again
        console.log('User signed up:', result.user);
        return { success: true };
      }
    } catch (err) {
      console.error('Signup error:', err);
      setError('Something went wrong. Try again.');
      return { success: false, error: 'Something went wrong. Try again.' };
    } finally {
      setLoading(false);
    }
  };

  const logout = () => {
    setUser(null);
    setError(null);
    localStorage.removeItem('user');
    localStorage.removeItem('userData');
  };

  // Function to update user data (useful for onboarding completion)
  const updateUser = (updates) => {
    if (user) {
      const updatedUser = { ...user, ...updates };
      setUser(updatedUser);
      localStorage.setItem('user', JSON.stringify(updatedUser));
    }
  };

  // Check onboarding status
  const isOnboardingComplete = () => {
    return user?.onboardingCompleted === true;
  };

  const value = {
    user,
    loading,
    error,
    login,
    signup,
    logout,
    updateUser,
    isOnboardingComplete,
    isAuthenticated: !!user
  };

  return (
    <AuthContext.Provider value={value}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within AuthProvider');
  }
  return context;
}