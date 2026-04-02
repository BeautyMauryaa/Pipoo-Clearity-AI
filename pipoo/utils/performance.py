"""
Performance Monitor - Track and optimize performance
"""
import time
import psutil
import os
from utils.logger import logger
from config.settings import DEBUG_MODE


class PerformanceMonitor:
    """
    Monitor app performance and resource usage
    """
    
    def __init__(self):
        self.start_time = time.time()
        self.operation_times = {}
    
    def start_timer(self, operation_name):
        """Start timing an operation"""
        self.operation_times[operation_name] = time.time()
    
    def end_timer(self, operation_name, log_threshold=1.0):
        """
        End timing and log if exceeds threshold
        
        Args:
            operation_name: Name of operation
            log_threshold: Log if operation takes longer than this (seconds)
        """
        if operation_name not in self.operation_times:
            return 0
        
        elapsed = time.time() - self.operation_times[operation_name]
        
        if elapsed > log_threshold:
            logger.warning(f"Slow operation: {operation_name} took {elapsed:.2f}s")
        elif DEBUG_MODE:
            logger.debug(f"Operation: {operation_name} took {elapsed:.2f}s")
        
        del self.operation_times[operation_name]
        return elapsed
    
    def get_memory_usage(self):
        """Get current memory usage"""
        try:
            process = psutil.Process(os.getpid())
            memory_info = process.memory_info()
            return {
                'rss_mb': memory_info.rss / 1024 / 1024,  # Resident Set Size
                'vms_mb': memory_info.vms / 1024 / 1024,  # Virtual Memory Size
            }
        except:
            return {'rss_mb': 0, 'vms_mb': 0}
    
    def log_memory_usage(self):
        """Log current memory usage"""
        memory = self.get_memory_usage()
        logger.info(f"Memory: RSS={memory['rss_mb']:.1f}MB, VMS={memory['vms_mb']:.1f}MB")
    
    def get_uptime(self):
        """Get app uptime in seconds"""
        return time.time() - self.start_time
    
    def optimize_database(self, db_path):
        """Optimize SQLite database"""
        try:
            import sqlite3
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            # Vacuum database (reclaim space)
            cursor.execute('VACUUM')
            
            # Analyze database (update statistics)
            cursor.execute('ANALYZE')
            
            conn.commit()
            conn.close()
            
            logger.info("Database optimized successfully")
            return True
        except Exception as e:
            logger.error(f"Database optimization failed: {e}")
            return False


# Global performance monitor
perf_monitor = PerformanceMonitor()