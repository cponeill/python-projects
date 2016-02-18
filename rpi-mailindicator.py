#Copyright 2016
#This is a work-in-progress script that can be customized
#Intended for use on a Raspberry Pi 2 board with a red LED connected at pin GPIO 2, yellow LED at pin GPIO 3, and green LED at pin
#GPIO 4. However, you can use arguments to specify other BCM mode pin numbers

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
  
