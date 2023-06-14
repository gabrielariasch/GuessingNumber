import random
game_on = True
numbers = range(1,101)
guessing_number = random.choice(numbers)

print(guessing_number)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
difficulty = input("Type 'easy' or 'hard': ").lower()

if difficulty == 'easy':
    lives = 10
else:
    lives = 5

while game_on:
    if difficulty == 'easy':
        if lives == 0:
            print("Game over. You ran out of attempts")
            break
        print(f"You have {lives} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        if guess == guessing_number:
            print("You won!")
            game_on = False
        elif guess > guessing_number:
            print("Too high")
            print("Guess again")
            lives -= 1
        elif guess < guessing_number:
            print("Too low")
            print("Guess again")
            lives -= 1
    else:
        if lives == 0:
            print("Game over. You ran out of attempts")
            break
        print(f"You have {lives} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        if guess == guessing_number:
            print("You won!")
            game_on = False
        elif guess > guessing_number:
            print("Too high")
            print("Guess again")
            lives -= 1
        elif guess < guessing_number:
            print("Too low")
            print("Guess again")
            lives -= 1