print('''
      *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
      ''')

print("Welcome to treasure Quest")
print("Your mission is to find the treasure")

left_or_right = input("where do you want to go, left or right? ").upper().strip()
if left_or_right == "RIGHT":
    print("You fall into a hole, game over")
    exit()

swim_or_wait = input("Do you want to swim or wait? ").upper().strip()
if swim_or_wait == "SWIM":
    print("You were attacked by a shark, game over")
    exit()

door_color = input("Choose the color of your door (Red, Yellow or Blue): ").upper().strip()
if door_color == "RED":
    print("Burned by fire, game over")
elif door_color == "BLUE":
    print("You were eaten by bests, game over")
elif door_color == "YELLOW":
    print("You win!!!")
else:
    print("There is no door with this color, game over")
