#15 minutes
'''
    Caesar Cipher - encrypt
    Input: plaintext message to encrypt, number of spaces to shift by.
    Output: encrypted message
'''

def getKey():
    key = 0
    print("Shift by: ")
    key = int(input())
    if key < 27 and key > 0:
        return key
    else:
        print("Key must be in range 1 to 26 inclusive.")
        getKey()

def encrypt(plaintext, key):
    plaintext.lower()
    shiftBy = key - 32
    for symbol in plaintext:
        if symbol.isalpha():
            currentValue = ord(symbol)
            newValue = currentValue + shiftBy
            if newValue>90:
                newValue = newValue - 26
            newChar = chr(newValue)
            print(newChar, end = "")
        else:
            print(symbol, end = "")

#main method
print("Enter a message to encrypt: ")
plaintext = str(input())
key = int(getKey())
encrypt(plaintext, key)
