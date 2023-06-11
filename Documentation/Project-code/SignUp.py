import tkinter as tk
import customtkinter
from tkinter import messagebox
from PIL import ImageTk, Image

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

#create class SignUp
class SignUp:
    
    def __init__(self): 
        
        self.root = tk.Toplevel()
        self.root.geometry("1200x900") 
        self.root.title("Sign Up") 
        
        # Set up the background image
        self.background_image = ImageTk.PhotoImage(Image.open("Documentation/Project-code/backround.png"))
        self.background_label = tk.Label(self.root, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
         

#---------------------------------------------------------------------------------------------------------------------
        #Entries & Entry Labels Config
    
        #First Name
        self.first_label = tk.Label(self.root, text="First Name", font=('Arial', 14))
        self.first_var = tk.StringVar()
        self.first_var.set("")
        self.first = tk.Entry(self.root, textvariable=self.first_var)
       
        #Last Name
        self.last_label = tk.Label(self.root, text="Last Name", font=('Arial', 14))
        self.last_var = tk.StringVar()
        self.last_var.set("")
        self.last = tk.Entry(self.root, textvariable=self.last_var)
       
        #email
        self.email_label = tk.Label(self.root, text="Email", font=('Arial', 14))
        self.email_var = tk.StringVar()
        self.email_var.set("")
        self.email = tk.Entry(self.root, textvariable=self.email_var)
       
        #password
        self.password_label = tk.Label(self.root, text="Password", font=('Arial', 14))
        self.password_var = tk.StringVar()
        self.password_var.set("")
        self.password = tk.Entry(self.root, textvariable=self.password_var, show="*")
       
        #confirm password
        self.c_password_label = tk.Label(self.root, text="Confirm Password", font=('Arial', 14))
        self.c_password_var = tk.StringVar()
        self.c_password_var.set("")
        self.c_password = tk.Entry(self.root, textvariable=self.c_password_var, show="*")
        
#---------------------------------------------------------------------------------------------------------------------
        #Layout
        self.first_label.grid(row=0, column=0, sticky="e")
        self.first.grid(row=0, column=1)
        self.last_label.grid(row=1, column=0, sticky="e")
        self.last.grid(row=1, column=1)
        self.email_label.grid(row=2, column=0, sticky="e")
        self.email.grid(row=2, column=1)
        self.password_label.grid(row=3, column=0, sticky="e")
        self.password.grid(row=3, column=1)
        self.c_password_label.grid(row=4, column=0, sticky="e")
        self.c_password.grid(row=4, column=1, sticky="e")
        
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_rowconfigure(4, weight=1)
        self.root.grid_rowconfigure(5, weight=1)
        self.root.grid_rowconfigure(6, weight=1)
        self.root.grid_columnconfigure(0, weight=0)
        self.root.grid_columnconfigure(1, weight=0)
    
#---------------------------------------------------------------------------------------------------------------------    
    
        #define a variable to the event: is check button clicked?        
        self.check_state = tk.IntVar() #this integer value will have the state of the checkbox
        
        #Checkbox
        self.checkbox = tk.Checkbutton(self.root, text="I Accept the Terms of Use & Privacy Policy", font=('Arial', 14), variable=self.check_state)
        self.checkbox.grid(row=5, column=0, sticky="e")
        
        #Sign up button
        self.button = tk.Button(self.root, text="Sign Up", font=('Arial', 14), command=self.sign_up)
        self.button.grid(row=6, column=1, sticky="e")

        ##button that takes the user back to home window
        self.back_button = customtkinter.CTkButton(master=self.frame, text="Back", command=self.to_login_window) 
        self.back_button.pack(pady=12, padx=10)
        
        #horizontal Menu bar with dropdown list elements
        self.menubar = tk.Menu(self.root)
        self.filemenu = tk.Menu(self.menubar, tearoff=0) #this menu is part of the menubar, tearoff parameter:otherwise we will have a dashed line at the top
        self.filemenu.add_command(label="Close", command=self.on_closing) #inside the filemenu there will be an option Close, which will be closing the GUI
        self.filemenu.add_separator() #adds a separator between the two commands on the drop down filemenu
        #to add the filemenu to the menubar we need to use cascade:
        self.menubar.add_cascade(menu=self.filemenu, label="File")
        
        #adding the menubar to the root:
        self.root.config(menu=self.menubar)
        
        #Event handler for closing the window 
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing) 
        
        self.root.mainloop()

#---------------------------------------------------------------------------------------------------------------------
    
    #methods declaration

    def sign_up(self):
        if self.check_state.get() == 1:
            if self.password_var.get() == self.c_password_var.get():
                self.save_login_details()
        

    def save_login_details(self):
        self.first_name = self.first_var.get()
        self.last_name = self.last_var.get()
        self.email_ = self.email_var.get()
        self.password_ = self.password_var.get()
        # Create a document
        data = {"First Name": self.first_name, "Last Name": self.last_name, 
                "email": self.email_, "password": self.password_}
        
        # Insert the document into the collection
        collection.insert_one(data)
        print("Login details saved to MongoDB")
        self.root.destroy()
        
    #when clicking on the close window: ask the user 
    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            print("Goodbye!")
            self.root.destroy() #destroys the current window
    
    def to_login_window(self):
        self.root.destroy()
        from login import login    
        login_window = login()
        login_window.root.mainloop()