"""
3- write a script that will take user's zip code and check if the zip code has 5 digit 
if yes display valid zip code if not display in valid zip code
"""
"""
f_name = input("Enter your name: ")
zip_code = input("Enter your zip code: ")


if len(zip_code) == 5:
    print(f"{f_name} you have entered a valid zip code: {zip_code}")
else:
    print("in valid zip code") """

zip_code = input("Enter your zip code: ")
if not zip_code.isdigit():
    print("Invalid zip code")
elif len(zip_code) != 5:
    print("Invalid zip code")
else:
    print("Valide zip code")    