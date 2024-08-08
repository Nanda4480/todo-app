'''
password = input("Enter your password: ")

result = False
if len(password) > 7:
    result = True
    print("Great password there!")

else:
    print("your password is weak")
'''
from unittest import result

'''
password = input("Enter your password: ")

if len(password) > 7:
    print("Great password there!")
elif len(password) ==7:
    print("Your password is OK")
else:
    print("Your password weak")
'''

'''
day_temperatures = ('morning : 10.5', 'noon : 22.5', 'evening : 12.5')

ids = ["XF345_89", "XER_7_6849", "XA454_55"]

x = 0

for id in ids:
    if '_' in id:
        x = x + 1
print(x)

'''
'''
try:
    total_value = float(input("Enter total value: "))
    value = float(input("Enter value: "))

    Percentage = value/total_value*100
    print(f"the result {Percentage}%")
except ValueError:
    print("Please enter a number")
except ZeroDivisionError:
    print("your total value cant be zero")
'''

'''
colors = [11, 34, 98, 43, 45, 54, 54]

for color in colors:
    if color > 50:
        print(color)
'''

'''
try:
    waiting_list = ["john", "marry"]
    name = input("Enter name: ")

    number = waiting_list.index(name)
    print(f"{name}'s turn is {number}")
except ValueError:
    print(f"{name} is not in the list")
'''

def get_max():
    grades = [9.6, 9.2, 9.7]
    max_grade = max(grades)
    min_grade = min(grades)
    message = F"max:{max_grade} & min: {min_grade}"
    return message


print(get_max())

'''
liters = float(input("Enter liters: "))


def liters_to_m3(liters):
    m3 = liters / 1000
    return m3

print(f"liters {liters_to_m3(liters)}")

'''

'''
#function to determine password
password = input("Enter your password: ")
def strength(password):

    result = {}

    if len(password) >= 8:
        result["length"] = True
    else:
        result["length"] = False

    digit = False
    uppercase = False
    for item in password:
        if item.isdigit():
            digit = True

        if item.isupper():
            uppercase = True
        result["digit"] = digit
        result["upper-case"] = uppercase

    if all(result.values()):
        return "strong password"
    else:
        return "weak password"


print(strength(password))
'''

'''
year_birth = int(input("enter year of birth"))

def get_age(year_birth, current_year=2024):
    age = current_year - year_birth
    return age

current_age = get_age(year_birth, current_year=2024)

print(f"{current_age} years old")
'''

'''
item_list = input("enter items: ")

def get_nr_items(item_list):
    items = item_list.split(',')
    return len(items)

new_list = get_nr_items(item_list)
print(new_list)

'''

'''
side = int(input("enter side: "))

def area_square(side):
    area = side * side
    return area

area = area_square(side)
print(area)

'''

'''
temp = float(input("enter temp: "))

def weather(temp):
    if temp > 7:
        return "warm"
    elif temp <= 7:
        return "cold"

print(weather(temp))
'''
'''
word = input("enter length: ")


def string(word):
    if len(word) >= 8:
        return "True"
    else:
        return "False"

print(string(word))
'''

'''
def calculate_time(h, g=9.80665):
    t = (2 * h / g) ** 0.5
    return t


time = calculate_time(100)
print(time)
'''
'''
temp = int(input("enter temp: "))

def water_state(temp):
    if temp <= 0:
        return "Solid"
    elif temp <= 99:
        return "liquid"
    else:
        return "Gas"

print(water_state(temp))
'''

'''
temperature = int(input("enter temp: "))

def water_state(temperature):
    FREEZING_POINT = 0
    BOILING_POINT = 100

    if temperature <= FREEZING_POINT:
        return "solid"

    elif FREEZING_POINT < temperature < BOILING_POINT:
        return "liquid"

    else:
        return "gas"

print(water_state(temperature))

'''
'''
temp = int(input("enter temp: "))
def water_state(temp):
   if temp < 15:
       return "Cold"
   elif temp <= 25:
       return "Warm"
   else:
       return "Hot"
print(water_state(temp))
'''
'''
import time
print(time.strftime("%A"))

import random

# Get two numbers from the user and covert them to integers
lower_bound = int(input("Enter the lower bound: "))
upper_bound = int(input("Enter the upper bound: "))

# Pick a random int using randint()
rand = random.randint(lower_bound, upper_bound)

print(rand)

'''

'''
from function_coding_exercise import parse
import random

# Ask the user to enter a lower and an upper bound divided by a comma
user_input = input("Enter a lower bound and an uppwer bound divided a comma (e.g., 2,10)")

# Parse the user string by calling the parse function
parsed = parse(user_input)

# Pick a random int between the two numbers
rand = random.randint(parsed['lower_bound'], parsed['upper_bound'])

print(rand)
'''

def sp_number(user_input):
    user_input = user_input.split(",")
    lower = int(user_input[0])
    upper = int(user_input[1])
    return lower, upper

import random
user_input = input("Enter a lower and an upper bound divided by a comma or space: ")
spl_number = sp_number(user_input)
rand = random.randint(spl_number[0], spl_number[1])
print(rand)





