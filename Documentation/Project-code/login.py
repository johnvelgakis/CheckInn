import os
import tkinter as tk
import customtkinter
from PIL import ImageTk, Image
import sqlite3

from PIL import ImageTk, Image

from Home import Home
from SignUp import SignUp
from DB import DB

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

class Login:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1300x731")
        self.frame = tk.Frame(master=self.root)
        self.frame.pack(pady=0, padx=0, fill="both", expand=True)


        # Set up the background image
        self.background_image = ImageTk.PhotoImage(Image.open("Documentation/Project-code/backround.png"))
        self.background_label = tk.Label(self.root, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        self.frame = tk.Frame(master=self.root)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        self.entry1 = customtkinter.CTkEntry(master=self.frame, placeholder_text="Username")
        self.entry1.pack(pady=4, padx=2)
        self.entry2 = customtkinter.CTkEntry(master=self.frame, placeholder_text="Password", show="*")
        self.entry2.pack(pady=4, padx=2)
        self.login_button = customtkinter.CTkButton(master=self.frame, text="Login", command=self.login)
        self.login_button.pack(pady=4, padx=2)
        self.signup_button = customtkinter.CTkButton(master=self.frame, text="Sign Up", command=self.signup)
        self.signup_button.pack(pady=4, padx=2)
       
      
        
        self.guest_button = customtkinter.CTkButton(master=self.root, text="Guest",fg_color=("black", "green"), command=self.go_to_guest_menu)
        self.guest_button.place(x=580, y=530)

        self.exit_button = customtkinter.CTkButton(master=self.root, text="Exit",fg_color=("black", "red"), command=self.exit)
        self.exit_button.place(x=580, y=600)
       
        
        
        
     


    ##Log-In
    def login(self):
        username = self.entry1.get()
        password = self.entry2.get()
        if username == "admin" and password == "password":
            self.root.destroy()
            Home()   ##Opens Home Screen
        
        else:
            # Incorrect username or password
            customtkinter.CTkMessageBox.showinfo("Login Failed", "Wrong username or password.")




    #exit (close window)
    def exit(self):
        self.root.destroy()


    def start(self):
        self.root.mainloop()

    def signup(self):
        SignUp()
            

    def go_to_guest_menu(self):
        self.root.destroy()
        from GuestMenu import GuestMenu  ##import here to avoid circular import error
        window = GuestMenu()
        window.root.mainloop()
