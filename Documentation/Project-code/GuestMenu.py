import os
import tkinter as tk
import customtkinter
from PIL import ImageTk, Image

from MakeReservation import MakeReservation

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

class GuestMenu:
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



        button1 = customtkinter.CTkButton(master=self.frame, text="Make Reservation", command=self.go_to_Make_Reservation)
        button1.pack(pady=12, padx=10)
        
        button2 = customtkinter.CTkButton(master=self.frame, fg_color=("black", "red") ,text="Logout", command= self.Logout)
        button2.pack(pady=12, padx=10)


    def go_to_Make_Reservation(self):
        self.root.destroy()
        window = MakeReservation()
        window.root.mainloop()

    def Logout(self):
        self.root.destroy()
        from login import Login          ##import here to avoid circular import error
        login_window = Login()