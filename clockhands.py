from microbit import *

class ClockHands:
    def __init__(self):
        self.arrow = 0
        self.images = []
        self.images.extend([Image.CLOCK1, Image.CLOCK2, Image.CLOCK3])
        self.images.extend([Image.CLOCK4, Image.CLOCK5, Image.CLOCK6])
        self.images.extend([Image.CLOCK7, Image.CLOCK8, Image.CLOCK9])
        self.images.extend([Image.CLOCK10, Image.CLOCK11, Image.CLOCK12])
        print(self.images)
        
    def show(self):
        display.show(self.images[self.arrow])
        sleep(1000)
        self.arrow = self.arrow+1
        if self.arrow == len(self.images):
            self.arrow = 0
        
    
it = ClockHands()
while True:
    it.show()
    