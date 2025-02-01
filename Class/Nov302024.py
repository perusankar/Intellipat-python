class Dog:
  def __init__(self,breed,age):
    self.breed = breed
    self.age = age

  def concat(self):
      print(self.breed+ " - " + str(self.age))

  def display(self):
    print(self.breed,str(self.age))

dog_data = [("labra",12),("bulldog",13),("german sphered",13)]

for breed , age in dog_data:
    print(breed)

dogs = [Dog(breed,age) for breed , age in dog_data]

for dog in dogs:
  dog.concat()

class parent:
    def show(self):
        print("Parent")

class child(parent):
    def show(self):
        print("Child")

obj = child()
obj.show()

from abc import ABC , abstractmethod

class Sample(ABC):
    @abstractmethod
    def display(self):
        pass

class Child(Sample):
    def display(self):
        print("Child")

obj = Child()
obj.display()