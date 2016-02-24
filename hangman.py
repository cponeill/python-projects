#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Copyright 2016
#Python Hangman game

import random, sys
if sys.version_info >= (3,0):
    raw_input = input

alphabet = "abcdefghijklmnopqrstuvwxyz"
used = ""
working = ""
easy = []
medium = []
hard = []
with open("/usr/share/dict/words") as f:
    words = f.readlines()
    for i in range(0,len(words)):
        words[i] = words[i].strip("\n")
        if 3 <= len(words[i]) < 8: hard.append(words[i])
        if 8 <= len(words[i]) < 12: medium.append(words[i])
        if 12 <= len(words[i]): easy.append(words[i])
wrong = 0
hanger = ['''
    -------
    |     |
          |
          |
          |
          |
          |
    ---------
''','''
    -------
    |     |
    O     |
          |
          |
          |
          |
    ---------
''','''
    -------
    |     |
    O     |
    |     |
    |     |
          |
          |
    ---------
''','''
    -------
    |     |
    O     |
   /|     |
    |     |
          |
          |
    ---------
''','''
    -------
    |     |
    O     |
   /|\    |
    |     |
          |
          |
    ---------
''','''
    -------
    |     |
    O     |
   /|\    |
    |     |
   /      |
          |
    ---------
''','''
    -------
    |     |
    O     |
   /|\    |
    |     |
   / \    |
          |
    ---------
''']

print("Welcome to hangman!")
print('''1 - Easy
2 - Medium
3 - Hard''')

while True:
    try:
        difficulty = int(raw_input("Please choose your difficulty: "))
        if not 1 <= difficulty <=3:
            print("Please select a valid option.")
            continue
        else:
            break
    except ValueError:
        print("Please select a valid option.")
        continue
while True:
    if difficulty == 1:
        n = random.randint(0,len(easy)-1)
        answer = easy[n]
        if answer[0] not in alphabet: continue
        else: break
    if difficulty == 2:
        n = random.randint(0,len(medium)-1)
        answer = medium[n]
        if answer[0] not in alphabet: continue
        else: break
    if difficulty == 3:
        n = random.randint(0,len(hard)-1)
        answer = hard[n]
        if answer[0] not in alphabet: continue
        else: break

remaining = len(answer)

for i in range(0,len(answer)):
    if answer[i].lower() in alphabet: working += "_"
    else:
        working += answer[i]
        remaining -= 1

while True:
    print(str(hanger[wrong]))
    print(str(working[0:]))
    print("There are {0} letters left in the word.".format(remaining))
    if wrong > 0:
        print("You have used the following letters: ")
        print(used)
        print("\n")
    if wrong == len(hanger)-1:
        print("Sorry! The answer was {0}".format(answer))
        exit()
    guess = raw_input("\nGuess a letter: ")
    if len(guess) != 1:
        print("Please choose only one letter!")
        continue
    if guess.lower() not in alphabet:
        print("Please select a real letter!")
        continue
    if guess.upper() in used:
        print("You've already guessed that!")
        continue
    used += "{0}, ".format(guess.upper())
    if guess.lower() in answer.lower():
        for i in range(0,len(answer)):
            if guess.lower() == answer[i].lower():
                working = list(working)
                working[i] = answer[i]
                working = "".join(working)
                remaining -= 1
    else:
        print("Sorry! That's not right!")
        wrong += 1
    if working == answer:
        print("Yay! You got it! The answer was {0}!".format(answer))
        exit()
