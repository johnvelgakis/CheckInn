import sqlite3

def drop_all_tables():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    # Get the list of table names in the database
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    # Drop each table in the database
    for table in tables:
        table_name = table[0]
        cursor.execute(f"DROP TABLE {table_name};")

    connection.commit()
    connection.close()

# Call the function to drop all tables
drop_all_tables()
