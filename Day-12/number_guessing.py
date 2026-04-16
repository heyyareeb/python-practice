import random
import art
print(art.logo)

print("Welcome to the Number Guessing Game!")
print("Think a number between 1 to 100")


def game_level():
    level = input("Choose a difficulty 'easy' or 'hard': ")
    #easy = 10 , hard = 5
    if level == "easy":
        return 10
    elif level == "hard":
        return 5
    else:
        return "Invalid Input"

attempts = game_level()
print(f"You have {attempts} attempts")




def c_guess():
    return random.randint(1,100)

num = c_guess()



while attempts > 0:
    guess = int(input("Guess a number: "))
    if guess > num:
        print("Too high")
    elif guess < num:
        print("Too low")
    else:
        print("You Guessed the number. You win")

    attempts -= 1
    print(f"Attempts left: {attempts}")
    #game over condition
    if attempts == 0:
        print("You lost")
        print(f"The number was:  {num}")
