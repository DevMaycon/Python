import psycopg2

connection = psycopg2.connect(
    host="127.0.0.1",
    database="sqldatabase",
    user="postgres",
    password="12345678",
    port="5432"
)
def get_by_id(id: str):
    with connection.cursor() as conn:
        conn.execute(f"SELECT * FROM users WHERE id={id}")
        return conn.fetchall()
    
