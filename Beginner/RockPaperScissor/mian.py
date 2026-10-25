import random

user_choice = input("Choose 'rock', 'paper', or 'scissor': ").lower()
computer_choice = random.choice(["rock", "paper", "scissor"])

print(f"Computer chose: {computer_choice}")

if user_choice == computer_choice:
    print("It's a draw!")
elif (user_choice == "rock" and computer_choice == "scissor") or \
     (user_choice == "paper" and computer_choice == "rock") or \
     (user_choice == "scissor" and computer_choice == "paper"):
    print("You win! 🎉")
else:
    print("You lose! 😢")