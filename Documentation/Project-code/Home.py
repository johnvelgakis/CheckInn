import os
import customtkinter
from PIL import ImageTk, Image
from CheckIn import CheckIn
from CheckOut import CheckOut
from Requests import Requests
from Reservations import Reservations
from Housekeeping import Housekeeping
from PrintCheckIns import  PrintCheckIns

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

class Home:
    def __init__(self):
        self.root = customtkinter.CTk()
        self.root.geometry("1200x900")
        self.frame = customtkinter.CTkFrame(master=self.root)
        self.frame.pack(pady=0, padx=0, fill="both", expand=True)

        button1 = customtkinter.CTkButton(master=self.frame, text="Check In", command=self.go_to_check_in)
        button1.pack(pady=12, padx=10)
        
        button2 = customtkinter.CTkButton(master=self.frame, text="Check Out", command=self.go_to_check_out)
        button2.pack(pady=12, padx=10)

        button3 = customtkinter.CTkButton(master=self.frame, text="Housekeeping", command=self.go_to_housekeeping)
        button3.pack(pady=12, padx=10)

        button4 = customtkinter.CTkButton(master=self.frame, text="Requests", command=self.go_to_requests)
        button4.pack(pady=12, padx=10)

        button5 = customtkinter.CTkButton(master=self.frame, text="Reservations", command=self.go_to_reservations)
        button5.pack(pady=12, padx=10)

        button6 = customtkinter.CTkButton(master=self.frame, text="Active Reservations", command=self.go_to_print_check_ins)
        button6.pack(pady=12, padx=10)

        button7 = customtkinter.CTkButton(master=self.frame, text="Logout", command= self.Logout)
        button7.pack(pady=12, padx=10)


    def go_to_check_in(self):
        self.root.destroy()
        check_in_window = CheckIn()
        check_in_window.root.mainloop()

    def go_to_check_out(self):
        check_in_window = CheckOut()
        self.root.destroy()
        check_in_window.root.mainloop()

    def go_to_housekeeping(self):
        check_in_window = Housekeeping()
        self.root.destroy()
        check_in_window.root.mainloop()

    def go_to_requests(self):
        check_in_window = Requests()
        self.root.destroy()
        check_in_window.root.mainloop()

    def go_to_reservations(self):
        check_in_window = Reservations()
        self.root.destroy()
        check_in_window.root.mainloop()

    def go_to_print_check_ins(self):
        self.root.destroy()
        check_in_window = PrintCheckIns()
        check_in_window.root.mainloop()

    def Logout(self):
        self.root.destroy()
        from login import Login          ##import here to avoid circular import error
        login_window = Login()
        login_window.root.mainloop()
        


    def start(self):
        self.root.mainloop()

