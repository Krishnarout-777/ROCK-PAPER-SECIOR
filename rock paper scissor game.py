import random

def rock_paper_scissors():
    item_list = ["rock", "paper", "scissors"]

    user_choice = input("Enter rock, paper, scissors: ").lower()

    computer_choice = random.choice(item_list)

    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("Both choice same:It's a tie!")

    elif user_choice== "rock" and computer_choice == "scissors":
        print("You win!")

    elif user_choice == "paper" and computer_choice == "rock":
        print("You win!")

    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win!")

    elif user_choice in item_list:
        print("Computer wins!")

    else:
        print("Invalid choice!")


rock_paper_scissors()