import customtkinter
import sqlite3

from PIL import ImageTk, Image

from Home import Home
from SignUp import SignUp
from DB import DB

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

class Login:
    def __init__(self):
        self.root = customtkinter.CTk()
        self.root.geometry("600x400")
        self.frame = customtkinter.CTkFrame(master=self.root)
        self.frame.pack(
            pady=0, padx=0, fill="both", expand=True)
        self.label = customtkinter.CTkLabel(master=self.frame, text="Login System")
        self.label.pack(pady=12, padx=10)
        self.entry1 = customtkinter.CTkEntry(master=self.frame, placeholder_text="Username")
        self.entry1.pack(pady=12, padx=10)
        self.entry2 = customtkinter.CTkEntry(master=self.frame, placeholder_text="Password", show="*")
        self.entry2.pack(pady=12, padx=10)
        self.login_button = customtkinter.CTkButton(master=self.frame, text="Login", command=self.login)
        self.login_button.pack(pady=12, padx=10)
        self.signup_button = customtkinter.CTkButton(master=self.frame, text="Sign Up", command=self.signup)
        self.signup_button.pack(pady=12, padx=10)
        self.exit = customtkinter.CTkButton(master=self.frame, text="Exit", command=self.exit)
        self.exit.pack(pady=12, padx=10)
##DB

     # Connect to the database
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

    # Close the database connection
        cursor.close()
        conn.close()


    ##Log-In
    def login(self):
        username = self.entry1.get()
        password = self.entry2.get()
        if username == "admin" and password == "password":
            self.root.destroy()
            Home()   ##Opens Home Screen

        else:
            customtkinter.CTkMessageDialog(master=self.root, message="Invalid username or password", icon="error")

    

    #exit (close window)
    def exit(self):
        self.root.destroy()


    def start(self):
        self.root.mainloop()

    def signup(self):
        SignUp()
            

login_system = Login()
login_system.start()

DB_system = DB()
DB_system.start()
