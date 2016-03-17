#!/usr/bin/env python

#Copyright 2016
#This is a script for encrypting/decrypting messages using a Vigenere Cipher
#You will be asked if you want to encrypt or decrypt, the key you wish to use
#and the message.

import sys

if sys.version_info >= (3,0): raw_input = input

s = [[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0],[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1],[3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2],[4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3],[5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4],[6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5],[7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6],[8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7],[9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8],[10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9],[11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10],[12,13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11],[13,14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12],[14,15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13],[15,16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14],[16,17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],[17,18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],[18,19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17],[19,20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18],[20,21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],[21,22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],[22,23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21],[23,24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22],[24,25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],[25,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]]
f = ''

for i in range(0,len(s)):
    for j in range(0,len(s[i])):
        if s[i][j] == 0: s[i][j] = "A"
        if s[i][j] == 1: s[i][j] = "B"
        if s[i][j] == 2: s[i][j] = "C"
        if s[i][j] == 3: s[i][j] = "D"
        if s[i][j] == 4: s[i][j] = "E"
        if s[i][j] == 5: s[i][j] = "F"
        if s[i][j] == 6: s[i][j] = "G"
        if s[i][j] == 7: s[i][j] = "H"
        if s[i][j] == 8: s[i][j] = "I"
        if s[i][j] == 9: s[i][j] = "J"
        if s[i][j] == 10: s[i][j] = "K"
        if s[i][j] == 11: s[i][j] = "L"
        if s[i][j] == 12: s[i][j] = "M"
        if s[i][j] == 13: s[i][j] = "N"
        if s[i][j] == 14: s[i][j] = "O"
        if s[i][j] == 15: s[i][j] = "P"
        if s[i][j] == 16: s[i][j] = "Q"
        if s[i][j] == 17: s[i][j] = "R"
        if s[i][j] == 18: s[i][j] = "S"
        if s[i][j] == 19: s[i][j] = "T"
        if s[i][j] == 20: s[i][j] = "U"
        if s[i][j] == 21: s[i][j] = "V"
        if s[i][j] == 22: s[i][j] = "W"
        if s[i][j] == 23: s[i][j] = "X"
        if s[i][j] == 24: s[i][j] = "Y"
        if s[i][j] == 25: s[i][j] = "Z"

while True:
    try:
        q = int(raw_input("Would you like encrypt(1) or decrypt(2)? "))
        if not q == 1 and not q == 2: print("Please enter a valid selection!")
        else: break
    except ValueError: print("Please enter a valid selection!")


if q == 1:
    while True:
        k = str(raw_input("Key word: ")).upper()
        if not k.isalnum():
            print("Please enter only letters!")
        elif any(c.isdigit() for c in k):
            print("Please enter only letters!")
        else: break
    while True:
        m = str(raw_input("Message: ")).upper()
        if not m.isalnum(): print("Please enter only letters!")
        elif any(c.isdigit() for c in m): print("Please enter only letters!")
        else: break

    while True:
        if len(k) < len(m): k *= 2
        elif len(k) > len(m):
            d = len(k) - len(m)
            k = k[:-d]
            break
        else: break

    k = list(k)
    m = list(m)

    for i in range(0,len(k)):
        if k[i] == "A": k[i] = 0
        if k[i] == "B": k[i] = 1
        if k[i] == "C": k[i] = 2
        if k[i] == "D": k[i] = 3
        if k[i] == "E": k[i] = 4
        if k[i] == "F": k[i] = 5
        if k[i] == "G": k[i] = 6
        if k[i] == "H": k[i] = 7
        if k[i] == "I": k[i] = 8
        if k[i] == "J": k[i] = 9
        if k[i] == "K": k[i] = 10
        if k[i] == "L": k[i] = 11
        if k[i] == "M": k[i] = 12
        if k[i] == "N": k[i] = 13
        if k[i] == "O": k[i] = 14
        if k[i] == "P": k[i] = 15
        if k[i] == "Q": k[i] = 16
        if k[i] == "R": k[i] = 17
        if k[i] == "S": k[i] = 18
        if k[i] == "T": k[i] = 19
        if k[i] == "U": k[i] = 20
        if k[i] == "V": k[i] = 21
        if k[i] == "W": k[i] = 22
        if k[i] == "X": k[i] = 23
        if k[i] == "Y": k[i] = 24
        if k[i] == "Z": k[i] = 25
    for i in range(0,len(m)):
        if m[i] == "A": m[i] = 0
        if m[i] == "B": m[i] = 1
        if m[i] == "C": m[i] = 2
        if m[i] == "D": m[i] = 3
        if m[i] == "E": m[i] = 4
        if m[i] == "F": m[i] = 5
        if m[i] == "G": m[i] = 6
        if m[i] == "H": m[i] = 7
        if m[i] == "I": m[i] = 8
        if m[i] == "J": m[i] = 9
        if m[i] == "K": m[i] = 10
        if m[i] == "L": m[i] = 11
        if m[i] == "M": m[i] = 12
        if m[i] == "N": m[i] = 13
        if m[i] == "O": m[i] = 14
        if m[i] == "P": m[i] = 15
        if m[i] == "Q": m[i] = 16
        if m[i] == "R": m[i] = 17
        if m[i] == "S": m[i] = 18
        if m[i] == "T": m[i] = 19
        if m[i] == "U": m[i] = 20
        if m[i] == "V": m[i] = 21
        if m[i] == "W": m[i] = 22
        if m[i] == "X": m[i] = 23
        if m[i] == "Y": m[i] = 24
        if m[i] == "Z": m[i] = 25

    for i in range(0,len(k)): f += s[k[i]][m[i]]


if q == 2:
    while True:
        k = str(raw_input("Key Word: ")).upper()
        if not k.isalnum(): print("Please enter only letters!")
        elif any(c.isdigit() for c in k): print("Please enter only letters!")
        else: break
    while True:
        m = str(raw_input("Encrypted message: ")).upper()
        if not m.isalnum(): print("Please enter only letters!")
        elif any(c.isdigit() for c in m): print("Please enter only letters!")
        else: break
    while True:
        if len(k) < len(m): k *= 2
        elif len(k) > len(m):
            d = len(k)-len(m)
            k = k[:-d]
        else: break
    k = list(k)
    m = list(m)
    for i in range(0,len(k)):
        if k[i] == "A": k[i] = 0
        if k[i] == "B": k[i] = 1
        if k[i] == "C": k[i] = 2
        if k[i] == "D": k[i] = 3
        if k[i] == "E": k[i] = 4
        if k[i] == "F": k[i] = 5
        if k[i] == "G": k[i] = 6
        if k[i] == "H": k[i] = 7
        if k[i] == "I": k[i] = 8
        if k[i] == "J": k[i] = 9
        if k[i] == "K": k[i] = 10
        if k[i] == "L": k[i] = 11
        if k[i] == "M": k[i] = 12
        if k[i] == "N": k[i] = 13
        if k[i] == "O": k[i] = 14
        if k[i] == "P": k[i] = 15
        if k[i] == "Q": k[i] = 16
        if k[i] == "R": k[i] = 17
        if k[i] == "S": k[i] = 18
        if k[i] == "T": k[i] = 19
        if k[i] == "U": k[i] = 20
        if k[i] == "V": k[i] = 21
        if k[i] == "W": k[i] = 22
        if k[i] == "X": k[i] = 23
        if k[i] == "Y": k[i] = 24
        if k[i] == "Z": k[i] = 25

    for i in range(0,len(m)):
        f += s[0][s[k[i]].index(m[i])]

print("Your result is:\n{0}\n".format(f))
