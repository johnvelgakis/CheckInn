import tkinter as tk
import customtkinter
import sqlite3
from PIL import ImageTk, Image

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

class Analytics:
    def __init__(self):
        self.root = customtkinter.CTk()
        self.root.geometry("1300x731")
        self.frame = tk.Frame(master=self.root)
        self.frame.pack(pady=0, padx=0, fill="both", expand=True)
        self.root.title('Analytics')

       
        
        self.frame = tk.Frame(master=self.root)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")


        self.button1 = customtkinter.CTkButton(master=self.frame, text="Occupancy", command=self.occupancy_report, border_width=0)
        self.button1.pack(pady=12, padx=10)
        
        self.button2 = customtkinter.CTkButton(master=self.frame, text="Budget", command=self.budget_report, border_width=0)
        self.button2.pack(pady=12, padx=10)

        self.button3 = customtkinter.CTkButton(master=self.frame, text="Functional Budget", command=self.fun_budget_report, border_width=0)
        self.button3.pack(pady=12, padx=10)

        self.button4 = customtkinter.CTkButton(master=self.frame, text="Guest Preferences", command=self.guest_pref_report, border_width=0)
        self.button4.pack(pady=12, padx=10)

        self.button5 = customtkinter.CTkButton(master=self.frame, text="Top Bookers", command=self.top_bookers_report, border_width=0)
        self.button5.pack(pady=12, padx=10)

        self.button6 = customtkinter.CTkButton(master=self.frame, text="Action Log", command=self.action_log_report, border_width=0)
        self.button6.pack(pady=12, padx=10)

        ##button that takes the user back to home window
        self.back_button = customtkinter.CTkButton(master=self.frame, text="Back", command=self.to_home, border_width=0) 
        self.back_button.pack(pady=12, padx=10)
    
     # Placeholder function to go back to the home window
    def to_home(self):
        self.root.destroy()
        from Home import Home  ##import here to avoid circular import error
        home_window = Home()
        home_window.root.mainloop()

    def occupancy_report(self):
        # Placeholder function for the Occupancy report

        # Connect to the database
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        # Fetch the required information from the reservations table
        cursor.execute("SELECT arrival_date, departure_date, num_people FROM reservations")
        results = cursor.fetchall()

        # Prepare the message to display in the pop-up window
        message = "Occupancy Report:\n\n"
        for arrival_date, departure_date, num_people in results:
            message += f"Arrival Date: {arrival_date}\nDeparture Date: {departure_date}\nNumber of People: {num_people}\n\n"

        # Show the message in a pop-up window
        messagebox.showinfo("Occupancy Report", message)

        # Close the database connection
        cursor.close()
        conn.close()

    def budget_report(self):
        # Placeholder function for the Budget report
        return

    def fun_budget_report(self):
        # Placeholder function for the Functional Budget report
        return

    def guest_pref_report(self):
        # Placeholder function for the Guest Preferences report
        return

    def top_bookers_report(self):
        # Placeholder function for the Top Bookers report
        return

    def action_log_report(self):
        # Placeholder function for the Action Log report
        return
