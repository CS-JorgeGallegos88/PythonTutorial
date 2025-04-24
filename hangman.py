import random

#word_list = ["aaardvark", "baboon", "camel"]
word_list = ["baboon"]
chosen_word = random.choice(word_list)
print(chosen_word)

place_holder = ""
for letter_in_scope in chosen_word:
    place_holder += "_ "

print(place_holder)

attempts = 0
correct_letters = []
guess_count = 0
game_over = False

while not game_over:
    if guess_count == len(chosen_word):
        print("You win!!!!")
        break
    
    guess = input("Guess a letter: ").lower()
    if not guess in chosen_word:
        attempts += 1
        if attempts == 6:
            print("You loose!!!!")
            break

    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
            guess_count += 1 
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
        
    print(display)



#print(f"Attempts: {attempts}")
