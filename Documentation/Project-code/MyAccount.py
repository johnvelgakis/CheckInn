import tkinter as tk
import customtkinter
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from PIL import ImageTk, Image
from tkinter import messagebox

class MyAccount:
    def __init__(self):
        
       
        # Create the GUI window
        self.root = tk.Toplevel()
        self.root.title("My Account")
        self.root.geometry("800x500") 
        

        # Create Label fields
        self.title_label = tk.Label(self.root, text="My Account", font=('Arial', 18))
        self.first_label = tk.Label(self.root, text="First Name", font=('Arial', 14))
        self.last_label = tk.Label(self.root, text="Last Name", font=('Arial', 14))
        self.email_label = tk.Label(self.root, text="Email", font=('Arial', 14))
        
        # Create Entry fields
        self.first_var = tk.StringVar()
        self.last_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.first_entry = tk.Entry(self.root, textvariable=self.first_var)
        self.last_entry = tk.Entry(self.root, textvariable=self.last_var)
        self.email_entry = tk.Entry(self.root, textvariable=self.email_var)
        
        # Create Buttons
        self.save_button = tk.Button(self.root, text="Save", font=('Arial', 14))
        self.change_password_button = tk.Button(self.root, text="Change Password")

        
#---------------------------------------------------------------------------------------------------------------------        
      
#---------------------------------------------------------------------------------------------------------------------        
        # Layout - widgets
        self.title_label.grid(row=0, column=1)
        self.first_label.grid(row=1, column=0, sticky="e")
        self.first_entry.grid(row=1, column=1)
        self.last_label.grid(row=2, column=0, sticky="e")
        self.last_entry.grid(row=2, column=1)
        self.email_label.grid(row=3, column=0, sticky="e")
        self.email_entry.grid(row=3, column=1)
        self.save_button.grid(row=4, column=1, pady=10)
        self.change_password_button.grid(row=5, column=1)
        # Layout - row config [grid]
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_rowconfigure(3, weight=1)
        # Layout - column config [grid]
        self.root.grid_columnconfigure(0, weight=0)
        self.root.grid_columnconfigure(1, weight=0)
        
        
    
    def to_home(self):
        self.root.destroy()
        from Home import Home  # import here to avoid circular import error
        home_window = Home()
        home_window.root.mainloop()

#---------------------------------------------------------------------------------------------------------------------        
