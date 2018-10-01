Class User:
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

		from .userdata import user_data
		user_details = user_data()
		user_details.append(registered_user)
		print("Hoorah! You have created an account you can now log in")