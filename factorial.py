# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 20:13:39 2016

@author: jmago
"""

# -*- coding: utf-8 -*-


# AUTHOR Chenxi Zhang(Alex) alexzcx@bu.edu


"""
    Write a python program that does the following:
    
    reads two integers X and Y using input()
    calculates Z = X! - Y!
    Your program should print out Z, the number of decimal digits of Z, and the number of bytes that are required to store this number
    
    You may use math.factorial() to check your answer but you must calculate the factorial yourself.
    
    Here is an example output when X=11 and Y=7
    
    39911760
    8
    4
    This means that Z = 11!-7! = 39911760, which clearly has 8 decimal digits, and it requires 4 bytes of storage.
"""

"""
Created on Mon Sep 12 22:34:43 2016

@author: alex
"""
import math

X = int(input())
Y = int(input())
# X factorial function
Xlist = list(range(1,X+1,1))
Xfact = 1

for i in Xlist:
    Xfact = Xfact*i
    
print("Xlist =", Xlist)
print("Xfact =", Xfact)

# Y factorial function
Ylist = list(range(1,Y+1,1))
Yfact = 1

for j in Ylist:
    Yfact = Yfact*j

print("Ylist =", Ylist)
print("Yfact =", Yfact)

# the final process
Z = Xfact - Yfact
print("Z =",Xfact,"-",Yfact,"=",Z)
print("length of Z =",len(str(Z)))
print("Byte of Storage =",math.ceil(len(bin(Z))/8))

# Test

Z = math.factorial(X) - math.factorial(Y)
print("*test*","Z =",math.factorial(X),"-",math.factorial(Y),"=",Z,"*test*")


# A factorial function
Alist = list(range(1,A+1,1))
Afact = 1

for k in Alist:
    Afact = Afact*k

print("Alist =", Alist)
print("Afact =", Afact)

# B factorial function
Blist = list(range(1,B+1,1))
Bfact = 1

for l in Blist:
    Bfact = Bfact*k

print("Blist =", Blist)
print("Bfact =", Bfact)

# the final process A + B
C = Afact + Bfact
print("C =",Afact,"+",Bfact,"=",C)
print("length of C =",len(str(C)))
print("Byte of Storage =",math.ceil(len(bin(C))/8))

# Test

C = math.factorial(A) + math.factorial(B)
print("*test*","C =",math.factorial(A),"+",math.factorial(B),"=",C,"*test*")