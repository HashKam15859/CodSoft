import random  
import string

# Defining a function to generate password based on length and stregnth
def password_generator (length, strength):
    characters = ''
    if strength == 1:
        characters = string.ascii_letters
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length)) 
    return password


checker = 0 # Checker variable used to exit from the loop

# Exception Handling to handle any invalid inputs entered by the user
try:
    while checker == 0:
        length = int(input("Enter the desired password length: "))
        if length < 8: 
            if length < 1: 
                print("A password of this length is not possible! Try again~")
                continue
            else: 
                print("What kind of password would you like? \n1. Weak Password (Consists of only letters) \n2. Strong Password (Consists of letters, digits & special characters)\n")
                strength = int(input("Enter a choice: "))
                print("A good password has atleast 8 characters. Would you still like to proceed with a short length password? (y/n): ")
                checker2 = input().lower()
                if checker2 == 'n':
                    continue
                else:
                    print("Generated Password: ", password_generator(length, strength))
                    checker = 1
        else:
            print("Generated Password: ", password_generator(length, strength))
            checker = 1
except ValueError:  # Program will stop if an invalid input is entered
    print("Invalid input! Exiting from the Password Generator.....")
  
