import customtkinter

from MakeReservation import MakeReservation

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

class GuestMenu:
    def __init__(self):
        self.root = customtkinter.CTk()
        self.root.geometry("1200x900")
        self.frame = customtkinter.CTkFrame(master=self.root)
        self.frame.pack(pady=0, padx=0, fill="both", expand=True)

        self.name_label = customtkinter.CTkLabel(master=self.frame, text="Welcome , Below you can make your reservation!")
        self.name_label.pack(pady=12, padx=10)

        button1 = customtkinter.CTkButton(master=self.frame, text="Make Reservation", command=self.go_to_Make_Reservation)
        button1.pack(pady=12, padx=10)
        
    def go_to_Make_Reservation(self):
        self.root.destroy()
        window = MakeReservation()
        window.root.mainloop()