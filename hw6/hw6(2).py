import random


lucky1: int = random.randint(1, 100)
print(lucky1)
x = int(input("Try to guess a number"))
counter: int = 0
while x != lucky1:
    if x > lucky1:
        x = int(input('your number is too big, try again:'))
        counter +=1

    else:

        x = int(input('your number is too low , try again:'))
if x == lucky1:
    print(f"BINGO !! after {counter+1} times.")

