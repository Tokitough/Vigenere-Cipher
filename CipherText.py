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
    # define the first alphabet letter to get position in alphabet
    # get the position of the plaintext character
    # formula for encryption or decryption
    # get character of the ASCII code
# return ciphertext
# implement decrypt method to get plaintext
# ask user to input message
# print output

