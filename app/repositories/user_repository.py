from app.db.database import pool

class UserRepository:
    def create_user(self,email:str, password_hash:str):
        with pool.connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO users (email, password_hash) values (%s, %s) RETURNING id",
                    (email, password_hash)

                )

                #The database Insert Operation returns a user_id
                user_id = cursor.fetchone()
                if user_id is not None:
                    user_id=user_id[0]
                return user_id