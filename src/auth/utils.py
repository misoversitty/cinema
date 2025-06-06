import hashlib

def hash_password(password: str):
    return hashlib.sha256(bytes(password, encoding='utf-8')).hexdigest()
