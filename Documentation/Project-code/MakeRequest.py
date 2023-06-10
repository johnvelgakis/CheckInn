import tkinter as tk
from tkinter import ttk
import sqlite3
from PIL import ImageTk, Image


from PIL import ImageTk, Image

class MakeRequest:
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

        self.room_number_label = tk.Label(master=self.frame, text="Room Number")
        self.room_number_label.pack(pady=12, padx=10)

        self.room_number_entry = tk.Entry(master=self.frame)
        self.room_number_entry.pack(pady=0, padx=10)

        self.request_label = tk.Label(master=self.frame, text="Request")
        self.request_label.pack(pady=12, padx=10)

        self.request_combobox = ttk.Combobox(master=self.frame, values=["Housekeeping", "Alarm", "Airport Transportation", "Food and Beverages"])
        self.request_combobox.pack(pady=0, padx=10)

        self.description_label = tk.Label(master=self.frame, text="Description")
        self.description_label.pack(pady=12, padx=10)

        self.description_entry = tk.Entry(master=self.frame)
        self.description_entry.pack(pady=0, padx=10)

        self.send_request_button = tk.Button(master=self.frame, text="Send Request", command=self.send_request)
        self.send_request_button.pack(pady=12, padx=10)

        self.back_button = tk.Button(master=self.frame, text="Back", command=self.to_guest_menu)
        self.back_button.pack(pady=12, padx=10)

    def send_request(self):
        room_number = self.room_number_entry.get()
        request = self.request_combobox.get()
        description = self.description_entry.get()

        if room_number and request:
            self.save_request(room_number, request, description)
            tk.messagebox.showinfo("Success", "Request sent successfully!")
        else:
            tk.messagebox.showerror("Error", "Please enter a room number, select a request, and provide a description.")

    def save_request(self, room_number, request, description):
        # Establish a connection to the database
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        # Insert the request into the requests table
        cursor.execute("INSERT INTO requests (room_number, request, description) VALUES (?, ?, ?)",
                       (room_number, request, description))
        connection.commit()

        connection.close()

    def to_guest_menu(self):
        self.root.destroy()
        from GuestMenu import GuestMenu     ##import here to avoid circular import error
        home_window = GuestMenu()
        home_window.root.mainloop()
