from app.repositories.user_repository import UserRepository 
from app.security.password import  hash_password, verify_password
from typing import Any



class AuthService:
    def register_user(self, email:str , password:str )-> Any:
        """
        Accepts Email, password of the user and checks if existing user with the same userId is present
        and creates a user if it doesnt exist
        """
        usr_repo_object = UserRepository()
        user_info =  usr_repo_object.get_user_by_email(email)
        if user_info is not  None :
            raise Exception("User with this email Already Exists")
        
        hashed_password = hash_password(password)

        user_id = usr_repo_object.create_user(email,hashed_password)
        return user_id

        

        

        
        
        

