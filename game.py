import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie"
    elif (
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "rock" and computer_choice == "scissors")
    ):
        return "You Won"
    else:
        return "You Lose"

def main():
    user_score = 0
    computer_score = 0

    while True:
        print("\nLet's play Rock-Paper-Scissors!")
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(["rock", "paper", "scissors"])
        print(f"Computer's choice: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You Won":
            user_score += 1
        elif result == "You Lose":
            computer_score += 1

        print(f"Scores - You: {user_score}, Computer: {computer_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()