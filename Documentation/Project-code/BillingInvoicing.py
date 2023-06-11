import tkinter as tk
import customtkinter
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
from tkcalendar import Calendar
from PIL import ImageTk, Image

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

class BillingInvoicing:
    def __init__(self):
        self.root = customtkinter.CTk()
        self.root.geometry("1500x830")
        self.frame = customtkinter.CTkFrame(master=self.root)
        self.frame.pack(pady=0, padx=0, fill="both", expand=True)
        self.root.title('Billing and Invoicing')

        
    
        # Room Type Configuration
        room_type_label = customtkinter.CTkLabel(self.root, text='Room Type:', font=('Arial', 14))
        room_type_label.pack()

        self.room_type_combo = ttk.Combobox(self.root, values=['Simple Room', 'Deluxe Room', 'VIP Room'], font=('Arial', 14))
        self.room_type_combo.pack()
        self.room_type_combo.current(0)

        amenities_label = customtkinter.CTkLabel(self.root, text='Amenities:', font=('Arial', 14))
        amenities_label.pack()

        self.safebox_var = tk.IntVar()
        safebox_checkbox = ttk.Checkbutton(self.root, text='Safebox', variable=self.safebox_var)
        safebox_checkbox.pack()

        self.air_conditioner_var = tk.IntVar()
        air_conditioner_checkbox = ttk.Checkbutton(self.root, text='Air Conditioner', variable=self.air_conditioner_var)
        air_conditioner_checkbox.pack()

        capacity_label = customtkinter.CTkLabel(self.root, text='Capacity:', font=('Arial', 14))
        capacity_label.pack()

        self.capacity_spinbox = tk.Spinbox(self.root, from_=1, to=8)
        self.capacity_spinbox.pack()
        self.capacity_spinbox.delete(0, tk.END)
        self.capacity_spinbox.insert(0, 1)

        # Seasonal Pricing
        season_label = customtkinter.CTkLabel(self.root, text='Season:')
        season_label.pack()

        self.check_in_cal = Calendar(self.root, selectmode='day')
        self.check_in_cal.pack()

        self.check_out_cal = Calendar(self.root, selectmode='day')
        self.check_out_cal.pack()

        # Rate Display and Calculation
        calculate_price_button = customtkinter.CTkButton(self.root, text='Calculate Price', command=self.calculate_price)
        calculate_price_button.pack()

        self.price_label = customtkinter.CTkLabel(self.root, text='Total Price: ')
        self.price_label.pack()
        
        ##button that takes the user back to home window
        self.back_button = customtkinter.CTkButton(master=self.frame, text="Back", command=self.to_home) 
        self.back_button.pack(pady=12, padx=10) 

    def calculate_price(self):
        # Get selected room type and dates
        room_type = self.room_type_combo.get()
        check_in = self.check_in_cal.get_date()
        check_out = self.check_out_cal.get_date()

        # Calculate length of stay
        length_of_stay = (check_out - check_in).days

        # Calculate base rate based on room type
        if room_type == 'Simple Room':
            base_rate = 100
        elif room_type == 'Deluxe Room':
            base_rate = 150
        elif room_type == 'VIP Room':
            base_rate = 250

        # Calculate total charges
        total_charges = base_rate * length_of_stay

        # Add additional charges for amenities
        if self.safebox_var.get() == 1:
            total_charges += 20
        if self.air_conditioner_var.get() == 1:
            total_charges += 30

        # Calculate VAT (24%)
        total_charges *= 0.24

        # Display total charges and VAT
        self.price_label.configure(text=f'Total Price: {total_charges} USD')
        
    def to_home(self):
     self.root.destroy()
     from Home import Home  # import here to avoid circular import error
     home_window = Home()
     home_window.root.mainloop()