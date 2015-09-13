'''
    Caesar Cipher - encrypt and decrypt
    Takes as input: 'e'/'d', key, plaintext/ciphertext
    Outputs: ciphertext/plaintext
'''
import os

def encrypt(plaintext, key):
    plaintext = plaintext.lower()
    shiftBy = key - 32
    for symbol in plaintext:
        if symbol.isalpha():
            currentValue = ord(symbol)
            newValue = currentValue + shiftBy
            if newValue > 90:
                newValue = newValue - 26
            newChar = chr(newValue)
            print(newChar, end = "")
        else:
            print(symbol, end = "")


def decrypt(ciphertext, key):
    ciphertext = ciphertext.upper()
    shiftBy = 32 - key
    for symbol in ciphertext:
        if symbol.isalpha():
            currentValue = ord(symbol)
            newValue = currentValue + shiftBy
            if newValue > 122:
                newValue = newValue - 26
            elif newValue < 97:
                newValue = newValue + 26
            newChar = chr(newValue)
            print(newChar, end="")
        else:
            print(symbol, end="")


#main method
print("Encrypt (e) or decrypt (d)?")
decisionDirect = str(input())
print("Key (integer between 1 and 26 inclusive): ")
key = int(input())
if key < 27 and key > 0:
    if decisionDirect.lower() == "e" or decisionDirect.lower() == "encrypt":
        print("Enter a message to encrypt: ")
        plaintext = str(input())
        encrypt(plaintext, key)
    elif decisionDirect.lower() == "d" or decisionDirect.lower() =="decrypt":
        print("Enter a message to decrypt: ")
        ciphertext = str(input())
        decrypt(ciphertext, key)
else:
    print("key not in range")

print(" ")
os.system("pause")

