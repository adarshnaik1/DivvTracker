from app.schemas.auth import RegisterRequest

user = RegisterRequest(
    email="adarshnayak108@gmail.com",
    password="abscfdfj"
)
type(user)

print(user)
print(user.email)
print(user.password)