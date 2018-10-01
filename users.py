from userdata import Userdata

class User:
  """Creates variables for any user"""
  def __init__(self):
    self.username = ""
    self.password = ""
    self.access_level = 0
    self.user_details = Userdata().user_data()



  def create_account(self):
    print("Register to create an account")
    self.username = input("Enter a username: ")
    self.password = input("Enter a password: ")

    registered_user = {
    	'username': self.username,
    	'password': self.password
    }

    self.user_details.append(registered_user)
    print(self.user_details)
    return "Hoorah! You have created an account you can now log in"

  def user_login(self):
    print("Please provide your username and password to log in")
    self.username = input("Enter a username: ")
    self.password = input("Enter a password: ")
    user_data = Userdata().user_data()
    varx = self.user_details
    user = [user for user in varx if user['username'] == self.username]
    if user[0]['password'] == self.password:
      print("Logged in!")
      login_details = {
      "logged_in": True,
      "access_level": 0,
      "Timestamp":"Coming soon"
      }
      Userdata().user_login_data().append(login_details)

