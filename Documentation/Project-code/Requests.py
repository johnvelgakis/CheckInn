import customtkinter
from tkinter import ttk
import sqlite3
import tkinter as tk


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

class Requests:
    def __init__(self):
        self.root = customtkinter.CTk()
        self.root.geometry("1300x731")
        self.frame = customtkinter.CTkFrame(master=self.root)
        self.frame.pack(pady=0, padx=0, fill="both", expand=True)

        self.name_label = customtkinter.CTkLabel(master=self.frame, text="Ongoing Reservations")
        self.name_label.pack(pady=12, padx=10)

        
        # Create a Treeview widget
        self.treeview = ttk.Treeview(self.frame)

        # Define the column titles as a separate list
        column_titles = ['Room ', 'Request','Description']

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

         # Create a button to go back to the home window
        self.completerequest_button = customtkinter.CTkButton(master=self.root,fg_color=("black", "green"), text="Done", command=self.complete_request)
        self.completerequest_button.pack(pady=12, padx=10)

        # Create a button to go back to the home window
        self.back_button = customtkinter.CTkButton(master=self.root, text="Back", command=self.to_home)
        self.back_button.pack(pady=12, padx=10)

    def complete_request(self):
        # Get the selected item
        selected_item = self.treeview.focus()

        if selected_item:
            # Retrieve the values of the selected row
            values = self.treeview.item(selected_item)['values']

            # Remove the row from the Treeview
            self.treeview.delete(selected_item)

            # Remove the row from the database
            self.remove_row_from_database(values)

    def remove_row_from_database(self, row_values):
        # Establish a connection to the database
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        # Remove the row from the database based on the row values
        cursor.execute("DELETE FROM requests WHERE room=? AND request=? AND description=?",
                       row_values)  

        connection.commit()
        connection.close()

    def fetch_rows_from_database(self):
        # Establish a connection to the database
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        # Fetch all rows from the checkins table
        cursor.execute("SELECT * FROM requests")
        rows = cursor.fetchall()

        connection.close()

        return rows   

    def to_home(self):
        self.root.destroy()
        from Home import Home  ##import here to avoid circular import error
        home_window = Home()
        home_window.root.mainloop()



