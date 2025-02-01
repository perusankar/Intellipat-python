from operator import length_hint


class rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def calculateArea(self):
        return self.length * self.width

obj = rectangle(10,20)
print(obj.calculateArea())

