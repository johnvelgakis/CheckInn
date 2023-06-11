import tkinter as tk
import customtkinter
from PIL import ImageTk, Image


class Home:
    def __init__(self):
        self.root = customtkinter.CTk()
        self.root.geometry("1200x900")
        self.frame = tk.Frame(master=self.root)
        self.frame.pack(pady=0, padx=0, fill="both", expand=True)
        self.root.title('Analytics')

        # Set up the background image
        self.background_image = ImageTk.PhotoImage(Image.open("Documentation/Project-code/backround.png"))
        self.background_label = tk.Label(self.root, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        self.frame = tk.Frame(master=self.root)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")


        self.button1 = customtkinter.CTkButton(master=self.frame, text="Occupancy", command=self.occupancy_report, border_width=0)
        self.button1.pack(pady=12, padx=10)
        
        self.button2 = customtkinter.CTkButton(master=self.frame, text="Budget", command=self.budget_report, border_width=0)
        self.button2.pack(pady=12, padx=10)

        self.button3 = customtkinter.CTkButton(master=self.frame, text="Functional Budget", command=self.fun_budget_report, border_width=0)
        self.button3.pack(pady=12, padx=10)

        self.button4 = customtkinter.CTkButton(master=self.frame, text="Guest Preferences", command=self.guest_pref_report, border_width=0)
        self.button4.pack(pady=12, padx=10)

        self.button5 = customtkinter.CTkButton(master=self.frame, text="Top Bookers", command=self.top_bookers_report, border_width=0)
        self.button5.pack(pady=12, padx=10)

        self.button6 = customtkinter.CTkButton(master=self.frame, text="Action Log", command=self.action_log_report, border_width=0)
        self.button6.pack(pady=12, padx=10)

        ##button that takes the user back to home window
        self.back_button = customtkinter.CTkButton(master=self.frame, text="Back", command=self.to_guest_menu, border_width=0) 
        self.back_button.pack(pady=12, padx=10)

    def to_guest_menu(self):
        self.root.destroy()
        from GuestMenu import GuestMenu    
        home_window = GuestMenu()
        home_window.root.mainloop()   

