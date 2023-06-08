import customtkinter
import sqlite3
from datetime import datetime
from tkcalendar import Calendar, DateEntry

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

class MakeReservation:
    def __init__(self):
        self.root = customtkinter.CTk()
        self.root.geometry("1200x900")
        self.frame = customtkinter.CTkFrame(master=self.root)
        self.frame.pack(pady=0, padx=0, fill="both", expand=True)

        self.name_label = customtkinter.CTkLabel(master=self.frame, text="Name")
        self.name_label.pack(pady=12, padx=10)

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

        self.num_people_label = customtkinter.CTkLabel(master=self.frame, text="Number of People")
        self.num_people_label.pack(pady=12, padx=10)

        self.num_people_entry = customtkinter.CTkEntry(master=self.frame, placeholder_text="Enter number of people")
        self.num_people_entry.pack(pady=12, padx=10)

        self.arrival_date_label = customtkinter.CTkLabel(master=self.frame, text="Arrival Date")
        self.arrival_date_label.pack(pady=12, padx=10)

        self.arrival_date_entry = DateEntry(self.frame, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.arrival_date_entry.pack(pady=12, padx=10)

        self.departure_date_label = customtkinter.CTkLabel(master=self.frame, text="Departure Date")
        self.departure_date_label.pack(pady=12, padx=10)

        self.departure_date_entry = DateEntry(self.frame, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.departure_date_entry.pack(pady=12, padx=10)

        self.make_reservation_button = customtkinter.CTkButton(master=self.frame, text="Make Reservation", command=self.save_to_db)
        self.make_reservation_button.pack(pady=12, padx=10) 

        

    def select_dates(self):
        def get_selected_dates():
            selected_arrival_date = calendar.selection_get()
            selected_departure_date = calendar.selection_get() + timedelta(days=1)
            self.arrival_date_entry.set_date(selected_arrival_date)
            self.departure_date_entry.set_date(selected_departure_date)
            top.destroy()

        top = customtkinter.CTkToplevel(self.root)
        top.geometry("400x300")
        calendar = Calendar(top, selectmode="day", date_pattern="dd/mm/yyyy")
        calendar.pack(pady=10)

        confirm_button = customtkinter.CTkButton(master=top, text="Confirm", command=get_selected_dates)
        confirm_button.pack(pady=10)

    def save_to_db(self):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        name = self.name_entry.get()
        surname = self.surname_entry.get()
        age = int(self.age_entry.get())
        num_people = int(self.num_people_entry.get())
        arrival_date = self.arrival_date_entry.get_date().strftime('%d/%m/%Y')
        departure_date = self.departure_date_entry.get_date().strftime('%d/%m/%Y')

        cursor.execute("INSERT INTO reservations (name, surname, age, num_people, arrival_date, departure_date) VALUES (?, ?, ?, ?, ?, ?)",
                       (name, surname, age, num_people, arrival_date, departure_date))

        connection.commit()
        connection.close()

        customtkinter.CTkMessageBox.showinfo("Reservation Successful", "Your reservation has been successfully made.")

   
