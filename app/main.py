import psycopg2
from psycopg2 import OperationalError

try:
    # Establish the connection
    conn = psycopg2.connect(
        database="docker_db",
        user="app",
        password="docker",
        host="localhost",  # Use 'localhost' or the IP address of your database container
        port="5432"
    )

    # Create a cursor
    cur = conn.cursor()

    # Execute a statement
    cur.execute("SELECT version()")
    
    # Fetch the result
    db_version = cur.fetchone()[0]
    print("Connected to PostgreSQL version:", db_version)

except OperationalError as e:
    print("Error:", e)
finally:
    # Close the cursor and connection (regardless of success or failure)
    if cur:
        cur.close()
    if conn:
        conn.close()
