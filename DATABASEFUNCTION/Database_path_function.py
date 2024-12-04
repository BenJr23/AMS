import os

def database_path_locator(relative_path_to_db="../AMS.db"):
    """
    Locates the database file from the base path of the current script.

    :param relative_path_to_db: The relative path to the database file.
    :return: The absolute path to the database file.
    :raises FileNotFoundError: If the database file does not exist.
    """
    base_path = os.path.dirname(os.path.abspath(__file__))
    db_file = os.path.join(base_path, relative_path_to_db)

    # Check if the database exists
    if not os.path.exists(db_file):
        raise FileNotFoundError(f"Database does not exist at {db_file}. Run the database setup first.")
    return db_file