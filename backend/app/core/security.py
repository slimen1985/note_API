import bcrypt


def get_password_hash(password: str) -> str:
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password.decode('utf-8')


def verify_password(plain_password: str, hashed_password: str) -> bool:
    encoded_password = plain_password.encode('utf-8')
    encoded_hash = hashed_password.encode('utf-8')
    return bcrypt.checkpw(encoded_password, encoded_hash)