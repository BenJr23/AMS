from DATABASEFUNCTION.Database_seeder import create_database
from DATABASEFUNCTION.Admin_Acc import create_admin_account
from DATABASEFUNCTION.Admin_Acc import create_attendance_account
from Controller.Controller import start_app


# Call the function to create the database and tables
create_database()
create_admin_account()
create_attendance_account()
app = start_app()
