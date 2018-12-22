from microbit import *

alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
while(1):
    for char in alphabets:
        display.show(char)
        sleep(250)
        
    sleep(1000)