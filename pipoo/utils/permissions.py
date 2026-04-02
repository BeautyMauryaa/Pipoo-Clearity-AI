"""
Permissions Handler - Android Runtime Permissions
"""
from config.settings import IS_ANDROID, DEBUG_MODE


class PermissionsHandler:
    """
    Handle Android runtime permissions
    """
    
    def __init__(self):
        self.permissions_granted = {}
        
        if IS_ANDROID:
            from android.permissions import request_permissions, check_permission, Permission
            self.request_permissions = request_permissions
            self.check_permission = check_permission
            self.Permission = Permission
        else:
            # Desktop - permissions not needed
            self.request_permissions = None
            self.check_permission = None
            self.Permission = None
    
    def request_microphone_permission(self, callback=None):
        """
        Request microphone permission (Android)
        
        Args:
            callback: Function to call after permission result
        """
        if not IS_ANDROID:
            # Desktop - assume permission granted
            if callback:
                callback(True)
            return True
        
        if DEBUG_MODE:
            print("📱 Requesting microphone permission...")
        
        try:
            # Check if already granted
            if self.check_permission(self.Permission.RECORD_AUDIO):
                if DEBUG_MODE:
                    print("✅ Microphone permission already granted")
                if callback:
                    callback(True)
                return True
            
            # Request permission
            def permission_callback(permissions, grant_results):
                granted = all(grant_results)
                self.permissions_granted['microphone'] = granted
                
                if DEBUG_MODE:
                    status = "✅ granted" if granted else "❌ denied"
                    print(f"Microphone permission {status}")
                
                if callback:
                    callback(granted)
            
            self.request_permissions(
                [self.Permission.RECORD_AUDIO],
                permission_callback
            )
            
        except Exception as e:
            if DEBUG_MODE:
                print(f"❌ Permission request error: {e}")
            if callback:
                callback(False)
            return False
    
    def check_microphone_permission(self):
        """
        Check if microphone permission is granted
        
        Returns:
            bool: True if granted
        """
        if not IS_ANDROID:
            return True  # Desktop - assume granted
        
        try:
            return self.check_permission(self.Permission.RECORD_AUDIO)
        except:
            return False
    
    def request_storage_permission(self, callback=None):
        """
        Request storage permission (Android)
        
        Args:
            callback: Function to call after permission result
        """
        if not IS_ANDROID:
            if callback:
                callback(True)
            return True
        
        if DEBUG_MODE:
            print("📱 Requesting storage permission...")
        
        try:
            # Check if already granted
            if self.check_permission(self.Permission.WRITE_EXTERNAL_STORAGE):
                if DEBUG_MODE:
                    print("✅ Storage permission already granted")
                if callback:
                    callback(True)
                return True
            
            # Request permission
            def permission_callback(permissions, grant_results):
                granted = all(grant_results)
                self.permissions_granted['storage'] = granted
                
                if DEBUG_MODE:
                    status = "✅ granted" if granted else "❌ denied"
                    print(f"Storage permission {status}")
                
                if callback:
                    callback(granted)
            
            self.request_permissions(
                [self.Permission.WRITE_EXTERNAL_STORAGE, self.Permission.READ_EXTERNAL_STORAGE],
                permission_callback
            )
            
        except Exception as e:
            if DEBUG_MODE:
                print(f"❌ Permission request error: {e}")
            if callback:
                callback(False)
            return False