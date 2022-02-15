#!/usr/bin/python3
import get_fruits
try:
    total = get_fruits.a + get_fruits.b
except:
    print("\33[41m[Error]\33[0m can not add a,b")
