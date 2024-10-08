import random

randomtal = random.randint(1, 100)
max_tries = 7
tries = 0

print("Gissa rätt tal mellan 0-100")

while tries < max_tries:
   
    guess = int(input(f"Försök {tries + 1}: Gissa ett tal: "))

    if guess > randomtal:
        print("För högt")
    elif guess < randomtal:
        print("För lågt")
    else:
        print("Bra jobbat! Du gissade rätt!")
        break  
   
    tries += 1

if tries == max_tries and guess != randomtal:
    print(f"Tyvärr, du har gissat fel 7 gånger. Det rätta talet var {randomtal}.")