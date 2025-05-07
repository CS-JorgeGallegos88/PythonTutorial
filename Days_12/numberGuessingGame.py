import random

computer_choice = random.randint(1, 101)
#print(f"Computer choice: {computer_choice}")

print("Welcom to the Number Guessing game!\nI'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty, type 'easy' or 'hard': ").lower()

def start_game(max_number_of_attempts):
    #Start game
    while max_number_of_attempts > 0:
        
        if max_number_of_attempts > 1:
            print(f"You have {max_number_of_attempts} remaining to guess the number")
        else:
            print(f"Last chance!")

        user_guess = int(input("Make a guess: "))
        if user_guess == computer_choice:
            print("You win")
            break
        
        high_range = user_guess - computer_choice
        low_range = computer_choice - user_guess

        if (low_range) >= 30:
            max_number_of_attempts -= 1
            print("Too low!") # muy lejos hacia abajo
        elif (high_range) >= 30:
            max_number_of_attempts -= 1
            print("Too high!") # muy lejos hacia arriba
        elif (low_range) >= 10:
            max_number_of_attempts -= 1
            print("You are still under") # solo un poco lejos hacia abajo
        elif (high_range) >= 10:
            max_number_of_attempts -= 1
            print("You are still up") # solo un poco lejos hacia arriba
        elif (low_range) >= 5:
            max_number_of_attempts -= 1
            print("Up a bit") # muy cerca hacia abajo
        elif (high_range) >= 5:
            max_number_of_attempts -= 1
            print("Low a bit") # muy cerca hacia arriba
        elif max_number_of_attempts == 0:
            print(f"You lose, the number was {computer_choice}") #Avisar que el jugador perdio
        else:
            max_number_of_attempts -= 1
            print("You are close...")

max_attempts = 0
if difficulty == "easy":
    max_attempts = 10
    start_game(max_attempts)
elif difficulty == "hard":
    max_attempts = 5
    start_game(max_attempts)
else:
    print("Invalid difficulty, game over!")











