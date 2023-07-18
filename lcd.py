#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import board
import busio
import adafruit_character_lcd.character_lcd_i2c as character_lcd

# Definiere LCD Zeilen und Spaltenanzahl.
lcd_columns = 16
lcd_rows    = 2

# Initialisierung I2C Bus
i2c = busio.I2C(board.SCL, board.SDA)

# Festlegen des LCDs in die Variable LCD
lcd = character_lcd.Character_LCD_I2C(i2c, lcd_columns, lcd_rows, 0x21)

try: 
    
    # Cursor anzeigen lassen.
    lcd.clear()
    lcd.cursor = True
    lcd.message = "motion"
 
except KeyboardInterrupt:
    # LCD ausschalten.
    lcd.clear()
    lcd.backlight = False
