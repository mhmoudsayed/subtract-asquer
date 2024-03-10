def is_square_number(num):
    # Function to check if a number is a perfect square
    if num <= 0:
        return False
    root = num ** 0.5
    return root.is_integer()

print("Welcome to subtract a square game")

while True:
    # Prompt the user to enter the initial number of coins to start the game
    n_coins = int(input("Enter the number of coins to start with: "))
    if n_coins > 1:
        break
    else:
        print("Please enter a number greater than 1 to start the game.")

while True:
    # Main loop for the game
    while n_coins > 1:
        # Player 1's turn
        move_1 = int(input("Player 1: Enter a non-zero positive square number: "))
        if move_1 <= 0 or not is_square_number(move_1) or move_1 >= n_coins:
            # Check for valid input from Player 1
            print("Invalid input!")
            continue
        n_coins -= move_1
        print(f"Now we have {n_coins} coins.")
        if n_coins <= 1:
            print("Player 2 wins!")  # Player 2 wins if there's only one coin left
            break

        # Player 2's turn
        move_2 = int(input("Player 2: Enter a non-zero positive square number: "))
        if move_2 <= 0 or not is_square_number(move_2) or move_2 >= n_coins:
            # Check for valid input from Player 2
            print("Invalid input!")
            continue
        n_coins -= move_2
        print(f"Now we have {n_coins} coins.")
        if n_coins <= 1:
            print("Player 1 wins!")  # Player 1 wins if there's only one coin left
            break

    # Ask if the players want to play again
    if input("Do you want to play again? (yes/no): ").lower() != 'yes':
        break
#