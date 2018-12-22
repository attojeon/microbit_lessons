from microbit import *

class ImageStore:
    def __init__(self, image_type):
        self.arrow = 0
        self.images = []
        self.set_type(image_type)
        
    def set_type(self, image_type):
        if image_type == "direction":
            self.images.extend([Image.ARROW_N, Image.ARROW_NE, Image.ARROW_E])
            self.images.extend([Image.ARROW_SE, Image.ARROW_S, Image.ARROW_SW])
            self.images.extend([Image.ARROW_W, Image.ARROW_NW])
        elif image_type == "face":
            self.images.extend([Image.HEART, Image.HEART_SMALL, Image.SMILE])
            self.images.extend([Image.SAD, Image.CONFUSED, Image.ANGRY])
            self.images.extend([Image.ASLEEP, Image.SURPRISED, Image.SILLY])
            self.images.extend([Image.FABULOUS, Image.MEH, Image.YES])
        elif image_type == "prime":
            self.images.extend([2, 3, 5, 7])
        elif image_type == "polygon":
            self.images.extend([Image.TRIANGLE, Image.TRIANGLE_LEFT])
            self.images.extend([Image.CHESSBOARD, Image.DIAMOND])
        elif image_type == "animal":
            self.images.extend([Image.RABBIT, Image.COW, Image.PACMAN])
            self.images.extend([Image.DUCK, Image.BUTTERFLY, Image.GHOST])
            self.images.extend([Image.GIRAFFE, Image.SKULL, Image.SNAKE])
        else:
            pass
        
        print(self.images)
        
    def show(self):
        display.show(self.images[self.arrow])
        sleep(1000)
        self.arrow = self.arrow+1
        if self.arrow == len(self.images):
            self.arrow = 0
        
it = ImageStore("animal")
while True:
    it.show()
    