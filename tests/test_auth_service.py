from app.services.auth_service import AuthService

auth_service = AuthService()
#testing auth service in case where the the new user is created and also when a user already exists

#auth_service.register_user("adarshnaik@mclaren.com","test123")

#testing auth service in case new user is to be created 
auth_service.register_user("adarshnaik@mclarensv.com","test123")