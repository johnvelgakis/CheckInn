from login import Login
from DB import DB


# Run main to start the programm 

# To login as admin (hotel employee) use 
#---- username: admin -------
#---- password: password ----

#To login as guest (hotel client) press the green Guest button


#login
login_system = Login()
login_system.start()

#database
DB_system = DB()