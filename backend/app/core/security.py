import bcrypt


def get_password_hash(password: str) -> str:
    salt = bcrypt.gensalt()
    password_hash = bcrypt.hashpw(password.encode("utf-8"), salt)
    return password_hash.decode("utf-8")