# utils.py (Vulnerable)
import hashlib

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()  # ¡MD5 es inseguro!