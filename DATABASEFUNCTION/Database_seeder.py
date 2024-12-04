import sqlite3
import os

def create_database():
    if os.path.exists('AMS.db'):
        print("Database already exists. Skipping creation.")
        return

    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('AMS.db')
    cursor = conn.cursor()

    # Create the EMPLOYEE table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS EMPLOYEE (
        EmployeeID INTEGER PRIMARY KEY AUTOINCREMENT,
        FName NVARCHAR(50) NOT NULL,
        LName NVARCHAR(50) NOT NULL,
        Email NVARCHAR(50) NOT NULL,
        Hashpassword NVARCHAR(64) NOT NULL,
        Hash NVARCHAR(64) NOT NULL,
        ContactNo NUMERIC NOT NULL,
        Role NVARCHAR(50),
        CreatedBy INT,
        Softdelete BOOLEAN DEFAULT 0,
        FOREIGN KEY (CreatedBy) REFERENCES EMPLOYEE(EmployeeID),
        UNIQUE (FName, LName, Email)
    )
    ''')

    # Create the ATTENDANCE table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ATTENDANCE (
        TimeIn DATE NOT NULL,
        TimeOut DATE,
        EmployeeID INTEGER NOT NULL,
        EmpName NVARCHAR(50),
        Softdelete BOOLEAN DEFAULT 0,
        FOREIGN KEY (EmployeeID) REFERENCES EMPLOYEE(EmployeeID)
    )
    ''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()

    print("Database and tables created successfully.")