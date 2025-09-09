temp = int(input("Enter the temperature in Celsius: "))
condition = input("Enter the condition: ")

if condition == "sunny":
    if temp > 25:
        print("Great day for beach")
    elif 15 <= temp <= 25:
        print("picnic")
    else:
        print("walk")
elif condition == "rainy":
    if temp > 20:
        print("rain walk")
    else:
        print("stay inside")
else:
    print("snow main")