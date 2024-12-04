import sqlite3
import os
from DATABASEFUNCTION.Admin_Acc import hash_password
from DATABASEFUNCTION.Database_path_function import database_path_locator


def login_validation(email: str, password: str) -> tuple[bool, str, int | None]:
    """
    Validates the login credentials of a user.
    :param email: User's email address.
    :param password: User's password.
    :return: A tuple containing (True/False, Role) where Role is None if login fails.
    """
    # Get the base path for the database
    db_file = database_path_locator()

    # Connect to the database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    try:
        # Retrieve the hashed password, salt, and role for the given email
        cursor.execute("SELECT Hashpassword, Hash, Role,EmployeeID FROM EMPLOYEE WHERE Email = ? AND Softdelete = ?", (email, 0))
        result = cursor.fetchone()

        if result is None:
            print("Invalid email or password.")
            return False, None, None

        stored_hashed_password, salt, role, employee_id = result

        # Hash the provided password with the retrieved salt
        hashed_password = hash_password(password, salt)

        # Compare the hashed password with the stored hash
        if hashed_password == stored_hashed_password:
            print("Login successful!")
            return True, role, employee_id  # Return True and the role
        else:
            print("Invalid email or password.")
            return False, None, None
    except sqlite3.Error as e:
        print(f"Error during login validation: {e}")
        return False, None, None
    finally:
        conn.close()