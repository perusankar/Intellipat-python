
class Person:
    def __init__(self,name):
        self.name = name

    def say_hello(self):
        print("Hello " + self.name)

obj = Person("Peru")
obj.say_hello()
