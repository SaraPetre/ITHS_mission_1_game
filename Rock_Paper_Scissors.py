import random
import os
 

def get_user_choice():
    os.system('clear')
    print("=========================================")
    print("Let´s play the Rock, Paper, Scissors Game\nIt starts by you choising the rock, paper or scissors.\nPlease make your choice!")
    print("=========================================")
    print("Rock")
    print("Paper")
    print("Scissors")
    choice = input(str("\nEnter your choice (Rock/Paper/Scissors): "))
    # if choice == "1":
    #     print ("You chose Rock!")
    # if choice == "2":
    #     print ("You chose Paper!")
    # if choice == "3":
    #     print ("You chose Scissors!")
    return choice

def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        #print(f"Both players selected {user_choice}. It's a tie!")
        return (f"Both players selected {user_choice}. It's a tie!")
    
    # elif 
    #     (user_choice == "Rock" and computer_choice == "Scissors") or
    #     (user_choice == "Paper" and computer_choice == "Rock") or
    #     (user_choice == "Scissors" and computer_choice == "Paper")
    
    elif(
        (user_choice == "Scissors" and computer_choice == "Paper")  

    ):
        return f"Scissors cuts paper! You win!"
        #return "You win!"
    else:
        return "Computer wins!"
    

def main():
    while True:
        user_choice = get_user_choice()
        if user_choice not in ["Rock", "Paper", "Scissors"]:
            print("\n\n!!!!!!!!Invalid choice. Please enter Rock, Paper, or Scissors!!!!!!!\n")
            continue

        computer_choice = get_computer_choice()

        print(f"You chose {user_choice}!")
        print(f"Computer chose {computer_choice}!")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        play_again = input("Play again? (y/n): ").lower()
        if play_again != "y":
            break
#Clearing the Screen
os.system('clear')

if __name__ == "__main__":
    main()



# import random

# while True:
#     user_action = input("Enter a choice (rock, paper, scissors): ")
#     possible_actions = ["rock", "paper", "scissors"]
#     computer_action = random.choice(possible_actions)
#     print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

#     if user_action == computer_action:
#         print(f"Both players selected {user_action}. It's a tie!")
#     elif user_action == "rock":
#         if computer_action == "scissors":
#             print("Rock smashes scissors! You win!")
#         else:
#             print("Paper covers rock! You lose.")
#     elif user_action == "paper":
#         if computer_action == "rock":
#             print("Paper covers rock! You win!")
#         else:
#             print("Scissors cuts paper! You lose.")
#     elif user_action == "scissors":
#         if computer_action == "paper":
#             print("Scissors cuts paper! You win!")
#         else:
#             print("Rock smashes scissors! You lose.")

#     play_again = input("Play again? (y/n): ")
#     if play_again.lower() != "y":
#         break


