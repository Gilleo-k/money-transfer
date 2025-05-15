""" 
1 - write a python script that will take email from
users and check if the email entered has '@' 
if the email have it, then display "you have entered a valid email" otherwise display
your email is invalid please enter a valid email.
"""

f_name = input("Enter your name: ")
Email = input("Enter your Email: ")
if '@' in Email:
    print(f"{f_name} you have entered a valid email")
else:
    print("invalid please enter a valid email")