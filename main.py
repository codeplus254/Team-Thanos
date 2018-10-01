from users import User

def main():
    user = User()
    
    user.create_account()
    user.user_login()
    user.user_logout()

if __name__ == '__main__':
    main()

