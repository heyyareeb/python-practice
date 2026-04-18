from random import choice

from game_data import data
from art import logo,vs
import random


#account data into printable form
def format_data(account):
    account_name = account["name"]
    account_des = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_des}, from {account_country}"



def check_answer(user_guess, a_follower, b_follower):
    if a_follower > b_follower:
        return user_guess == "a"
    else:
        return user_guess == "b"

print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    #random account from thr game data
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random,choice(data)


    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    #ask user how has more followers
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    #clear screen
    print("\n"*22)
    print(logo)

    #check follower_count
    a_follow_count = account_a["follower_count"]
    b_follow_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follow_count, b_follow_count)

    #response to user on their guess
    if is_correct:
        score += 1
        print(f"you're right! Current score:{score}")
    else:
        print(f"sorry, that's wrong. Final score: {score}")
        game_should_continue = False


#swap position btw A and B
