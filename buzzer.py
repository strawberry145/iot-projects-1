#!/usr/bin/python

import RPi.GPIO as GPIO         #importieren der benoetigten Bibliotheken
import time

buzzer_pin = 12                 #buzzer_pin wird definiert

GPIO.setmode(GPIO.BOARD)
GPIO.setup(buzzer_pin, GPIO.OUT)

GPIO.output(buzzer_pin, GPIO.HIGH)      #Gebe Geraeusch aus

time.sleep(0.5)                         #warte eine halbe Sekunde
print("Buzzer activated")

GPIO.output(buzzer_pin, GPIO.LOW)       #Stoppe Geraeuschausgabe

GPIO.cleanup()
