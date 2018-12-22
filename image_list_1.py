from microbit import *

image_list = [
Image.HEART, Image.HEART_SMALL, Image.SMILE, Image.SAD, Image.CONFUSED, 
Image.ANGRY, Image.ASLEEP, Image.SURPRISED, Image.SILLY, Image.FABULOUS,
Image.MEH, Image.YES, Image.NO
]

while True:
    for it in image_list:
        display.show(it)
        sleep(1000)