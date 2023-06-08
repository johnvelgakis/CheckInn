from login import Login
from DB import DB


# Run main to start the programm 

# To login as admin (hotel employee) use 
#---- username: admin -------
#---- password: password ----

#login
login_system = Login()
login_system.start()

#database
DB_system = DB()