import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image


#create class SignUp
class SignUp:
    
    def __init__(self): 
        
        self.root = tk.Toplevel()
        
        self.root.geometry("800x500") 
        self.root.title("Sign Up") 
        
        
        
        # Load the background image
        #background_image = ImageTk.PhotoImage(Image.open("/Users/macbook/Desktop/draft_code/CheckInn_Python/back.png"))

        # Create a Label widget with the background image
        #background_label = tk.Label(self.root, image=background_image)
        #background_label.place(x=0, y=0, relwidth=1, relheight=1)
       

        
        
       # self.label = tk.Label(self.root, text="Sign Up", font=('Arial', 16))
       # self.label.pack(padx=10, pady=10) 

#---------------------------------------------------------------------------------------------------------------------
        #
        #First Name
        self.first_label = tk.Label(self.root, text="First Name", font=('Arial', 14))
        #self.first_label.pack(padx=10, pady=10) 
        self.first_var = tk.StringVar()
        self.first_var.set("")
        self.first = tk.Entry(self.root, textvariable=self.first_var)
       # self.first.pack(padx=10, pady=10)
        #Last Name
        self.last_label = tk.Label(self.root, text="Last Name", font=('Arial', 14))
       # self.last_label.pack(padx=10, pady=10) 
        self.last_var = tk.StringVar()
        self.last_var.set("")
        self.last = tk.Entry(self.root, textvariable=self.last_var)
       # self.last.pack(padx=10, pady=10)
        #email
        self.email_label = tk.Label(self.root, text="Email", font=('Arial', 14))
      #  self.email_label.pack(padx=10, pady=10) 
        self.email_var = tk.StringVar()
        self.email_var.set("")
        self.email = tk.Entry(self.root, textvariable=self.email_var)
       # self.email.pack(padx=10, pady=10)
        #password
        self.password_label = tk.Label(self.root, text="Password", font=('Arial', 14))
       # self.password_label.pack(padx=10, pady=10) 
        self.password_var = tk.StringVar()
        self.password_var.set("")
        self.password = tk.Entry(self.root, textvariable=self.password_var, show="*")
       # self.password.pack(padx=10, pady=10)
        #confirm password
        self.c_password_label = tk.Label(self.root, text="Confirm Password", font=('Arial', 14))
       # self.c_password_label.pack(padx=10, pady=10) 
        self.c_password_var = tk.StringVar()
        self.c_password_var.set("")
        self.c_password = tk.Entry(self.root, textvariable=self.c_password_var, show="*")
        #self.c_password.pack(padx=10, pady=10)
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
    
    
    
    

        #define a variable to the event: is check button clicked?        
        self.check_state = tk.IntVar() #this integer value will have the state of the checkbox
        
        #Checkbox
        self.checkbox = tk.Checkbutton(self.root, text="I Accept the Terms of Use & Privacy Policy", font=('Arial', 14), variable=self.check_state)
        self.checkbox.grid(row=5, column=0, sticky="e")
        
        #Using the command attribute when button is clicked use function show_message
        self.button = tk.Button(self.root, text="Sign Up", font=('Arial', 14), command=self.sign_up())
        self.button.grid(row=6, column=1, sticky="e")
        
        
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
    
    
    def sign_up(self):
        return
    #T&C checked? && password_var ==? c_password_var

  
        
   
    #when clicking on the close window: ask the user 

    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            print("Goodbye!")
            self.root.destroy() #destroys the current window    
    
  
