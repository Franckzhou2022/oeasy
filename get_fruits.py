#!/usr/bin/python3
'''
input number of apples.
'''
a = input("how many apples do you have?")
try:
    a = int(a) # change a from string to intiger
except:
    print("\33[41m[error]\33[0m" , a , "NAN")
else:
    print("You have got " , a , " apples!" )
'''
input number of bananas.
'''
b = input("how many banana  do you have?")
try:
    b = int(b) #change b from string to intiger.
except:
    print("\33[41m[error]\33[0m" , b,"NAN")
else:
    print("You have got " , b , " bananas!" )
