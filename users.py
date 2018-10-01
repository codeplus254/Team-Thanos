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
		self.access_level = input("Enter access-level : ")

		registered_user = {
			'username': self.username,
			'password': self.password,
			'access_level': self.access_level
		}

		self.user_details.append(registered_user)
		print(self.user_details)
		print("Hoorah! You have created an account you can now log in")