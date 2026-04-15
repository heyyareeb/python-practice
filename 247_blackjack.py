import random
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]




def calculate_score(cards):
    """Take a lis of cards and calculate the score"""
    if sum(cards)== 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draww"
    elif c_score == 0:
        return "Lose, opponent has Blackjack"
    elif u_score == 0:
        return "Win with a Blackjack"
    elif u_score > 21:
        return "You went over. You lose"
    elif c_score > 21:
        return "Opponent went over. You Win"
    elif u_score > c_score:
        return "You win"
    else:
        return "You lose"

def play_game():
    print(logo)
    user_card = []
    user_score = -1
    computer_card = []
    computer_score = -1


    is_game_over = False

    user_card.append(random.choice(cards))
    user_card.append(random.choice(cards))

    computer_card.append(random.choice(cards))
    computer_card.append(random.choice(cards))


    while not is_game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        print(f"Your cards: {user_card}, current score: {user_score}")
        print(f"Computer's first card: {computer_card[0]}")


        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal= input("Type 'y' to get another card or type 'n' to pass: ")
            if user_should_deal == "y":
                user_card.append(random.choice(cards))
            else:
                is_game_over = True



    while computer_score != 0 and computer_score < 17:
        computer_card.append(random.choice(cards))
        computer_score = calculate_score(computer_card)

    print(f"Your final hand: {user_card}, final score: {user_score}")
    print(f"Computer's final hand {computer_card}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("would you like to play again y for 'yes' or n for 'no: "):
    print("\n" * 18)
    play_game()