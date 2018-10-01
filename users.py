from userdata import Userdata

class User:
  """Creates variables for any user"""
  def __init__(self):
    self.username = ""
    self.password = ""
    self.access_level = 0
    self.user_details = Userdata().user_data()
    self.logged_in_details = Userdata().user_login_data()



  def create_account(self):
    print("Register to create an account")
    self.username = input("Enter a username: ")
    self.password = input("Enter a password: ")
    self.access_level = input("Enter a Access level: ")
    varx = self.user_details
    user = [user for user in varx if user['username'] == self.username]
    if len(user) != 0:
      print("Error, user already exists")
    else:
      registered_user = {
        'username': self.username,
        'password': self.password,
        'access_level': self.access_level

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
    else:
      print("Wrong username/password combination")

  def user_logout(self):
    print("Do you want to log out?")
    # print("Enter y/n")
    choice = input("Enter y/n: ")
    if choice == "y":
      varx = self.logged_in_details
      user = [user for user in varx if user['username'] == self.username]
      login_details = {
      "username":self.username,
      "logged_in": False,
      "Timestamp":"Coming soon"
      }
      self.logged_in_details.append(login_details)
      print("Logged out!")
    else:
      print("Aborted")