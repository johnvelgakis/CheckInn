import customtkinter
import tkinter as tk
import sqlite3
from datetime import datetime, timedelta

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

class CheckIn:
    def __init__(self):
        self.root = customtkinter.CTk()
        self.root.geometry("1200x900")
        self.frame = customtkinter.CTkFrame(master=self.root)
        self.frame.pack(pady=0, padx=0, fill="both", expand=True)

        self.name_label = customtkinter.CTkLabel(master=self.frame, text="Name")
        self.name_label.pack( pady=12, padx=10)

        self.name_entry = customtkinter.CTkEntry(master=self.frame, placeholder_text="Enter name")
        self.name_entry.pack(pady=12, padx=10)

        self.surname_label = customtkinter.CTkLabel(master=self.frame, text="Surname")
        self.surname_label.pack(pady=12, padx=10)

        self.surname_entry = customtkinter.CTkEntry(master=self.frame, placeholder_text="Enter surname")
        self.surname_entry.pack(pady=12, padx=10)

        self.age_label = customtkinter.CTkLabel(master=self.frame, text="Age")
        self.age_label.pack(pady=12, padx=10)

        self.age_entry = customtkinter.CTkEntry(master=self.frame, placeholder_text="Enter age")
        self.age_entry.pack(pady=12, padx=10)

        self.room_label = customtkinter.CTkLabel(master=self.frame, text="Room")
        self.room_label.pack(pady=12, padx=10)

        self.room_entry = customtkinter.CTkEntry(master=self.frame, placeholder_text="Enter room number")
        self.room_entry.pack(pady=12, padx=10)

        self.arrival_date_label = customtkinter.CTkLabel(master=self.frame, text="Arrival Date (dd/mm/yyyy)")
        self.arrival_date_label.pack(pady=12, padx=10)

        self.arrival_date_entry = customtkinter.CTkEntry(master=self.frame, placeholder_text="Enter arrival date")
        self.arrival_date_entry.pack(pady=12, padx=10)

        self.departure_date_label = customtkinter.CTkLabel(master=self.frame, text="Departure Date (dd/mm/yyyy)")
        self.departure_date_label.pack(pady=12, padx=10)

        self.departure_date_entry = customtkinter.CTkEntry(master=self.frame, placeholder_text="Enter departure date")
        self.departure_date_entry.pack(pady=12, padx=10)

        self.check_in_button = customtkinter.CTkButton(master=self.frame, text="Check In", command=self.save_to_db)
        self.check_in_button.pack(pady=12, padx=10) 

        ##button that takes the user back to home window
        self.back_button = customtkinter.CTkButton(master=self.frame, text="Back", command=self.to_home) 
        self.back_button.pack(pady=12, padx=10) 

     
    def save_to_db(self):
        ##connect to db
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        # Retrieve the values from the entry widgets (replace `self.name_entry`, `self.surname_entry`, etc., with the respective entry widgets)
        name = self.name_entry.get()
        surname = self.surname_entry.get()
        age = int(self.age_entry.get())  # Assuming age is entered as an integer
        room = self.room_entry.get()
        arrival_date = self.arrival_date_entry.get()  # Assuming the entry widget returns a valid datetime value
        departure_date = self.departure_date_entry.get()  # Assuming the entry widget returns a valid datetime value

        # Insert the values into the database
        cursor.execute("INSERT INTO checkins (name, surname, age, room, arrival_date, departure_date) VALUES (?, ?, ?, ?, ?, ?)",
                    (name, surname, age, room, arrival_date, departure_date))

        connection.commit()
        connection.close()


    def to_home(self):
        self.root.destroy()
        from Home import Home     ##import here to avoid circular import error
        home_window = Home()
        home_window.root.mainloop()
