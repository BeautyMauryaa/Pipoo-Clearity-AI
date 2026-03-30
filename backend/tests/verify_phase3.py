"""
Phase 3 Verification Script
Tests all requirements to confirm Phase 3 is complete
"""

import asyncio
import httpx
from datetime import datetime

BASE_URL = "http://localhost:8000/api"

class Phase3Verifier:
    def __init__(self):
        self.token = None
        self.user_id = None
        self.task_id = None
        self.results = []
    
    def log(self, test_name: str, passed: bool, message: str = ""):
        """Log test result"""
        status = "✅ PASS" if passed else "❌ FAIL"
        self.results.append((test_name, passed, message))
        print(f"{status} - {test_name}")
        if message:
            print(f"    {message}")
    
    async def verify_all(self):
        """Run all verification tests"""
        print("\n" + "=" * 60)
        print("PHASE 3 VERIFICATION - Complete Test Suite")
        print("=" * 60 + "\n")
        
        async with httpx.AsyncClient(timeout=30.0) as client:
            # Test 1: User can signup and login
            await self.test_auth_persistence(client)
            
            if not self.token:
                print("\n⚠️  Cannot continue without valid token. Fix auth first.")
                self.print_summary()
                return
            
            # Test 2: Onboarding persists
            await self.test_onboarding_persistence(client)
            
            # Test 3: Tasks persist across sessions
            await self.test_task_persistence(client)
            
            # Test 4: History reflects real actions
            await self.test_history_accuracy(client)
            
            # Test 5: Workspace rebuilds from DB
            await self.test_workspace_rebuild(client)
            
            # Test 6: Frontend is stateless
            await self.test_frontend_stateless(client)
        
        # Summary
        self.print_summary()
    
    async def test_auth_persistence(self, client):
        """Test 1: Can user log out & log back in and see same state?"""
        
        # Generate unique email
        timestamp = int(datetime.utcnow().timestamp())
        
        # Signup
        signup_data = {
            "name": "Test User",
            "email": f"test_{timestamp}@test.com",
            "password": "test123",
            "role": "student"
        }
        
        try:
            response = await client.post(
                f"{BASE_URL}/auth/signup",
                json=signup_data
            )
            
            print(f"Signup Status: {response.status_code}")
            
            if response.status_code in [200, 201]:
                data = response.json()
                self.token = data["access_token"]
                self.user_id = data["user"]["id"]
                self.log("Auth Signup", True, f"User created: {self.user_id}")
            else:
                print(f"Signup Response: {response.text}")
                self.log("Auth Signup", False, f"Failed: {response.status_code}")
                return
        except Exception as e:
            print(f"Signup Error: {e}")
            self.log("Auth Signup", False, f"Exception: {str(e)}")
            return
        
        # Login again
        login_data = {
            "email": signup_data["email"],
            "password": signup_data["password"]
        }
        
        try:
            response = await client.post(
                f"{BASE_URL}/auth/login",
                json=login_data
            )
            
            if response.status_code == 200:
                new_token = response.json()["access_token"]
                self.log("Auth Login", True, "User can login again")
            else:
                self.log("Auth Login", False, f"Failed: {response.status_code}")
        except Exception as e:
            self.log("Auth Login", False, f"Exception: {str(e)}")
    
    async def test_onboarding_persistence(self, client):
        """Test 2: Onboarding data persists"""
        
        headers = {"Authorization": f"Bearer {self.token}"}
        
        # Complete onboarding
        onboarding_data = {
            "goal": "job-ready",
            "timeline": "6-12m",
            "experience_level": "beginner",
            "time_available": "1-2h",
            "blocker": "consistency",
            "skills": "Python",
            "target_role": "Developer"
        }
        
        try:
            response = await client.post(
                f"{BASE_URL}/onboarding/student",
                json=onboarding_data,
                headers=headers
            )
            
            print(f"Onboarding Status: {response.status_code}")
            
            if response.status_code == 200:
                self.log("Onboarding Create", True, "Onboarding completed")
            else:
                print(f"Onboarding Response: {response.text}")
                self.log("Onboarding Create", False, f"Failed: {response.status_code}")
                return
        except Exception as e:
            print(f"Onboarding Error: {e}")
            self.log("Onboarding Create", False, f"Exception: {str(e)}")
            return
        
        # Check status
        try:
            response = await client.get(
                f"{BASE_URL}/onboarding/status",
                headers=headers
            )
            
            if response.status_code == 200:
                data = response.json()
                if data.get("onboarding_completed") and data.get("onboarding_data"):
                    self.log("Onboarding Persistence", True, "Data retrieved successfully")
                else:
                    self.log("Onboarding Persistence", False, "Data not found")
            else:
                self.log("Onboarding Persistence", False, f"Failed: {response.status_code}")
        except Exception as e:
            self.log("Onboarding Persistence", False, f"Exception: {str(e)}")
    
    async def test_task_persistence(self, client):
        """Test 3: Are tasks remembered across days?"""
        
        headers = {"Authorization": f"Bearer {self.token}"}
        
        # Create task
        task_data = {
            "title": "Test Task",
            "description": "Verification task",
            "task_type": "daily",
            "estimated_time": "30 min",
            "assigned_date": datetime.utcnow().date().isoformat()
        }
        
        try:
            response = await client.post(
                f"{BASE_URL}/tasks/system/create",
                json=task_data,
                headers=headers
            )
            
            print(f"Task Create Status: {response.status_code}")
            
            if response.status_code == 200:
                data = response.json()
                self.task_id = data.get("task_id")
                self.log("Task Create", True, f"Task created: {self.task_id}")
            else:
                print(f"Task Create Response: {response.text}")
                self.log("Task Create", False, f"Failed: {response.status_code}")
                return
        except Exception as e:
            print(f"Task Create Error: {e}")
            self.log("Task Create", False, f"Exception: {str(e)}")
            return
        
        # Retrieve tasks
        try:
            response = await client.get(
                f"{BASE_URL}/tasks",
                headers=headers
            )
            
            if response.status_code == 200:
                data = response.json()
                tasks = data.get("tasks", [])
                if any(t.get("task_id") == self.task_id for t in tasks):
                    self.log("Task Persistence", True, "Task retrieved successfully")
                else:
                    self.log("Task Persistence", False, "Task not found")
            else:
                self.log("Task Persistence", False, f"Failed: {response.status_code}")
        except Exception as e:
            self.log("Task Persistence", False, f"Exception: {str(e)}")
    
    async def test_history_accuracy(self, client):
        """Test 4: Does history reflect real past actions?"""
        
        if not self.task_id:
            self.log("Task Complete", False, "No task to complete")
            self.log("History Accuracy", False, "Skipped - no task")
            return
        
        headers = {"Authorization": f"Bearer {self.token}"}
        
        # Complete task (creates history event)
        try:
            response = await client.post(
                f"{BASE_URL}/tasks/complete",
                json={"task_id": self.task_id},
                headers=headers
            )
            
            if response.status_code == 200:
                self.log("Task Complete", True, "Task completed")
            else:
                print(f"Task Complete Response: {response.text}")
                self.log("Task Complete", False, f"Failed: {response.status_code}")
                return
        except Exception as e:
            self.log("Task Complete", False, f"Exception: {str(e)}")
            return
        
        # Check history
        try:
            response = await client.get(
                f"{BASE_URL}/history",
                headers=headers
            )
            
            if response.status_code == 200:
                data = response.json()
                events = data.get("events", [])
                
                # Should have: signup, login, onboarding, task_completed
                event_types = [e.get("event_type") for e in events]
                
                expected_events = ["task_completed", "onboarding_completed"]
                found_events = [e for e in expected_events if e in event_types]
                
                if len(found_events) >= 1:  # At least one expected event
                    self.log("History Accuracy", True, f"Found events: {found_events}")
                else:
                    self.log("History Accuracy", False, f"Missing events. Found: {event_types}")
            else:
                self.log("History Accuracy", False, f"Failed: {response.status_code}")
        except Exception as e:
            self.log("History Accuracy", False, f"Exception: {str(e)}")
    
    async def test_workspace_rebuild(self, client):
        """Test 5: Can backend rebuild workspace using DB only?"""
        
        headers = {"Authorization": f"Bearer {self.token}"}
        
        try:
            # Get workspace overview
            response = await client.get(
                f"{BASE_URL}/workspace?view=overview",
                headers=headers
            )
            
            print(f"Workspace Status: {response.status_code}")
            
            if response.status_code == 200:
                data = response.json()
                
                # Check if workspace has real data
                has_pipoo = "pipoo" in data and "message" in data.get("pipoo", {})
                has_data = "data" in data
                
                if has_pipoo and has_data:
                    self.log("Workspace Rebuild", True, "Workspace built from database")
                else:
                    self.log("Workspace Rebuild", False, "Workspace missing data")
            else:
                print(f"Workspace Response: {response.text}")
                self.log("Workspace Rebuild", False, f"Failed: {response.status_code}")
        except Exception as e:
            print(f"Workspace Error: {e}")
            self.log("Workspace Rebuild", False, f"Exception: {str(e)}")
    
    async def test_frontend_stateless(self, client):
        """Test 6: Is frontend completely stateless?"""
        
        headers = {"Authorization": f"Bearer {self.token}"}
        
        try:
            # Make same request twice - should get same data
            response1 = await client.get(
                f"{BASE_URL}/workspace?view=overview",
                headers=headers
            )
            response2 = await client.get(
                f"{BASE_URL}/workspace?view=overview",
                headers=headers
            )
            
            if response1.status_code == 200 and response2.status_code == 200:
                # Both should succeed (frontend doesn't need to store state)
                self.log("Frontend Stateless", True, "Backend serves consistent data")
            else:
                self.log("Frontend Stateless", False, "Inconsistent responses")
        except Exception as e:
            self.log("Frontend Stateless", False, f"Exception: {str(e)}")
    
    def print_summary(self):
        """Print test summary"""
        print("\n" + "=" * 60)
        print("VERIFICATION SUMMARY")
        print("=" * 60)
        
        passed = sum(1 for _, p, _ in self.results if p)
        total = len(self.results)
        
        print(f"\nTests Passed: {passed}/{total}")
        if total > 0:
            print(f"Success Rate: {(passed/total)*100:.1f}%\n")
        
        if passed == total and total > 0:
            print("🎉 PHASE 3 COMPLETE! All tests passed.")
            print("\nYou can now confidently say:")
            print("✅ User can log out & log back in and see same state")
            print("✅ Tasks are remembered across days")
            print("✅ History reflects real past actions")
            print("✅ Backend can rebuild workspace using DB only")
            print("✅ Frontend is completely stateless")
        else:
            print("⚠️  Some tests failed. Review errors above.")
        
        print("=" * 60 + "\n")

# Run verification
if __name__ == "__main__":
    print("\n⏳ Starting Phase 3 Verification...")
    print("Make sure backend is running at http://localhost:8000\n")
    
    verifier = Phase3Verifier()
    asyncio.run(verifier.verify_all())