import random

# Lista con todas las letras del abecedario en inglés (mayúsculas y minúsculas)
letters = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]

# Lista con los números del 0 al 9 como strings
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# Lista con símbolos comúnmente aceptados en contraseñas
symbols = [
    "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+",
    "[", "]", "{", "}", ";", ":", "'", '"', ",", ".", "<", ">", "/", "?",
    "|", "\\", "`", "~"
]

print("Welcome to the PyPassword Generator")
number_of_letters = int(input("How many letters would you like in your password\n"))
number_of_symbols = int(input("How many symbols would you like in your password\n"))
number_of_numbers = int(input("How many numbers would you like in your password\n"))

password = ""

#Ejercicio facil
#iterar solo el numero de veces que el usuario seleccione
for rndm_index_in_letters in range(0, number_of_letters):
    random_index = random.randint(0, len(letters)-1)
    password += letters[random_index]

for rndm_index_in_symbols in range(0, number_of_symbols):
    random_index = random.randint(0, len(symbols)-1)
    password += symbols[random_index]

for rndm_index_in_numbers in range(0, number_of_numbers):
    random_index = random.randint(0, len(numbers)-1)
    password += numbers[random_index]

print(password)

#Ejercicio dificil
# Convertir la cadena en una lista de caracteres
password_list = list(password)
mixed_password = ""

# Mientras queden caracteres en la lista, extraer uno aleatoriamente y agregarlo a la nueva cadena
while password_list:
    random_index = random.randint(0, len(password_list) - 1)
    mixed_password += password_list.pop(random_index)

print(mixed_password)
