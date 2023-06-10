import customtkinter
from tkinter import *
from tkinter import Tk, Label
from PIL import ImageTk, Image

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

class Requests:
    def __init__(self):
        self.root = customtkinter.CTk()
        self.root.geometry("1200x900")
        self.frame = customtkinter.CTkFrame(master=self.root)
        self.frame.pack(pady=0, padx=0, fill="both", expand=True)

        

    




    ##button that takes the user back to home window
        self.back_button = customtkinter.CTkButton(master=self.frame, text="Back", command=self.to_home) 
        self.back_button.pack(pady=12, padx=10) 
    


    def to_home(self):
        self.root.destroy()
        from Home import Home     ##import here to avoid circular import error
        home_window = Home()
        home_window.root.mainloop()


    