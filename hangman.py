#Copyright 2016
#Python Hangman game
#Pretty simple, allows difficulties, but uses predetermined wordlists
#Planned feature: pick words at random from online dictionary and
#compare length to difficulty level

import random, sys
if sys.version_info >= (3,0):
    raw_input = input

alphabet = "abcdefghijklmnopqrstuvwxyz"
used = ""
working = ""
easy = ["Apple","Orange","Blue","Kittens","Puppies","Tower","Stuff"]
medium = ["California","Netherlands","United Kingdom","Gelatinous","Garbage Can","Olive Branch"]
hard = ["Xeroderma Pigmentosum","Canis Familiaris","Hypochondriac","Melancholy","Panthera leo"]
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
   /|     |
          |
          |
          |
    ---------
''','''
    -------
    |     |
    O     |
   /|\    |
          |
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

if difficulty == 1:
    n = random.randint(0,len(easy)-1)
    answer = easy[n]
if difficulty == 2:
    n = random.randint(0,len(medium)-1)
    answer = medium[n]
if difficulty == 3:
    n = random.randint(0,len(hard)-1)
    answer = hard[n]

for i in range(0,len(answer)):
    if answer[i] in alphabet: working += "_"
    else: working += " "

while True:
    print(str(hanger[wrong]))
    print(str(working[0:]))
    if wrong > 0:
        print("You have used the following letters: ")
        print(used)
        print("\n")
    if wrong == 5:
        print("Sorry! The answer was {0}".format(answer))
        exit()
    guess = raw_input("\nGuess a letter: ")
    if len(guess) != 1:
        print("Please choose only one letter!")
        continue
    if guess.lower() not in alphabet:
        print("Please select a real letter!")
        continue
    if guess in used:
        print("You've already guessed that!")
        continue
    used += "{0}, ".format(guess.upper())
    if guess.lower() in answer.lower():
        for i in range(0,len(answer)):
            if guess.lower() == answer[i].lower():
                working = list(working)
                working[i] = answer[i]
                working = "".join(working)
    else:
        print("Sorry! That's not right!")
        wrong += 1
    if working == answer:
        print("Yay! You got it! The answer was {0}!".format(answer))
        exit()
