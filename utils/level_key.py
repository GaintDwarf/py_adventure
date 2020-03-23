import hashlib

def get_hash(key: str):
    return hashlib.sha384(str(key).encode()).digest().hex()[:10]

