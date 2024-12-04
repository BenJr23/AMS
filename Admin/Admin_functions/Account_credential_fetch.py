import sqlite3
from DATABASEFUNCTION.Database_path_function import database_path_locator


def user_credentials(user_id) -> tuple[str, str | None]:
    db_file = database_path_locator()


    # Connect to the database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    cursor.execute("SELECT FName, LName FROM EMPLOYEE WHERE EmployeeID = ?", (user_id,))
    result = cursor.fetchone()
    first_name, last_name = result
    return first_name, last_name
