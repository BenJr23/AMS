import sqlite3
import os
import hashlib
import uuid

def hash_password(password: str, salt: str) -> str:
    """
    Hash a password with the provided salt using SHA-256.
    """
    return hashlib.sha256((password + salt).encode()).hexdigest()

def create_admin_account():
    # Admin details
    first_name = "RubenJr"
    last_name = "Bertuso"
    email = "rubenjrtbertuso@gmail.com"
    password = "benjr23"
    contact_no = 9272914369  # No leading 0 for integers
    role = "Admin"

    # Generate a salt and hash the password
    salt = uuid.uuid4().hex  # Generate a unique salt
    hashed_password = hash_password(password, salt)

    # Connect to the database
    db_file = "AMS.db"
    if not os.path.exists(db_file):
        print("Database does not exist. Run the database setup first.")
        return

    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Check if admin account already exists
    cursor.execute("SELECT * FROM EMPLOYEE WHERE Email = ? AND Softdelete = ?", (email, 0))
    if cursor.fetchone():
        print("Admin account already exists.")
        conn.close()
        return

    # Insert admin account into the EMPLOYEE table
    try:
        cursor.execute('''
        INSERT INTO EMPLOYEE (EmployeeID, FName, LName, Email, Hashpassword, Hash, ContactNo, Role, CreatedBy)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (1, first_name, last_name, email, hashed_password, salt, contact_no, role, None))  # CreatedBy is NULL for the first admin
        conn.commit()
        print("Admin account created successfully.")
    except sqlite3.Error as e:
        print(f"Error inserting admin account: {e}")
    finally:
        conn.close()

def create_attendance_account():
    # StaffUI details
    first_name = "AMS"
    last_name = "StaffUI"
    email = "staff@gmail.com"
    password = "staff"
    contact_no = 9272914369  # No leading 0 for integers
    role = "StaffUI"

    # Generate a salt and hash the password
    salt = uuid.uuid4().hex  # Generate a unique salt
    hashed_password = hash_password(password, salt)

    # Connect to the database
    db_file = "AMS.db"
    if not os.path.exists(db_file):
        print("Database does not exist. Run the database setup first.")
        return

    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Check if staff account already exists
    cursor.execute("SELECT * FROM EMPLOYEE WHERE Email = ?", (email,))
    if cursor.fetchone():
        print("StaffUI account already exists.")
        conn.close()
        return

    # Fetch the admin EmployeeID to use as CreatedBy
    cursor.execute("SELECT EmployeeID FROM EMPLOYEE WHERE Role = 'Admin' LIMIT 1")
    admin_record = cursor.fetchone()
    created_by = admin_record[0] if admin_record else None  # Use the first admin EmployeeID or NULL if no admin exists

    # Insert staff account into the EMPLOYEE table
    try:
        cursor.execute('''
        INSERT INTO EMPLOYEE (EmployeeID, FName, LName, Email, Hashpassword, Hash, ContactNo, Role, CreatedBy)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (2, first_name, last_name, email, hashed_password, salt, contact_no, role, created_by))  # CreatedBy references the admin
        conn.commit()
        print("StaffUI account created successfully.")
    except sqlite3.Error as e:
        print(f"Error inserting StaffUI account: {e}")
    finally:
        conn.close()
