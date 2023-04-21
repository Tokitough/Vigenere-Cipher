# implement key padding method
def _pad_key(plaintext, key):
    paddedKey = ''
    i = 0
    
# loop over the characters
    for char in plaintext:
        if char.isalpha():
            paddedKey += key[i % len(key)]
            i += 1
        else:
            paddedKey += ' '
    return paddedKey

# implement ecrypt_decrypt method
def _encrypt_decrypt_char(plaintextChar, keyChar, mode='encrypt'):
    if plaintextChar.isalpha():
        # define the first alphabet letter to get position in alphabet
        firstAlphabetLetter = 'a'
        if plaintextChar.isupper():
            firstAlphabetLetter = 'A'
            
        # get the position of the plaintext character
        oldCharPosition = ord(plaintextChar) - ord(firstAlphabetLetter)
        keyCharPosition = ord(keyChar.upper()) - ord('A')

        # formula for encryption or decryption
        if mode == 'encrypt':
            newCharPosition = (oldCharPosition + keyCharPosition) % 26
        else:
            newCharPosition = (oldCharPosition - keyCharPosition + 26) % 26
            
        # get character of the ASCII code
        return chr(newCharPosition + ord(firstAlphabetLetter))
    return plaintextChar

# return ciphertext
# implement decrypt method to get plaintext
# ask user to input message
# print output

