import random

# Function to get the computer's choice
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

# Main function to run the game
def main():
    user_score = 0
    computer_score = 0
    print("Welcome to Rock-Paper-Scissors Game!")
    
    while True:
        # Prompt user for input
        print("\nChoose one: rock, paper, or scissors")
        user_choice = input("Your choice: ").lower()

        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue
        
        # Get the computer's choice
        computer_choice = get_computer_choice()

        # Determine the winner
        winner = determine_winner(user_choice, computer_choice)

        # Display the choices
        print(f"\nYou chose: {user_choice}")
        print(f"The computer chose: {computer_choice}")

        # Display the result
        if winner == "tie":
            print("It's a tie!")
        elif winner == "user":
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1
        
        # Display the scores
        print(f"\nScore -> You: {user_score} | Computer: {computer_score}")
        
        # Ask if the user wants to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

# Run the game
if __name__ == "__main__":
    main()
