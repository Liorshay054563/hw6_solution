#start

sum_temp: float = 0
for i in  range (5):
    city_temp: float = float(input('Enter temp:'))
    while not -50 < city_temp < 45:
        city_temp: float = float(input('Valid temp, Enter temp:'))
    else:
        print("temp is correct")
    sum_temp += city_temp
print(f"the avg is {sum_temp / 5}")

#end