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


        #Reservations
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS reservations (
        name TEXT,
        surname TEXT,
        age INTEGER,
        num_people INTEGER,
        arrival_date TEXT,
        departure_date TEXT
    )
''')

        #Housekeeping
        cursor.execute('''
         CREATE TABLE IF NOT EXISTS rooms (
        room_number INTEGER PRIMARY KEY,
        condition TEXT CHECK(condition IN ('clean', 'dirty'))
    )
''')     
        #requests
        cursor.execute('''
    CREATE TABLE IF NOT EXISTS requests (
        room_number INTEGER,
        request TEXT,
        description TEXT
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
''')
                       
        # Insert values into the rooms table
        for room_number in range(1, 201):
            cursor.execute("INSERT INTO rooms (room_number, condition) VALUES (?, 'clean')", (room_number,))
            conn.commit()


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

