import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''



game = ('rock', 'paper', 'scissors')

user = int(input("What do you choose? type 0 for rock, 1 for paper, 2 for scissors.\n"))
print("you chose--",game[user])

computer = random.randint(0,2)
print("computer chose--",game[computer])

if user >=3 or user <0:
    print("Invalid option")
elif user == computer:
    print("Draw")
elif user == 0 and computer == 1:
    print("You Lose")
elif user == 1 and computer == 0:
    print("You Win")
elif user == 1 and computer == 2:
    print("You Lose")
elif user == 2 and computer == 1:
    print("You win")
elif user == 2 and computer == 0:
    print("you Lose")
elif user == 0 and computer == 2:
    print("You win")
else:
    print ("You have entered an invalid option")
