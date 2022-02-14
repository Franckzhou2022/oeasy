b = input("how many banana  do you have?")
try:
    b = int(b)
except:
    print("\33[41m[error]\33[0m" , b,"NAN")
    exit()
else:
    print("You have got " , b , " bananas!" )
