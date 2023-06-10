import os
import tkinter as tk
import customtkinter
from PIL import ImageTk, Image
from CheckIn import CheckIn
from CheckOut import CheckOut
from Requests import Requests
from Reservations import Reservations
from Housekeeping import Housekeeping
from PrintCheckIns import PrintCheckIns
from MakeReservation import MakeReservation
from MyAccount import MyAccount


class Home:
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


        button1 = customtkinter.CTkButton(master=self.frame, text="Check In", command=self.go_to_check_in, border_width=0)
        button1.pack(pady=12, padx=10)
        
        button2 = customtkinter.CTkButton(master=self.frame, text="Check Out", command=self.go_to_check_out, border_width=0)
        button2.pack(pady=12, padx=10)

        button3 = customtkinter.CTkButton(master=self.frame, text="Housekeeping", command=self.go_to_housekeeping, border_width=0)
        button3.pack(pady=12, padx=10)

        button4 = customtkinter.CTkButton(master=self.frame, text="Requests", command=self.go_to_requests)
        button4.pack(pady=12, padx=10)

        button5 = customtkinter.CTkButton(master=self.frame, text="Reservations", command=self.go_to_reservations)
        button5.pack(pady=12, padx=10)

        button6 = customtkinter.CTkButton(master=self.frame, text="Active Reservations", command=self.go_to_print_check_ins)
        button6.pack(pady=12, padx=10)

        button7 = customtkinter.CTkButton(master=self.frame, text="Make Reservation", command=self.go_to_Make_Reservation)
        button7.pack(pady=12, padx=10)

        button8 = customtkinter.CTkButton(master=self.frame, text="My Account", command=self.go_to_my_account)
        button8.pack(pady=12, padx=10)

        button9 = customtkinter.CTkButton(master=self.frame, fg_color=("black", "red") ,text="Logout", command= self.Logout)
        button9.pack(pady=12, padx=10)

    def go_to_check_in(self):
        self.root.destroy()
        window = CheckIn()
        window.root.mainloop()

    def go_to_check_out(self):
        window = CheckOut()
        self.root.destroy()
        window.root.mainloop()

    def go_to_housekeeping(self):
        window = Housekeeping()
        self.root.destroy()
        window.root.mainloop()

    def go_to_requests(self):
        window = Requests()
        self.root.destroy()
        window.root.mainloop()

    def go_to_reservations(self):
        window = Reservations()
        self.root.destroy()
        window.root.mainloop()

    def go_to_print_check_ins(self):
        self.root.destroy()
        window = PrintCheckIns()
        window.root.mainloop()

    def go_to_my_account(self):
        self.root.destroy()
        window = MyAccount()
        window.root.mainloop()

    def go_to_Make_Reservation(self):
        window = MakeReservation()
        window.root.mainloop()

    def Logout(self):
        self.root.destroy()
        from login import Login          ##import here to avoid circular import error
        login_window = Login()
       

