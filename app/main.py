import psycopg2
from psycopg2 import OperationalError
from retrying import retry

@retry(wait_fixed=2000, stop_max_attempt_number=10)  # Wait 2 seconds between retries, try up to 10 times
def connect_with_retry():
    conn = psycopg2.connect(
        database="docker_db",
        user="app",
        password="docker",
        host="localhost",  # Use the service name as the hostname
        port="5432"
    )
    return conn

try:
    # Attempt to connect with retry mechanism
    db_connection = connect_with_retry()
    print("Connected to the database!")
    # Create a cursor
    cur = db_connection.cursor()

    # Execute a statement
    cur.execute("SELECT version()")

    # Fetch the result
    db_version = cur.fetchone()[0]
    print("Connected to PostgreSQL version:", db_version)

except OperationalError as e:
    print("Error:", e)
finally:
    # Close the cursor and connection (regardless of success or failure)
    cur.close()
    db_connection.close()
    