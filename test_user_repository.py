from app.repositories.user_repository import UserRepository

user  = UserRepository()
user_id=user.create_user("adarshnaik@mclaren.com","abc-123")

print(user_id)