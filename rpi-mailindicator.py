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
