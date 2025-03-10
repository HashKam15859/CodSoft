import random  
import string

# Defining a function to generate password based on length and stregnth
def password_generator (length, strength):
    characters = ''
    if strength == 1:
        characters = string.ascii_letters
    elif strength == 2: 
        characters = string.ascii_letters + string.digits + string.punctuation
    else:   # If the user inputs anything besides 1 or 2 for strength, program will exit
        print("Invalid choice for strength! Exiting.....")
        exit()
    password = ''.join(random.choices(characters, k=length)) 
    return password


checker = 0 # Checker variable used to exit from the loop

# Exception Handling to handle any invalid inputs entered by the user
try:
    while checker == 0:
        length = int(input("\nEnter the desired password length: "))
        print("What kind of password would you like? \n1. Weak Password (Consists of only letters) \n2. Strong Password (Consists of letters, digits & special characters)\n")
        strength = int(input("Enter a choice: "))
        if length < 8: 
            if length < 1: 
                print("A password of this length is not possible! Try again~")
                continue
            else: 
                print("A good password has atleast 8 characters. Would you still like to proceed with a short length password? (y/n): ")
                checker2 = input().lower()
                if checker2 == 'n':
                    continue
                else:
                    print("\nGenerated Password: ", password_generator(length, strength))
                    checker = 1
        else:
            print("\nGenerated Password: ", password_generator(length, strength))
            checker = 1
except ValueError:
    print("Invalid input! Exiting from the Password Generator.....")
  
