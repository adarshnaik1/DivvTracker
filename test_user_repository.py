from app.repositories.user_repository import UserRepository
from app.services.auth_service import AuthService
user  = UserRepository()
#user_id=user.create_user("adarshnaik@mclaren.com","abc-123")

user_info=user.get_user_by_email("adarshnaik@mclaren.com")

#print(user_id)
print("-"*60)
print(user_info)

auth= AuthService()

auth.register_user("adarshnaik@mclaren.com", "1234")