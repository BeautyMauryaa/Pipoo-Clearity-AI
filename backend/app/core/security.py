# app/core/security.py
from datetime import datetime, timedelta
from typing import Optional, Dict
from jose import JWTError, jwt
from passlib.context import CryptContext
from app.core.config import settings

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# ==========================================
# PASSWORD HASHING
# ==========================================

def hash_password(password: str) -> str:
    """
    Hash a plain text password
    NEVER store passwords in plain text
    """
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a plain password against hashed password
    """
    return pwd_context.verify(plain_password, hashed_password)

# ==========================================
# JWT TOKEN CREATION
# ==========================================

def create_access_token(data: Dict, expires_delta: Optional[timedelta] = None) -> str:
    """
    Create a JWT access token
    
    Args:
        data: Dictionary containing user data to encode
        expires_delta: Optional custom expiration time
    
    Returns:
        Encoded JWT token string
    """
    to_encode = data.copy()
    
    # Set expiration
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.JWT_EXPIRATION_MINUTES)
    
    to_encode.update({"exp": expire})
    
    # Create JWT token
    encoded_jwt = jwt.encode(
        to_encode, 
        settings.JWT_SECRET_KEY, 
        algorithm=settings.JWT_ALGORITHM
    )
    
    return encoded_jwt

# ==========================================
# JWT TOKEN VERIFICATION
# ==========================================

def decode_access_token(token: str) -> Optional[Dict]:
    """
    Decode and verify JWT token
    
    Args:
        token: JWT token string
    
    Returns:
        Decoded token data or None if invalid
    """
    try:
        payload = jwt.decode(
            token, 
            settings.JWT_SECRET_KEY, 
            algorithms=[settings.JWT_ALGORITHM]
        )
        return payload
    except JWTError:
        return None

# ==========================================
# TOKEN DATA EXTRACTION
# ==========================================

def get_user_id_from_token(token: str) -> Optional[str]:
    """
    Extract user ID from token
    """
    payload = decode_access_token(token)
    if payload:
        return payload.get("sub")  # 'sub' is standard JWT claim for subject (user ID)
    return None

def get_user_role_from_token(token: str) -> Optional[str]:
    """
    Extract user role from token
    """
    payload = decode_access_token(token)
    if payload:
        return payload.get("role")
    return None