import customtkinter
from tkinter import ttk
import sqlite3
import tkinter as tk

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

class CheckOut:
    def __init__(self):
        self.root = customtkinter.CTk()
        self.root.geometry("1200x900")
        self.frame = customtkinter.CTkFrame(master=self.root)
        self.frame.pack(pady=0, padx=0, fill="both", expand=True)

        self.name_label = customtkinter.CTkLabel(master=self.frame, text="Select Room to Check Out")
        self.name_label.pack(pady=12, padx=10)

        # Create a Treeview widget
        self.treeview = ttk.Treeview(self.frame)

        # Define the column titles as a separate list
        column_titles = ['Name', 'Surname', 'Age', 'Room', 'Arrival Date', 'Departure Date']

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

        # Create a Check Out button
        checkout_button = customtkinter.CTkButton(master=self.frame, text="Check Out", command=self.checkout_row)
        checkout_button.pack()

        # button that takes the user back to the home window
        self.back_button = customtkinter.CTkButton(master=self.frame, text="Back", command=self.to_home)
        self.back_button.pack(pady=12, padx=10)

    def fetch_rows_from_database(self):
        # Establish a connection to the database
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        # Fetch all rows from the checkins table
        cursor.execute("SELECT * FROM checkins")
        rows = cursor.fetchall()

        connection.close()

        return rows

    def checkout_row(self):
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
        cursor.execute("DELETE FROM checkins WHERE name=? AND surname=? AND age=? AND room=? AND arrival_date=? AND departure_date=?",
                       row_values)

        connection.commit()
        connection.close()

    def to_home(self):
        self.root.destroy()
        from Home import Home  # import here to avoid circular import error
        home_window = Home()
        home_window.root.mainloop()