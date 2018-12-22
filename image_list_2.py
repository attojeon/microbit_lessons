from microbit import *

class FaceSamples:
    def __init__(self):
        self.arrow = 0
        self.images = []
        self.images.extend([Image.HEART, Image.HEART_SMALL, Image.SMILE])
        self.images.extend([Image.SAD, Image.CONFUSED, Image.ANGRY])
        self.images.extend([Image.ASLEEP, Image.SURPRISED, Image.SILLY])
        self.images.extend([Image.FABULOUS, Image.MEH, Image.YES, Image.NO])
        print(self.images)
        
    def show(self):
        display.show(self.images[self.arrow])
        sleep(1000)
        self.arrow = self.arrow+1
        if self.arrow == len(self.images):
            self.arrow = 0
        
    
it = FaceSamples()
while True:
    it.show()
    