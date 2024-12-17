temp = -5
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still on")



temp = 25
is_sunny = False

if temp >= 28 and is_sunny:
    print("It is HOT outside")
    print("It is sunny")
elif temp <= 0 and is_sunny:
    print("It is COLD outside")
elif 28 > temp > 0 and is_sunny:
    print("It is WARM outside")
elif temp >= 28 and  not is_sunny:
    print("It is CLOUDY outside")
elif temp <= 0 and not is_sunny:
    print("It is CLOUDY outside")
elif 28 > temp > 0 and not is_sunny:
    print("It is CLOUDY outside")
else:
    print("There is no weather forecast")


num = 5
a = 6
b = 7
age = 12

print("Positive" if num > 0 else print("Negative"))
result = "EVEN" if num % 2 == 0 else "ODD"
status = "Adult" if age >= 18 else "Child"
max_num = a if a > b else b
min_num = a if a < b else b
print(max_num, min_num)
print(status)

name = input("Enter your full name: ")
result = len(name)
null = name.find("b")
last = name.rfind("c")
name = name.capitalize()

print(result)
print(null)
print(last)
print(name)
