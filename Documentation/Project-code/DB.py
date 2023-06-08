import sqlite3

class DB:
    def __init__(self):
        # Connect to the database
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        # Create the table if it doesn't exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users(
                username TEXT,
                password TEXT,
                type TEXT
            )
        """)

         # Create check_ins
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS checkins(
                name TEXT,
                surname TEXT,
                age INT,
                room TEXT,
                arrival_date DATETIME,
                departure_date  DATETIME
            )
        """)

          # Create check_ins
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS requests(
                room TEXT,
                request TEXT,
                
            )
        """)

        # Insert data into the table
        cursor.execute("""
            INSERT INTO users VALUES ('admin', 'password', 'empl')
        """)

        # Commit the changes to the database
        conn.commit()



    
        # Close the database connection
        cursor.close()
        conn.close()

# Create an instance of the DB class

