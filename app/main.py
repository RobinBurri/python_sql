from pathlib import Path

import psycopg2
from psycopg2 import OperationalError
from retrying import retry


db_connection = None
cur = None


def read_sql_file(file_path: str) -> str:
    """Read SQL file"""
    return Path(file_path).read_text()


@retry(
    wait_fixed=2000, stop_max_attempt_number=10
)  # Wait 2 seconds between retries, try up to 10 times
def connect_with_retry():
    conn = psycopg2.connect(
        database="docker_db",
        user="app",
        password="docker",
        host="localhost",  # Use the service name as the hostname
        port="5432",
    )
    return conn


try:
    db_connection = connect_with_retry()

    cur = db_connection.cursor()

    # rawL_sql = read_sql_file(
    #     "/Users/robin/Desktop/python_sql/sql/create_users_tables.sql"
    # )
    # cur.execute(rawL_sql)

    rawL_sql = read_sql_file("../sql/insert_user.sql")
    insert_valuses = ('robin burri', 25000, 'self-employed')
    cur.execute(rawL_sql, insert_valuses)
    inserted_rows = cur.fetchone()
    print("new row inserted: ", inserted_rows)
    # Commit the changes
    db_connection.commit()


except OperationalError as e:
    print("Error:", e)

finally:
    if cur is not None:
        cur.close()
    if db_connection is not None:
        db_connection.close()
