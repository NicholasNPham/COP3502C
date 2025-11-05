from dragon import *

class IceDragon(Dragon):
    def __init__(self, name, image):
        Dragon.__init__(self, name, image)

    def can_breath_fire(self):
        return False


