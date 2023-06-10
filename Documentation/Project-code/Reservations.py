import customtkinter
from tkinter import ttk
import sqlite3
import tkinter as tk

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

class Reservations:
    def __init__(self):
        self.root = customtkinter.CTk()
        self.root.geometry("1200x900")
        self.frame = customtkinter.CTkFrame(master=self.root)
        self.frame.pack(pady=0, padx=0, fill="both", expand=True)
         

        self.name_label = customtkinter.CTkLabel(master=self.frame, text="Reservations")
        self.name_label.pack(pady=12, padx=10)

       # Create a Treeview widget
        self.treeview = ttk.Treeview(self.frame)
        
        # Define the column titles as a separate list
        column_titles = ['Name', 'Surname', 'Age', 'Number of People', 'Arrival Date', 'Departure Date']

        # Configure the Treeview with columns
        self.treeview['columns'] = column_titles

        # Format column headers
        for col in column_titles:
            self.treeview.heading(col, text=col, anchor=tk.CENTER)
            self.treeview.column(col, anchor=tk.CENTER)

        # Insert each row into the Treeview
        rows = self.fetch_rows_from_database()
        for row in rows:
            self.treeview.insert('', tk.END, values=row)

        # Create a vertical scrollbar for the Treeview
        vsb = ttk.Scrollbar(self.frame, orient='vertical', command=self.treeview.yview)
        self.treeview.configure(yscroll=vsb.set)
        vsb.pack(side='right', fill='y')

        # Pack the Treeview
        self.treeview.pack(pady=12, padx=10)




         ##button that takes the user back to home window
        self.back_button = customtkinter.CTkButton(master=self.frame, text="Back", command=self.to_home) 
        self.back_button.pack(pady=12, padx=10) 

    
    
    def fetch_rows_from_database(self):
        # Establish a connection to the database
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        # Fetch all rows from the checkins table
        cursor.execute("SELECT * FROM reservations")
        rows = cursor.fetchall()

        connection.close()

        return rows   



    


    def to_home(self):
        self.root.destroy()
        from Home import Home     ##import here to avoid circular import error
        home_window = Home()
        home_window.root.mainloop()
