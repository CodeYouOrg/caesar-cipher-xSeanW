alphabet = "abcdefghijklmnopqrstuvwxyz"

shift = 5

test = "python is fun!"

cipher = ""

for char in test.lower():
    if char in alphabet:
        letter = alphabet.index(char)
        letter += shift
        cipher += alphabet[letter % 26]
    else: 
            cipher = cipher + char


print(cipher)