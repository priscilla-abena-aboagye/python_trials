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
phone_number = input("Enter your phone number: ")
result = len(name)
null = name.find("b")
last = name.rfind("c")
name = name.capitalize()
upper = name.upper()
lower = name.lower()
number = name.isdigit()
master = name.isalpha()
phone = phone_number.count("-")
space = phone_number.replace("-", " ")

print(result)
print(null)
print(last)
print(name)
print(upper)
print(lower)
print(number)
print(phone)
print(space)



username = input("Enter a username: ")

if len(username) > 12:
    print("Your username can not be more than 12 characters")
elif not username.find(" ") == -1:
    print("Your username can not contain spaces")
elif not username.isalpha():
    print("Your username should not contain numbers")
else:
    print(f"Welcome {username}")


credit_number = "1234-2342-3564-5667-3444"
last_digit = credit_number[-4:]
print(credit_number[2])
print(credit_number[0:4])
print(credit_number[:4])
print(credit_number[5:9])
print(credit_number[5:])
print(credit_number[-1])
print(credit_number[::3])
print(credit_number[::-1])
print(last_digit)



price1 = 30200202.14159
price2 = -967.44
price3 = 12.455
print(f"Price 1 is ${price1:+,.2f}")
print(f"Price 2 is ${price2:+}")
print(f"Price 3 is ${price3:.2f}")

myName = input("Enter your name: ")


while myName == "":
    print("You did not enter your name")
    myName = input("Enter your name: ")
print(f"Hello {myName}")

myAge = input("Enter your age: ")


while myAge == "":
    print("You did not enter your age")
    myAge = int(input("Enter your age: "))
print(f"You are {myAge} yrs old")

food = input("Enter a food you like (press q to quit): ")

while not food == "q":
    print(f"You like {food}")
    food = input("Enter a another food you like (press q to quit): ")

print("Bye")


number1 = int(input("Enter a number between 1 - 10: "))

while number1 < 1 or number1 > 10:
    print(f"{number1} is not valid")
    number1 = int(input("Enter a number between 1 - 10: "))

print(f"Your number is {number1}")

principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle: "))
    if principle < 0:
        print("Principle cannot be less than zero")
    else:
        break


while True:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("Rate cannot be less than zero")
    else:
        break

while True:
    time = int(input("Enter the interest time: "))
    if time < 0:
        print("time cannot be less than zero")
    else:
        break


interest = principle * (1 + (rate / 100)) ** time
print(f"Balance after {time} year/s: ${interest:,.2f}")

for x in range(1,21):
    if x == 13:
        continue
    else:
        print(x)

import time
my_time = int(input("Enter the time in seconds: "))

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")

    time.sleep(1)


print("TIME'S UP")



for x in range(3):
    for y in range(1, 10):
        print(y, end=" ")
    print()

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter the symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(y, end=" ")
    print()

fruits = ["apple", "mango", "banana", "orange"]


fruits[0] = "pineapple"
fruits.append("cherry")
fruits.insert(1, "grapes")
fruits.sort()
fruits.reverse()
print(fruits)








