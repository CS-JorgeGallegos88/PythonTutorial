alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def encode(original_text, shift_amount):
    cipher_text = ""
    for character in original_text:
        if character in alphabet:
            original_index = alphabet.index(character)
            shifted_position = (original_index + shift_amount) % len(alphabet)
            cipher_text += alphabet[shifted_position]
        else:
            cipher_text += character  # mantener espacios u otros caracteres
    print(f"Encoded word: {cipher_text}")

def decode(original_text, shift_amount):
    cipher_text = ""
    for character in original_text:
        if character in alphabet:
            shifted_position = (alphabet.index(character) - shift_amount) % len(alphabet)
            cipher_text += alphabet[shifted_position]
        else:
            original_text += character
    print(f"Decoded word: {cipher_text}")

def caesar(text, shift, mode):
    result_text = ""
    for character in text:
        if character in alphabet:
            index = alphabet.index(character)
            if mode == "encode":
                new_index = (index + shift) % len(alphabet)
            elif mode == "decode":
                new_index = (index - shift) % len(alphabet)
            result_text += alphabet[new_index]
        else:
            result_text += character  # mantener espacios u otros caracteres
    print(f"{mode}d word: {result_text}")

user_choice = input("Type \'encode' to encrypt, type \'decode' to decrypt: ").lower()
text = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))

if user_choice == 'encode' or user_choice == 'decode':
    caesar(text, shift, user_choice)
else:
    print("Invalid option")