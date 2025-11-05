from cow import *

class Dragon(Cow):
    def __init__(self, name, image):
        super(Dragon, self).__init__(name)
        self.image = image

    def can_breath_fire(self):
        return True


