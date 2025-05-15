"""
2- write a script that will ask user for username and password,
if username is not admin and password admin, then display wrong credentials
please try again.
"""

f_name = input("Enter your name: ")
username = input("Enter your username: ")
password = input("Enter your password: ")

if username and password != 'admin':
    print(f"{f_name} you have entered a wrong credentials please try again")
else:
    print("valid credentials good Job")