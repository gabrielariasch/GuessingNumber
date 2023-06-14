# GuessingNumber

The code begins with importing the random module, which provides functions for generating random numbers.

The variable game_on is set to True, indicating that the game is currently running.

The variable numbers is created as a range of numbers from 1 to 100 (excluding 101).

The variable guessing_number is assigned a random number chosen from the numbers range using the random.choice() function.

The program then prints the guessing_number, which is the number the player needs to guess. This is done for debugging purposes and can be removed in a finished version of the game.

The program displays some introductory messages to the player, explaining the rules of the game.

The player is prompted to choose a difficulty level by entering 'easy' or 'hard'. The input is converted to lowercase using the lower() method to make it case-insensitive.

Depending on the chosen difficulty level, the variable lives is set to either 10 (easy) or 5 (hard). This variable represents the number of attempts the player has to guess the number correctly.

The game enters a while loop that continues until the game_on variable becomes False, indicating that the game is over.

Inside the loop, the program checks the difficulty level again to determine the behavior for each level.

If the difficulty is set to 'easy', the program checks if the player has run out of lives. If so, it prints a "Game over" message and breaks out of the loop, ending the game.

If the player still has lives remaining, the program displays the number of attempts left and prompts the player to make a guess using the input() function. The guess is converted to an integer using the int() function.

The program then compares the player's guess with the guessing_number generated at the beginning of the game.

If the guess is correct, the program prints a "You won!" message, sets game_on to False, and the game ends.

If the guess is higher than the guessing_number, the program prints "Too high" and "Guess again" messages, decreases the lives variable by 1, and continues the loop.

If the guess is lower than the guessing_number, the program prints "Too low" and "Guess again" messages, decreases the lives variable by 1, and continues the loop.

The same logic is repeated for the 'hard' difficulty level.
