alphabet = ['.', '!', '?', ' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        char_index = alphabet.index(char)
        encrypted_index = char_index + shift
        if(encrypted_index >= len(alphabet)):
            encrypted_index -= len(alphabet)
        encrypted_message += alphabet[encrypted_index]
    return encrypted_message

def decrypt(message, shift):
    decrypted_message = ""
    for char in message:
        char_index = alphabet.index(char)
        decrypted_index = char_index - shift
        if(decrypted_index < 0):
            decrypted_index += len(alphabet)
        decrypted_message += alphabet[decrypted_index]
    return decrypted_message

run_program = True
while(run_program):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction != "encode" and direction != "decode":
        continue
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % len(alphabet)

    if direction == "encode":
        print(encrypt(text, shift))
    elif direction == "decode":
        print(decrypt(text, shift))
    keep_going = input("Do you want to keep going? y/n: ")
    if(keep_going != "y"):
        run_program = False
