import sqlite3
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

class PrintCheckIns:
    def __init__(self):
        # Connect to the database
        conn = sqlite3.connect('DB.db')
        cursor = conn.cursor()

        # Retrieve data from the checkins table
        cursor.execute("SELECT * FROM checkins")
        rows = cursor.fetchall()

        # Print the rows
        for row in rows:
            print(row)

        # Close the database connection
        cursor.close()
        conn.close()


##button that takes the user back to home window
        self.back_button = customtkinter.CTkButton(master=self.frame, text="Back", command=self.to_home) 
        self.back_button.pack(pady=12, padx=10) 
    


    def to_home(self):
        self.root.destroy()
        from Home import Home     ##import here to avoid circular import error
        home_window = Home()
        home_window.root.mainloop()