#Ascii art for the options
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

#Importing the module
import random
#Assigning the values to a list
Choices = [rock, paper, scissors]
#Asking the player for their choice
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors "))
#Making the computer choose randomly
Comp_choice = int(random.randint(0,2))
#Making sure the player enters a valid input to avoid crashes
if player_choice >= 0 and player_choice <= 2:
  #Checking for a draw
  #and saving the result in a variable
  if player_choice == Comp_choice:
    Win_Lose = "Draw"
  #Checking if the player won
  elif player_choice == Comp_choice + 1:
    Win_Lose = "You win"
  #Checking if the player lost
  elif Comp_choice == player_choice + 1:
    Win_Lose = "You lose"
  print(f"You chose:\n{Choices[player_choice]}\n")
  print(f"Computer chose:\n{Choices[Comp_choice]}\n")
  print(Win_Lose)
else:
    #Showing the player that they lost
    #because they used an invalid number
    print("Invalid Number, You lose.")
