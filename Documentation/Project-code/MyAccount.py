import tkinter as tk
import customtkinter
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from PIL import ImageTk, Image
from tkinter import messagebox

#---------------------------------------------------------------------------------------------------------------------        
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

class MyAccount:
    def __init__(self, email):
        
        # instantiating email in order to be accessible from the other methods
        self.email = email
        
        # Connect to MongoDB
        uri = "mongodb+srv://user:user@cluster0.aoyv6kc.mongodb.net/?retryWrites=true&w=majority"
        # Create a new client and connect to the server
        client = MongoClient(uri, server_api=ServerApi('1'))
        db = client["test"]
        collection_name = "test"
        self.collection = db[collection_name]
        
        # Send a ping to confirm a successful connection
        try:
            client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)
        
        # Find the user's document
        self.user_data = self.collection.find_one({"email": self.email})
        print(self.user_data)  

#---------------------------------------------------------------------------------------------------------------------
        # Create the GUI window
        self.root = tk.Toplevel()
        self.root.title("My Account")
        self.root.geometry("1200x900") 
        
#---------------------------------------------------------------------------------------------------------------------        
        # Set up the background image
        self.background_image = ImageTk.PhotoImage(Image.open("Documentation/Project-code/backround.png"))
        self.background_label = customtkinter.CTkLabel(self.root, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
#---------------------------------------------------------------------------------------------------------------------                
        # tkinter Widgets
        # Create Label fields
        self.title_label = tk.Label(self.root, text="My Account", font=('Arial', 18))
        self.first_label = tk.Label(self.root, text="First Name", font=('Arial', 14))
        self.last_label = tk.Label(self.root, text="Last Name", font=('Arial', 14))
        self.email_label = tk.Label(self.root, text="Email", font=('Arial', 14))
        
        # Create Entry fields
        self.first_var = tk.StringVar()
        self.last_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.first_entry = tk.Entry(self.root, textvariable=self.first_var)
        self.last_entry = tk.Entry(self.root, textvariable=self.last_var)
        self.email_entry = tk.Entry(self.root, textvariable=self.email_var)
        
        # Create Buttons
        self.save_button = tk.Button(self.root, text="Save", font=('Arial', 14), command=self.save_changes)
        self.change_password_button = tk.Button(self.root, text="Change Password", command=self.change_password)

        ##button that takes the user back to home window
        self.back_button = customtkinter.CTkButton(master=self.frame, text="Back", command=self.to_guest_menu) 

#---------------------------------------------------------------------------------------------------------------------        
        # Populate the fields with user data
        self.first_entry.insert(0, self.user_data["First Name"])
        self.last_entry.insert(0, self.user_data["Last Name"])
        self.email_entry.insert(0, self.user_data["email"])
#---------------------------------------------------------------------------------------------------------------------        
        # Layout - widgets
        self.title_label.grid(row=0, column=1)
        self.first_label.grid(row=1, column=0, sticky="e")
        self.first_entry.grid(row=1, column=1)
        self.last_label.grid(row=2, column=0, sticky="e")
        self.last_entry.grid(row=2, column=1)
        self.email_label.grid(row=3, column=0, sticky="e")
        self.email_entry.grid(row=3, column=1)
        self.save_button.grid(row=4, column=1, pady=10)
        self.change_password_button.grid(row=5, column=1)
        self.back_button.grid(row=6, column=1)
        # Layout - row config [grid]
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_rowconfigure(4, weight=1)
        self.root.grid_rowconfigure(5, weight=1)
        self.root.grid_rowconfigure(6, weight=1)
        # Layout - column config [grid]
        self.root.grid_columnconfigure(0, weight=0)
        self.root.grid_columnconfigure(1, weight=0)
        
        # Run the GUI main loop
        self.root.mainloop()
    
#--------------------------------------------------------------------------------------------------------------------- 
    # methods declaration
    def save_changes(self):
        # Retrieve the new values from the entry fields
        new_first_name = self.first_var.get()
        new_last_name = self.last_var.get()
        new_email = self.email_entry.get()  # Retrieve the value from email_entry
        
        # Update the user's document in the MongoDB collection
        self.collection.update_one(
            {"email": self.email},
            {"$set": {"First Name": new_first_name, "Last Name": new_last_name, "email": new_email}}
        )

        # Update the email instance variable with the new email
        self.email = new_email

        # Show a message box with a success message
        messagebox.showinfo("Success", "Changes saved successfully!")

    
        
    def change_password(self):
        # Create a pop-up window for changing the password
        password_window = tk.Toplevel()
        password_window.title("Change Password")

        # Create Labels and Entry fields for current password, new password, and confirm password
        current_password_label = tk.Label(password_window, text="Current Password:")
        new_password_label = tk.Label(password_window, text="New Password:")
        confirm_password_label = tk.Label(password_window, text="Confirm New Password:")

        current_password_entry = tk.Entry(password_window, show="*")
        new_password_entry = tk.Entry(password_window, show="*")
        confirm_password_entry = tk.Entry(password_window, show="*")

        current_password_label.grid(row=0, column=0, sticky="e")
        new_password_label.grid(row=1, column=0, sticky="e")
        confirm_password_label.grid(row=2, column=0, sticky="e")

        current_password_entry.grid(row=0, column=1)
        new_password_entry.grid(row=1, column=1)
        confirm_password_entry.grid(row=2, column=1)
        
        def submit_password_change():
            current_password = current_password_entry.get()
            new_password = new_password_entry.get()
            confirm_password = confirm_password_entry.get()

            # Check if the current password matches the one in the database
            if current_password == self.user_data["password"]:
                # Check if the new passwords match
                if new_password == confirm_password:
                    # Update the password in the database
                    self.collection.update_one(
                        {"email": self.email},
                        {"$set": {"password": new_password}}
                    )
                    # Update the password in the user_data dictionary
                    self.user_data["password"] = new_password
                    messagebox.showinfo("Success", "Password changed successfully!")
                    password_window.destroy()
                else:
                    messagebox.showerror("Error", "New passwords do not match!")
            else:
                messagebox.showerror("Error", "Current password is incorrect!")

        # Create a button to submit the password change
        submit_button = tk.Button(password_window, text="Submit", command=submit_password_change)
        submit_button.grid(row=3, column=1, pady=10)
    
    def to_home(self):
        self.root.destroy()
        from Home import Home  # import here to avoid circular import error
        home_window = Home()
        home_window.root.mainloop()
#---------------------------------------------------------------------------------------------------------------------        
