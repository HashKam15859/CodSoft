import random
import time

# Function to generate a random choice for computer
def computer():
    return random.choice([1, 2, 3])

# Global variables to keep track of user & comupter scores
user_score = 0  
comp_score = 0
rounds = 0

# Function to determine who is the winner based on the user and computer chioces
def get_winner(user):
    global user_score, comp_score, rounds 
    comp = computer()
    if user == comp:
        if user == 1: 
            print("Computer: Rock, You: Rock \nIt's a Tie!")
        elif user == 2:
            print("Computer: Paper, You: Paper \nIt's a Tie!")
        else:
            print("Computer: Scissors, You: Scissors \nIt's a Tie!")
    elif user == 1:
        if comp == 2:
            print("Computer: Paper, You: Rock \nComputer wins!")
            comp_score += 1
        elif comp == 3:
            print("Computer: Scisscors, You: Rock \nYou win!")
            user_score += 1
    elif user == 2:
        if comp == 1:
            print("Computer: Rock, You: Paper \nYou win!")
            user_score += 1
        elif comp == 3: 
            print("Computer: Scissors, You: Paper \nYou win!")
            user_score += 1
    elif user == 3:
        if comp == 1:
            print("Computer: Rock, You: Scissors \nComputer wins!")
            comp_score += 1
        elif comp == 2:
            print("Computer: Paper, You: Scissors \nYou win!")
            user_score += 1
    else:
        print("Invalid choice! Choose a number between 1-3.....")

# Function to start the game and help the user navigate through the game
def play_game():
    global user_score, comp_score, rounds
    print("Welcome to the game of Rock-Paper-Scissors, Player!") 
    while True:
        print("\n-------------------------------------------")
        print("How would you like to proceed?")
        print("1. Read the Rules \n2. Play the Game \n3. View Scores \n4. Quit the Game")
        choice = int(input("Enter a choice: ")) 
        if choice not in [1, 2, 3, 4]:
            print("Invalid Choice! Try again by choosing a value from 1-4")
            continue
        elif choice == 1:
            get_rules()
        elif choice == 2:
            while True:
                print("Welcome, Player! Choose your weapon to start the match: ")
                print("1 - Rock, 2 - Paper, 3 - Scissors")
                user = int(input("Your choice: ")) 
                get_winner(user)
                rounds += 1
                print("Continue playing? (y/n)")
                user2 = input().lower()
                if user2 == 'y':
                    continue
                else:
                    print("Going back to the main menu....\n")
                    time.sleep(2)
                    print("------------------------------------------")
                    break
        elif choice == 3:
            print("Number of rounds played: ", rounds)
            print("Your Current Score: ", user_score)
            print("Computer Current Score: ", comp_score)
            if user_score == comp_score:
                print("You are tied with the Computer.")
            elif user_score < comp_score:
                print("The Computer is winning! :(")
            else:
                print("You are winning! Yaayyy~ :)")
        elif choice == 4:
            print("Farewell, Player! We are now exiting the game......^^") 
            exit()
        print("Please wait a moment......")
        time.sleep(3) # Gives the user a 3 second break before moving on to the next iteration

    
# Function to print 
def get_rules():
    print("===========================================================")
    print("Rules for Rock-Paper-Scissors Game: ")
    print("1. Rock breaks Scissors. \n2. Paper captures Rock. \n3. Scissors cuts Paper.\n")
    print("How to play: ")
    print("1. Enter a value to choose your weapon (1-Rock, 2-Paper, 3-Scissors) \n2. You will be playing against the computer. \n3. Best of out of 3 wins the round!")
    print("===========================================================")
                                     
try:
    play_game()
except ValueError or KeyboardInterrupt:
    print("\nYou either entered an invalid value or tried to stop the program! Goodbye~")
    
