#start 3.1


num : int = int(input("Enter a positive number "))

for i in range (9):
    for j in range (1, num+1):
        print(i, end="")
    print()

#end


#start 3.2

num : int = int(input("Enter a number:"))

for i in range (num):
    for j in range (num-i):
        print(" ", end ="")
    for _ in range (2*i+1):
        print("*", end= "")
    print()

#end     it's very difficult

