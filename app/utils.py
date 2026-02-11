from passlib.context import CryptContext

pwd_context = CryptContext(schemes = ["bcrypt"], deprecated="auto")

def hash(password: str) -> str:
   password_bytes = password.encode("utf-8")[:72]
   return pwd_context.hash(password_bytes.decode("utf-8", errors="ignore"))

def verify(plain_password, hashed_password):
   return pwd_context.verify(plain_password, hashed_password)