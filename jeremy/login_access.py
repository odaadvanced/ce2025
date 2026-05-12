user = 'admin'
password = '1234'

while True:
    userinput = input("Enter your username ")
    passwordinput = input("Enter your password ")
    
    if userinput == user and passwordinput == password:
        print("Access granted.")
    else:
        print("username or password is incorrect.")