a = input("how many apples do you have?")
try:
    a = int(a)
except:
    print("\33[41m[error]\33[0m" , a , "NAN")
    exit()
else:
    print("You have got " , a , " apples!" )
