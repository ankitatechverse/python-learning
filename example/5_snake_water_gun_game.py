# Snake Water Gun
"""
Snake, Water and Gun is a variation of the children's game "rock-paper-scissors" where players use hand gestures to represent a snake, water, or a gun. The gun beats the snake, the water beats the gun, and the snake beats the water.
Write a python program to create a Snake Water Gun game in Python using if-else statements. Do not create any fancy GUI. Use proper functions to check for win.

Game: Snake-Water-Gun (like Rock-Paper-Scissors).

Rules:
Gun beats Snake
Water beats Gun
Snake beats Water

Features:
Keep playing until the user types stop.
Can restart by typing start.
Use functions for clean code.
Add a matrix (dictionary) to simplify win-checking instead of a big if-else chain.
"""

# import random

# def get_computer_choice():
#     choices = ['snake', 'water', 'gun']
#     return random.choice(choices) 

# def get_user_choice():
#     user_input = input("Enter your choice (snake/water/gun): ").lower()
#     while user_input not in ['snake', 'water', 'gun']:
#         print("Invalid choice. Please try again.")
#         user_input = input("Enter your choice (snake/water/gun): ").lower()
#     return user_input

# def determine_winner(user_choice, computer_choice):
#     if user_choice == computer_choice:
#         return "It's a tie!"
#     elif (user_choice == 'snake' and computer_choice == 'gun') or \
#          (user_choice == 'water' and computer_choice == 'snake') or \
#          (user_choice == 'gun' and computer_choice == 'water'):
#         return "You win!"
#     else:
#         return "Computer wins!"
    
# def play_game():
#     print("Welcome to the Snake Water Gun Game!")
#     user_choice = get_user_choice()
#     computer_choice = get_computer_choice()
    
#     print(f"You chose: {user_choice}")
#     print(f"Computer chose: {computer_choice}")
    
#     result = determine_winner(user_choice, computer_choice)
#     print(result)

# if __name__ == "__main__":
#     play_game()




import random

# Choices mapping
choices = {0: "snake", 1: "water", 2: "gun"}

# Matrix for results: 0 = draw, 1 = win, -1 = lose
# Rows = player, Columns = computer
# Order: snake(0), water(1), gun(2)
win_matrix = [
    [0, 1, -1],  # player snake vs (snake, water, gun)
    [1, 0, -1],  # player water vs (snake, water, gun)
    [-1, 1, 0]   # player gun vs (snake, water, gun)
]

def get_computer_choice():
    return random.randint(0, 2)

def check_winner(player, computer):
    result = win_matrix[player][computer]
    if result == 1:
        return "You Win!"
    elif result == -1:
        return "You Lose!"
    else:
        return "It's a Draw/Tie!"

def play_game():
    while True:
        player_input = input("Enter 0 for Snake, 1 for Water, 2 for Gun (or 'stop' to quit): ").lower()
        if player_input == "stop":
            print("Game stopped. Type 'start' to play again.")
            break
        if not player_input.isdigit() or int(player_input) not in [0, 1, 2]:
            print("Invalid choice! Please choose 0, 1, or 2.")
            continue

        player_choice = int(player_input)
        computer_choice = get_computer_choice()
        print(f"You chose: {choices[player_choice]}, Computer chose: {choices[computer_choice]}")
        print(check_winner(player_choice, computer_choice))

def main():
    print("Welcome to Snake-Water-Gun Game!")
    while True:
        command = input("Type 'start' to play or 'stop' to quit: ").lower()
        if command == "start":
            play_game()
        elif command == "stop":
            print("Goodbye!")
            break
        else:
            print("Invalid command. Please type 'start' or 'stop'.")

main()
