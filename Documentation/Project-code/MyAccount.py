import tkinter as tk
import customtkinter

from PIL import ImageTk, Image
from tkinter import messagebox


class MyAccount:
    def __init__(self):
        self.root = customtkinter.CTk()
        self.root.geometry("1200x900")
        self.frame = customtkinter.CTkFrame(master=self.root)
        self.frame.pack(pady=0, padx=0, fill="both", expand=True)
    
        self.username_label = customtkinter.CTkLabel(master=self.frame, text="Username")
        self.username_label.pack(pady=12, padx=10)

        self.username_entry = customtkinter.CTkEntry(master=self.frame, placeholder_text="Enter username")
        self.username_entry.pack(pady=12, padx=10)

        self.password_label = customtkinter.CTkLabel(master=self.frame, text="Password")
        self.password_label.pack(pady=12, padx=10)

        self.password_entry = customtkinter.CTkEntry(master=self.frame, placeholder_text="Enter password", show="*")
        self.password_entry.pack(pady=12, padx=10)

        self.new_password_label = customtkinter.CTkLabel(master=self.frame, text="New Password")
        self.new_password_label.pack(pady=12, padx=10)

        self.new_password_entry = customtkinter.CTkEntry(master=self.frame, placeholder_text="Enter new password", show="*")
        self.new_password_entry.pack(pady=12, padx=10)

        self.confirm_password_label = customtkinter.CTkLabel(master=self.frame, text="Confirm New Password")
        self.confirm_password_label.pack(pady=12, padx=10)

        self.confirm_password_entry = customtkinter.CTkEntry(master=self.frame, placeholder_text="Confirm new password", show="*")
        self.confirm_password_entry.pack(pady=12, padx=10)

        self.check_in_button = customtkinter.CTkButton(master=self.frame, text="Connfirm", command=self.save_to_db)
        self.check_in_button.pack(pady=12, padx=10) 

        ##button that takes the user back to home window
        self.back_button = customtkinter.CTkButton(master=self.frame, text="Back", command=self.to_home) 
        self.back_button.pack(pady=12, padx=10) 
    

    def save_to_db(self):
      

        # Retrieve the values from the entry widgets
        username = self.username_entry.get()
        password = self.password_entry.get()
        new_password = self.new_password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        # Perform additional validation or checks as needed
        if new_password != confirm_password:
            # Passwords do not match, show an error message or handle accordingly
            print("Error: New password and confirm password do not match.")
            return

        
    
    def to_home(self):
        self.root.destroy()
        from Home import Home  # import here to avoid circular import error
        home_window = Home()
        home_window.root.mainloop()
     
