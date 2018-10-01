from userdata import Userdata
class User:
  """Creates variables for any user"""

  def __init__(self):
    self.username = ""
    self.password = ""
    self.access_level = 0


  def create_account(self):
    print("Register to create an account")
    self.username = input("Enter a username: ")
    self.password = input("Enter a password: ")

    registered_user = {
    	'username': self.username,
    	'password': self.password
    }

    user_details = Userdata().user_data()
    user_details.append(registered_user)
    print(user_details)
    return "Hoorah! You have created an account you can now log in"

  def user_login(self):
    self.username = input("Enter a username: ")
    self.password = input("Enter a password: ")
    user_data = Userdata().user_data()

    user = [user for user in user_data if user_data['username']==self.username]
    if user[0]['password'] == self.password:
      print("Logged in!")
      login_details = {
      "logged_in": True,
      "access_level": 0,
      "Timestamp":"Coming soon"
      }
      Userdata().user_login_data().append(login_details)