import sqlite3
import customtkinter
import tkinter as tk

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

class PrintCheckIns:
    def __init__(self):
        # Connect to the database
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        # Retrieve data from the checkins table
        cursor.execute("SELECT * FROM checkins")
        rows = cursor.fetchall()

        # Close the database connection
        cursor.close()
        conn.close()

        self.root = tk.Tk()

        # Create a Listbox widget
        self.listbox = tk.Listbox(self.root, width=60)

        # Insert each row into the Listbox
        for row in rows:
            self.listbox.insert(tk.END, row)

        # Create a scrollbar for the Listbox
        scrollbar = tk.Scrollbar(self.root)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configure the Listbox to use the scrollbar
        self.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)

        # Pack the Listbox
        self.listbox.pack(pady=12, padx=10)

        # Create a button to go back to the home window
        self.back_button = customtkinter.CTkButton(master=self.root, text="Back", command=self.to_home)
        self.back_button.pack(pady=12, padx=10)

        self.root.mainloop()
        

    def to_home(self):
        self.root.destroy()
        from Home import Home  ##import here to avoid circular import error
        home_window = Home()
        home_window.root.mainloop()



