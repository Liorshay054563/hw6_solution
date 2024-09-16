import random

name1: str = input('enter name:')
name2: str = input('enter another name:')
name3: str = input('enter another name:')
name4: str = input('enter another name:')

lucky1= random.choice([name1, name2, name3, name4])

print(f"{lucky1} Win!!!")




