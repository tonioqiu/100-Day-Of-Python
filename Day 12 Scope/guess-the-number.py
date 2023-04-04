import random

def guess_the_number():
    number = random.randint(1, 100)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        attempts = 10
    elif difficulty == "hard":
        attempts = 5
    else:
        print("Invalid difficulty. You lose.")
        return

    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Guess the number: "))
        if guess == number:
            print("You guessed it!")
            break
        elif guess > number:
            print("Too high")
            attempts -= 1
        else:
            print("Too low")
            attempts -= 1
    if attempts == 0:
        print("You ran out of guesses. You lose.")
        return


guess_the_number()

