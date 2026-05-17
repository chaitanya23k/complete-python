#password checker will check length of your password
#after printing your password will be hide

user = input("Enter your username! ")
password = input("Enter your password? ")
password = "*" * len(password)
length = len(password)
print(f"Hey {user} your {password} length is {length}")