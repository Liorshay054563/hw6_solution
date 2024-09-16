# start


x: int = int(input('Enter a number that divisible with 7:'))
counter = 0

while True:
    if x % 7 == 0 or x % 11 != 0 : #
        print('Correct! continue:')
    x: int = int(input('Enter a number that divisible with 7:'))
    counter += 1
    if x % 7 != 0 :                                         #לא הצלחתי לעשות  else היה ךי באדום
        print(f"wrong, but you success {counter} times")
    if x % 11 == 0:
        break


