class Person:
 def __init__(self,name,age):
  self.name = name
  self.age = age
 def greet(self):
  print(f"Hello {self.name} and age : {self.age}")

p = Person("Peru",50)
p.greet()

class Student:
  def __init__(self,id,name,classname):
    self.id = id
    self.name = name
    self.classname = classname

  def greet(self):
    print(f" Student ID : {self.id} , Name {self.name} and class is {self.classname}")

std1 = Student(1000,"Arun","Math")
std2 = Student(1001,"Victor","Science")

std1.greet()
std2.greet()

#without init
class Person:

 def greet(self):
  print(f"Hello {self.name} and age : {self.age}")

p = Person()
p.name = "Peru"
p.age = 30
p.greet()

#OOPS
#encapsulation
#private : .__ variable / function
#protected : ._variable name / Function
#public : .

class Account:
  def __init__(self,name,accountNo,balance=0):
   self.name = name
   self._accountNo = accountNo
   self.__balance = balance #private attribute

  def deposit(self,amount):
    if amount > 0 :
       self.__balance += amount

  def getBalance(self):
    return self.__balance

  def __private_getNewBalance(self):
    return self.__balance

  def _protected_getNewBalance(self):
    return self.__balance

acc = Account("Peru","ACC12345",10000)
acc.__balance=9000
print(acc.__balance)
print(acc.getBalance())
print(acc._accountNo)
acc._accountNo = "XD11111"
print(acc._accountNo)
print(acc.name + " Balance "+str(acc.getBalance()))
acc.deposit(300)
print(acc.name + " Balance "+str(acc.getBalance()))
print(acc._protected_getNewBalance())
#polymorphism
#inherutance
#abstraction

class ATM:

  def __init__(self,pin,phone,amount):
    self.__pin = pin
    self._phone = phone
    self.amount = amount

  def getBalance(self):
      return self.amount

  def _getPhone(self):
      return self._phone

  def __setPin(self,pin):
      self.__pin = pin

  def changePin(self,pin):
      self.__setPin(pin)

  def getPin(self):
      return self.__pin

atm = ATM("11111","9187849144",100)

print(atm.getBalance())
print(atm._getPhone())
atm._phone = "9800999922"
print(atm._getPhone())
atm.__pin = 322324
print(atm.__pin)
print(atm.getPin())
atm.changePin("444444444")

#inhertiance
class Device:

  def __init__(self,brand,model):
    self.brand = brand
    self.model = model

  def deviceInfo(self):
    return f"Brand is {self.brand} and Model is {self.model}"

class Laptop(Device):

  def __init__(self,brand,model,batteryLife):
    super().__init__(brand,model)
    self.batteryLife = batteryLife

  def laptopInfo(self):
    return f"{self.deviceInfo()} with Battery Life is {self.batteryLife} hours"

mylaptop = Laptop("Dell","Vostro",13)
print(mylaptop.laptopInfo())

class Animal:

  def __init__(self,type):
    self.type = type

  def typeInfo(self):
    return f"Type of animal is {self.type}"

class Dog(Animal):

  def __init__(self,type,breed,color):
    super().__init__(type)
    self.breed = breed
    self.color = color

  def dogInfo(self):
    return f"{self.typeInfo()} with breed {self.breed} and color is {self.color}"

myDog = Dog("Dog","German Shepherd","White")
print(myDog.dogInfo())

#####################################
#multi level (linear)
#####################################
class A:
  def methodA(self):
    print("Mothod A")

class B(A):
  def methodB(self):
    print("Mothod B")

class C(B):
  def methodC(self):
    print("Mothod C")

  def callAll(self):
    self.methodA()
    self.methodB()
    self.methodC()

mm = C()
mm.callAll()

#####################################
#multi level (Non Linear)
#####################################
class A:
  def methodA(self):
    print("Mothod A")

class B:
  def methodB(self):
    print("Mothod B")

class C(A,B):
  def methodC(self):
    print("Mothod C")

  def callAll(self):
    self.methodA()
    self.methodB()
    self.methodC()

mm = C()
mm.callAll()

#####################################
#polymorphism
#####################################

def add(a,b):
  return a + b

print(add(1,3))
print(add("SSS","DDD"))

class Tablet:
  def deviceType(self):
    return "Tablet with big screen."

class SmartPhone:
  def deviceType(self):
    return "SmartPhone with small screen."

def showdevice(device):
  print(device.deviceType())

myTablet = Tablet()
showdevice(myTablet)

mySmartPhone = SmartPhone()
showdevice(mySmartPhone)

class Device:
  def powerOn(self):
    return "Device power on"

class Laptop(Device):
  def powerOn(self):
    return "Laptop power on"


mdev = Laptop()
mdev.powerOn()

class Device1:
  def power_on(self):
    return "Device is powering on"

class Laptop1(Device1):
  def power_on(self):
    return "Laptop is started now"


device1 = Device1()
laptop1 = Laptop1()

print(device1.power_on())
print(laptop1.power_on())
print(Laptop1.power_on(device1))

#####################################
#overloading
#####################################
class Vector:
  def __init__(self,x,y):
    self.x = x
    self.y = y

  def __add__(self,other):
    return Vector(self.x+other.x,self.y + other.y)

  def __str__(self):
    return f"Vector({self.x},{self.y})"

v1 = Vector(2,3)
v2 = Vector(5,6)

print(v1+v2)







