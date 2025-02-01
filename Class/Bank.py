class bank:
    def __init__(self,accountno,amount):
        self.accountno = accountno
        self.__amount = amount

    def withdraw(self,amount):
        if self.__amount - amount <= -1:
            print("Over draft")
        else:
            self.__amount = self.__amount - amount

    def getamount(self):
        return self.__amount

obj = bank("AB686868",1000)
print("Before widthdraw "+ str(obj.getamount()))
obj.withdraw(400)
print("Before widthdraw "+ str(obj.getamount()))
obj.withdraw(40000)
print("Before widthdraw "+ str(obj.getamount()))