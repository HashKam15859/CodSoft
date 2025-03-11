checker = '' # Initializing a global variable to check when to exit the loop

# Function to perform the functions of a calculator
def calculator(): 
    global checker
    print("\n\nChoose which operation is to be performed: ")
    print("1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Integer Division \n6. Modular Division (for Remainder)")
    print("7. Press e to Exit....")
    choice = input("Enter an choice: ")
    checker = choice
    if choice in ('1', '2', '3', '4', '5', '6'): 
        a = float(input("Enter first operand: "))
        b = float(input("Enter second operand: "))
        if choice == '1':  # If the user chooses addition
            c = a + b 
            print ("\nResult: \n", a, " + ", b, " = ", c)
        elif choice == '2':  # If the user chooses subtraction
            c = a - b
            print("\nResult: \n", a, " - ", b, " = ", c)
        elif choice == '3':  # If the user chooses multiplication
            c = a * b
            print("\nResult: \n", a, " * ", b, " = ", c)
        elif choice in ('4', '5', '6'):  # If the user chooses any type of division
            if b == 0.0:
                print("Division of any kind can't be performed with 0!")
            else: 
                if choice == '4':   # If the user chooses simple division
                    c = a / b
                    print("\nResult: \n", a, " / ", b, " = ", c)
                elif choice == '5':  # If the user chooses integer division
                    c = a // b
                    print("\nResult: \n", a, " // ", b, " = ", c)
                elif choice == '6':  # If the user chooses to find the remainder after division
                    c = a % b
                    print("\nResult: \n", a, " % ", b, " = ", c)
    elif choice in ('e', 'E'):  # If the user chooses to exit the calculator
        print("\nExiting the Calculator.....")
        checker = 'e'
        exit()                    
    else: 
        print("Invalid choice! Try again~")         

# while loop to keep running the calculator until the user enters 'e' to Exit
while checker != 'e':
    calculator()
                
