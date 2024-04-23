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

#Write your code below this line 👇

import random

Choices = [rock, paper, scissors]
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors "))
Comp_choice = int(random.randint(0,2))
if player_choice >= 0 and player_choice <= 2:
  if player_choice == Comp_choice:
    Win_Lose = "Draw"
  elif player_choice == Comp_choice + 1:
    Win_Lose = "You win"
  elif Comp_choice == player_choice + 1:
    Win_Lose = "You lose"
  print(f"You chose:\n{Choices[player_choice]}\n")
  print(f"Computer chose:\n{Choices[Comp_choice]}\n")
  print(Win_Lose)
else:
  print("Invalid Number, You lose.")
