def solution(x):
    deciphered_string = ""
    for char in x:
        # Check if the character is a lowercase letter
        if char.islower():
            # Decipher the lowercase letter and append to the result
            deciphered_char = chr(ord('z') - (ord(char) - ord('a')))
            deciphered_string += deciphered_char
        else:
            # Keep non-lowercase letters unchanged and append to the result
            deciphered_string += char
    return deciphered_string
