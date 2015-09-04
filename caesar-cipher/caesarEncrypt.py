#15 minutes
'''
    Caesar Cipher - encrypt
    Input: plaintext message to encrypt, number of spaces to shift by.
    Output: encrypted message
'''
        
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
invalidKey = True
print("Shift plaintext by: ")
key = int(input())
if key < 27 and key > 0:
    print("Enter a message to encrypt: ")
    plaintext = str(input())
    encrypt(plaintext, key)
else:
    print("key not in range")
