# Imports go at the top
from microbit import *


# Code in a 'while True:' loop repeats forever

while True:
    Image1 = Image(
              '90009:'
              '09090:'
              '00900:'
              '09090:'
              '90009:'
    )
    if button_a.was_pressed():
       display.show(Image1)
       sleep(2000)
       display.show(Image(
              '00000:'
              '00009:'
              '00090:'
              '90900:'
              '09000:'
       
    ))
       sleep(2000)
       display.show(Image1)
            
