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

        ##view the table check ins
       
        
        from tkinter import ttk

        # Assuming this code is within a class or a method
        # Create a Treeview widget
        self.treeview = ttk.Treeview(self.root)

        # Define the column titles as a separate list
        column_titles = ['Name', 'Surname', 'Age', 'Room', 'Arrival Date', 'Departure Date']

        # Configure the Treeview with columns
        self.treeview['columns'] = column_titles

        # Format column headers
        for col in column_titles:
            self.treeview.heading(col, text=col, anchor=tk.CENTER)
            self.treeview.column(col, anchor=tk.CENTER)

        # Insert each row into the Treeview
        for row in rows:
            self.treeview.insert('', tk.END, values=row)

        # Create a vertical scrollbar for the Treeview
        vsb = ttk.Scrollbar(self.root, orient='vertical', command=self.treeview.yview)
        self.treeview.configure(yscroll=vsb.set)
        vsb.pack(side='right', fill='y')

        # Pack the Treeview
        self.treeview.pack(pady=12, padx=10)



        # Create a button to go back to the home window
        self.back_button = customtkinter.CTkButton(master=self.root, text="Back", command=self.to_home)
        self.back_button.pack(pady=12, padx=10)

        self.root.mainloop()
        

    def to_home(self):
        self.root.destroy()
        from Home import Home  ##import here to avoid circular import error
        home_window = Home()
        home_window.root.mainloop()



