from login import Login
from DB import DB


# Run main to start the programm 

# To login as admin (hotel employee) use 
#---- username: admin -------
#---- password: password ----


login_system = Login()
login_system.start()

DB_system = DB()