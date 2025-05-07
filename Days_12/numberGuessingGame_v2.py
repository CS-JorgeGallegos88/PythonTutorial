import random

'''
La función abs() en Python es muy útil y su propósito es obtener el valor absoluto de un número, es decir, el valor sin tener en cuenta si es positivo o negativo.
¿Por qué usar abs() para get_feedback()?
- En tu lógica, estás comparando la diferencia entre la suposición del usuario y el número de la computadora. Sin embargo, esta diferencia puede ser tanto positiva como negativa. Por ejemplo:
- Si el número de la computadora es 50 y el usuario adivina 40, la diferencia será -10.
- Si el número de la computadora es 50 y el usuario adivina 60, la diferencia será +10.
'''

def get_feedback(diff):
    """Devuelve retroalimentación basada en la diferencia."""
    if diff >= 30:
        return "Too high!"
    elif diff <= -30:
        return "Too low!"
    elif abs(diff) >= 10:
        if diff > 0: #En esta linea no se evalua el valor absoluto, aqui diff puede ser menor a 0
            return "You are still up"
        else:
            return "You are still under"
    elif abs(diff) >= 5:
        if diff > 0:
            return "Low a bit"
        else:
            return "Up a bit"
    else:
        return "You are close..."

def start_game(max_attempts, computer_choice):
    while max_attempts > 0:
        print(f"You have {max_attempts} attempt{'s' if max_attempts > 1 else ''} remaining.")
        try:
            user_guess = int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if user_guess == computer_choice:
            print("🎉 You win!")
            return

        diff = user_guess - computer_choice
        print(get_feedback(diff))
        max_attempts -= 1

    print(f"😢 You lose, the number was {computer_choice}")

def main():
    computer_choice = random.randint(1, 100)  # El 100 sí entra aquí
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty, type 'easy' or 'hard': ").lower()

    if difficulty == "easy":
        start_game(10, computer_choice)
    elif difficulty == "hard":
        start_game(5, computer_choice)
    else:
        print("Invalid difficulty, game over!")

if __name__ == "__main__":
    main()
