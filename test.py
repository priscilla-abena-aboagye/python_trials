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






