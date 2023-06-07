import customtkinter
from CheckIn import CheckIn
from CheckOut import CheckOut
from Requests import Requests


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

        button3 = customtkinter.CTkButton(master=self.frame, text="Housekeeping")
        button3.pack(pady=12, padx=10)

        button4 = customtkinter.CTkButton(master=self.frame, text="Requests", command=self.go_to_requests)
        button4.pack(pady=12, padx=10)

        button5 = customtkinter.CTkButton(master=self.frame, text="Logout", command= self.Logout)
        button5.pack(pady=12, padx=10)


    def go_to_check_in(self):
        self.root.destroy()
        check_in_window = CheckIn()
        check_in_window.root.mainloop()

    def go_to_check_out(self):
        check_in_window = CheckOut()
        self.root.destroy()
        check_in_window.root.mainloop()

    def go_to_requests(self):
        check_in_window = Requests()
        self.root.destroy()
        check_in_window.root.mainloop()

    def Logout(self):
        self.root.destroy()
        from login import Login          ##import here to avoid circular import error
        login_window = Login()
        login_window.root.mainloop()
        


    def start(self):
        self.root.mainloop()

