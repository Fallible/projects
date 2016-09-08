#Program to encrypt or decrypt string.
#Accepts a string for encryption or decryption, an int for shift distance, and a flag to determine which direction to shift.


# Needed functions:
#    cesarX(char, int) returns char
#    shiftUp(char) returns char
#    shiftDown(char) returns char   

import sys

def shiftUp(c):
    if c == 'z':
        return 'a'
    if c == 'Z':
        return 'A'
    else:
        return chr(ord(c) + 1)

def shiftDown(c):
    if c == 'a':
        return 'z'
    if c == 'A':
        return 'Z'
    else:
        return chr(ord(c) - 1)

def cesarX(char, shift):
    for i in range(0, shift, 1 if shift > 0 else -1):
	if shift > 0:
            char = shiftUp(char)
        else:
            char = shiftDown(char)
    return char

def cesarString(string, shift):
    result = ''
    for char in string:
        result = result + cesarX(char, shift)
	if shift > 0:
            shift += 1
        else:
            shift -= 1
    return result

inputString = sys.argv[1]

cesarKey = int(sys.argv[2])

print (cesarString(inputString, cesarKey))
