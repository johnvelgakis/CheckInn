import customtkinter
from tkinter import ttk
import sqlite3
import tkinter as tk

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

class Housekeeping:
    def __init__(self):
        self.root = customtkinter.CTk()
        self.root.geometry("1200x900")
        self.frame = customtkinter.CTkFrame(master=self.root)
        self.frame.pack(pady=0, padx=0, fill="both", expand=True)

        self.name_label = customtkinter.CTkLabel(master=self.frame, text="Housekeeping")
        self.name_label.pack(pady=12, padx=10)

        # Create a Treeview widget
        self.treeview = ttk.Treeview(self.frame)

        # Define the column titles as a separate list
        column_titles = ['Room Number', 'Condition']

        # Configure the Treeview with columns
        self.treeview['columns'] = column_titles

        # Format column headers
        for col in column_titles:
            self.treeview.heading(col, text=col, anchor=tk.CENTER)
            self.treeview.column(col, anchor=tk.CENTER)

        # Insert each row into the Treeview
        self.refresh_treeview()

        # Create a vertical scrollbar for the Treeview
        vsb = ttk.Scrollbar(self.frame, orient='vertical', command=self.treeview.yview)
        self.treeview.configure(yscroll=vsb.set)
        vsb.pack(side='right', fill='y')

        # Pack the Treeview
        self.treeview.pack(pady=12, padx=10)

        # Create buttons
        self.clean_button = customtkinter.CTkButton(master=self.frame, text="Cleaned", command=self.set_room_condition_clean)
        self.clean_button.pack(pady=12, padx=10)

        self.dirty_button = customtkinter.CTkButton(master=self.frame, text="Dirty", command=self.set_room_condition_dirty)
        self.dirty_button.pack(pady=12, padx=10)

        self.back_button = customtkinter.CTkButton(master=self.frame, text="Back", command=self.to_home)
        self.back_button.pack(pady=12, padx=10)

    def set_room_condition_clean(self):
        # Get the selected item from the Treeview
        selected_item = self.treeview.focus()
        if selected_item:
            room_number = self.treeview.item(selected_item)['values'][0]
            self.update_room_condition(room_number, 'Clean')

    def set_room_condition_dirty(self):
        # Get the selected item from the Treeview
        selected_item = self.treeview.focus()
        if selected_item:
            room_number = self.treeview.item(selected_item)['values'][0]
            self.update_room_condition(room_number, 'Dirty')

    def update_room_condition(self, room_number, condition):
        # Establish a connection to the database
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        # Update the condition of the room
        cursor.execute("UPDATE rooms SET condition = ? WHERE room_number = ?", (condition, room_number))
        connection.commit()

        connection.close()

        # Refresh the Treeview
        self.refresh_treeview()

    def refresh_treeview(self):
        # Clear the Treeview
        self.treeview.delete(*self.treeview.get_children())

        # Fetch the updated rows from the database
        rows = self.fetch_rows_from_database()

        # Insert each row into the Treeview
        for row in rows:
            self.treeview.insert('', tk.END, values=row)

    def to_home(self):
        self.root.destroy()
        from Home import Home     ##import here to avoid circular import error
        home_window = Home()
        home_window.root.mainloop()

    def fetch_rows_from_database(self):
        # Establish a connection to the database
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        # Fetch all rows from the rooms table
        cursor.execute("SELECT * FROM rooms")
        rows = cursor.fetchall()

        connection.close()

        return rows
