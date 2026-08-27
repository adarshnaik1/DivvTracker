from pwdlib import PasswordHash

password_hasher= PasswordHash.recommended()

def hash_password(password:str):
    pwd_hashed_value= password_hasher.hash(password)
    return pwd_hashed_value


def verify_password(entered_password:str, hashed_password:str):
   
    is_verified = password_hasher.verify(entered_password,hashed_password)
    if is_verified:
        return True
    return False

