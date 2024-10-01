import random 

Throws=int (input ("Hur många tärningar vill du kasta?: "))
addict=0
vdo=1
while vdo <= Throws:
    dice=random.randrange(6)+1
    #print(dice)
    addict += dice
    vdo+=1
random.randrange(7)

i = 1
while i <= Throws:
  print (random.randrange(6)+1)
  i+=1

print(addict)
print(addict/Throws)