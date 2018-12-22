# Write your code here :-)
from microbit import *

arrow_list = [
Image.ARROW_N, 
Image.ARROW_NE, 
Image.ARROW_E, 
Image.ARROW_SE, 
Image.ARROW_S, 
Image.ARROW_SW, 
Image.ARROW_W, 
Image.ARROW_NW
]

for this_image in arrow_list:
    display.show(this_image)
    sleep(250)