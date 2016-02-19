#Copyright 2016
#This script uses an array of questions, random numbers, and other basics
#to create a multiple choice quiz.
#Note to all of my students on brownvpn.tk, I will know if you use this
#as a template on the Quiz challenge.

from random import randint

questions = ['''What is the capital of California?
A - Sacramento
B - San Diego
C - San Francisco
D - Washington''','''Who was the first man to walk on the moon?
A - Neil Armstrong
B - Lance Armstrong
C - Monty Python
D - Nobody's actually been on the moon, crazy!''','''Which of these is a versatile, interpreted programming language?
A - C++
B - Boa Constrictor
C - Python
D - Flibbert''','''Should you use synthetic or long division when dividing a polynomial by a binomial?
A - Long
B - Synthetic
C - What are these? Away with your sorcery!
D - Whichever makes the most sense for the problem.''']

number = len(questions)

used = []
n = 0
score = 0

while true:
    j = randint(0, number)
    if j in used: continue
    n += 1
    print("Question {0}:\n".format(n))
    print questions[j]
    while true:
        answer = raw_input("Your answer: ".upper())
        if len(answer) > 1: print("Please only enter one letter.")
        elif answer not in ["A","B","C","D"]: print("Please select a valid answer."]
        else: break
    if j == 0 and answer == "A": score += 1
    if j == 1 and answer == "A": score += 1
    if j == 2 and answer == "C": score += 1
    if j == 3 and answer == "D": score += 1
    if n == number: break

print("Your score is {0}/{1}!".format(score,number))
