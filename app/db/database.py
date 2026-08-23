from app.config import DATABASE_URL
from psycopg_pool import ConnectionPool

pool = ConnectionPool(DATABASE_URL)


#sample code to test if the connection has happened
with pool.connection() as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT 1")
        result= cursor.fetchone()

print(result)

