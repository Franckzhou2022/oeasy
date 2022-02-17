#!/usr/bin/python3
'''
input number of apples.
'''
s_apple = input("how many apples do you have?")
try:
    i_apple = int(s_apple) # change a from string to intiger
except:
    print("\33[41m[error]\33[0m" , s_apple , "NAN")
else:
    print("You have got " , i_apple , " apples!" )
'''
input number of bananas.
'''
s_banana = input("how many banana  do you have?")
try:
    i_banana = int(s_banana) #change b from string to intiger.
except:
    print("\33[41m[error]\33[0m" , s_banana ,"NAN")
else:
    print("You have got " , i_banana, " bananas!" )
