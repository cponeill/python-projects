#Copyright 2016
#This is a work-in-progress script that can be customized
#Intended for use on a Raspberry Pi 2 board with a red LED connected at pin GPIO 2, yellow LED at pin GPIO 3, and green LED at pin
#GPIO 4. However, you can use arguments to specify other BCM mode pin numbers
#Also, please be sane and use resistors on your LEDs. Make sure that the ANODE (+, positive) lead is directly connected to
#desired output pin, and that the CATHODE (-, negative) lead is connected to a ground pin with a resistor between them.

#The main purpose of this script is to create an LED indicator bar to tell you if you have unread email in your GMail inbox.
#Red light means you have mail in the Important category
#Yellow light means you have mail in the Finances category
#Green light means you have mail that has not been filtered into another category.
#This does require that you set up mail filter rules in GMail on your own, this script will NOT do it for you
#Usage:
#rpi-mailindicator.py -u GMAIL-ADDRESS -p GMAIL-PASSWORD
#optional arguments: -r RED_LIGHT_PIN -y YELLOW_LIGHT_PIN -g GREEN_LIGHT_PIN

import sys, imaplib
import RPi.GPIO as g
from time import sleep

red_pin, yellow_pin, green_pin = 2, 3, 4

if '-u' not in sys.argv:
  print "You must supply a username!"
  exit(1)
  
if '-p' not in sys.argv:
  print "You must supply a password!"
  exit(1)
  
for i in sys.argv:
  if sys.argv[i] == "-u": USERNAME = sys.argv[i+1]
  if sys.argv[i] == "-p": PASSWORD = sys.argv[i+1]
  if sys.argv[i] == "-r": red_pin = int(sys.argv[i+1])
  if sys.argv[i] == "-y": yellow_pin = int(sys.argv[i+1])
  if sys.argv[i] == "-g": green_pin = int(sys.argv[i+1])

#Setup the GPIO header as needed/desired  
g.setmode(g.BCM)
g.setup(red_pin, g.OUT, pull_up_down=g.PUD_DOWN)
g.setup(yellow_pin, g.OUT, pull_up_down=g.PUD_DOWN)
g.setup(green_pin, g.OUT, pull_up_down=g.PUD_DOWN)
g.output(red_pin, 0)
g.output(yellow_pin, 0)
g.output(green_pin, 0)

#Now, let's get signed into G-Mail...
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(USERNAME, PASSWORD)

#Okay, here is the loop that checks for unseen email in different folders/categories. Because this is meant to be an
#"always on" type script, there will be a sleep at the end to prevent busy waiting and over-use of the processor.
#Also, I suggest running this script with a trailing & or in a screen instance so that you can still use your terminal
while True:
  mail.select('inbox')
  green_count = mail.search(None,'UnSeen')
  mail.select('finances') #Change this to whatever category you want for the yellow light
  yellow_count = mail.search(None, 'UnSeen')
  mail.select('important') #Change this whatever category you want for the red light
  red_count = mail.search(None, 'UnSeen')
  if red_count == 0: g.output(red_pin, 0)
  else: g.output(red_pin, 1)
  if yellow_count == 0: g.output(yellow_pin, 0)
  else: g.output(yellow_pin, 1)
  if green_count == 0: g.output(green_pin, 0)
  else: g.output(green_pin, 1)
  sleep(0.5)
