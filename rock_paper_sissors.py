import random

# Rock
rock_ascii = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper_ascii = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
sissors_ascii = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

game_choices = ["Rock", "Paper", "Sissors"]
image_choices = [rock_ascii, paper_ascii, sissors_ascii]

computer_choice_index = random.randint(0, 2)
my_choice = input("Please select an option R for rock, P for papper, S for Sissors:\n").upper()

if my_choice != "R" and my_choice != "P" and my_choice != "S":
    print("That is not a valid option, game over")
    exit()

if my_choice == "R":
    my_choice_index = 0

if my_choice == "P":
    my_choice_index = 1

if my_choice == "S":
    my_choice_index = 2

print(f"You chose: {game_choices[my_choice_index]} \n")
print(image_choices[my_choice_index])
print("\n")
print(f"Computer choice: {game_choices[computer_choice_index]} \n")
print(image_choices[computer_choice_index])
print("\n")

if my_choice_index == computer_choice_index:
    print("Draw")
elif computer_choice_index == 2 and my_choice_index == 0:
    print("You win!!! \U0001F606")
    print(f"{game_choices[my_choice_index]} beats {game_choices[computer_choice_index]}")
elif computer_choice_index > my_choice_index:
    print("Computer wins \U0001F610")
    print(f"{game_choices[computer_choice_index]} beats {game_choices[my_choice_index]}")
else:
    print("You win!!! \U0001F606")
    print(f"{game_choices[my_choice_index]} beats {game_choices[computer_choice_index]}") 