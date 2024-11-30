l = "shahrukh"

print(l[-5:-2])

list1 = [1,2,3,4,5]

print(list1[-4:])

mylist = ["Tea","Milk","Juice"]

mylist.append("TESRT")

#print(mylist)

mylist2 = ["FRTY","XXXXX","ZZZZZ"]

#mylist.extend(mylist2)


print(mylist2.pop(2))

tt = (1,2,3,4,5)
tta = (1,2,3,4,5)

print((tta+tt).count(2))
print((tta+tt).index(5))
print(tta+tt)

set7 = {33,55}
list1 = list(set7)
list1.append(789)
print(list1)
set7 = set(list1)
print(set(list1))
set8 = {33,99}
print(set7)
print(set7.union(set8))
print(set7.intersection(set8))

print(round(6.6))
f = False
f1 = False
if f == f1:
    print("DDD")
else:
    print("FFFF")

i =5
while i >= 0:
    print(i)
    i -=1

def gg():
    print("DDD")

gg()