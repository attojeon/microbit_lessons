from microbit import *

class Directions:
    def __init__(self):
        self.arrow = 0
        self.images = []
        self.images.extend([Image.ARROW_N, Image.ARROW_NE, Image.ARROW_E])
        self.images.extend([Image.ARROW_SE, Image.ARROW_S, Image.ARROW_SW])
        self.images.extend([Image.ARROW_W, Image.ARROW_NW])
        print(self.images)
        
    def show(self):
        display.show(self.images[self.arrow])
        sleep(1000)
        self.arrow = self.arrow+1
        if self.arrow == len(self.images):
            self.arrow = 0
        
    
it = Directions()
while True:
    it.show()
    