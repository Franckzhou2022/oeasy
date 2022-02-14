#!/usr/bin/python3
a = input("how many apples do you have?")
try:
    a = int(a)
except:
    print("\33[41m[error]\33[0m" , a , "NAN")
else:
    print("You have got " , a , " apples!" )

b = input("how many banana  do you have?")
try:
    b = int(b)
except:
    print("\33[41m[error]\33[0m" , b,"NAN")
else:
    print("You have got " , b , " bananas!" )
