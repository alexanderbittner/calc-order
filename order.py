#!/usr/bin/python3
import sys
if(len(sys.argv)<3):
    print("USAGE: order.py [ORDER-CANDIDATE] [GROUP]")
    exit(1)
order = int(sys.argv[1])
group = int(sys.argv[2])
print("trying to compute order of " + str(order) + " in group " + str(group))
exp = 1
while((order**exp)%group!=1):
    print(str(order) + "^" + str(exp) + " mod " + str(group) + " = " +  str((order**exp)%group))
    exp = exp+1
print(str(order) + "^" + str(exp) + " mod " + str(group) + " = " +  str((order**exp)%group))
print(exp)