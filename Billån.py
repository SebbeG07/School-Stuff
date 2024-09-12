import math 

tal1=int(input ("Ange x år: "))
Maybe = 265000 * (0.85 ** tal1)
print(Maybe) 

tal2=int(input ("Ange x år: "))
test1=float(input ("Ange ett startvärde: "))
Maybe2 = test1 * (0.85 ** tal2)
print(Maybe2)

tal3=int(input ("Ange x år: "))
test2=float(input ("Ange ett startvärde: "))
yes1=float(input ("Ange en procent takt: "))
yes1=((100-yes1)/100)
Maybe3 = test2 * (yes1 ** tal3)
print(Maybe3)