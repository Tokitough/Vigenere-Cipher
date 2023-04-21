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
def encrypt(plaintext, key):
    ciphertext = ''
    paddedKey = _pad_key(plaintext, key)
    for plaintextChar, keyChar in zip(plaintext, paddedKey):
        ciphertext += _encrypt_decrypt_char(plaintextChar, keyChar)
    return ciphertext

# implement decrypt method to get plaintext
def decrypt(ciphertext, key):
    plaintext = ''
    paddedKey = _pad_key(ciphertext, key)
    for ciphertextChar, keyChar in zip(ciphertext, paddedKey):
        plaintext += _encrypt_decrypt_char(ciphertextChar, keyChar, mode='decrypt')
    return plaintext

# ask user to input message
print("\u001b[30m=" * 50)
print("\u001b[33mType your input in all UPPERCASE and no spaces")
plaintext = input("\033[95mEnter a message: ")
key = input("\033[1;32mEnter a key: ")
print("\u001b[30m=" * 50)

# print output
ciphertext = encrypt(plaintext, key)
decryptedPlaintext = decrypt(ciphertext, key)

print(f'\033[95mCiphertext: {ciphertext}')
print(f'\033[1;32mDecrypted Plaintext: {decryptedPlaintext}')
print("\u001b[30m=" * 50)
