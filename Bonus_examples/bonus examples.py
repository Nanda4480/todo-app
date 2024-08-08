
'''
filenames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt"]
print(filenames)
for filename in filenames:
    filename = filename.replace(".", "-", 1)
    print(filename)
'''


'''
DOB = int(input("enter birth year"))
age = 2024 - DOB
print(age)
'''

'''
ranking = ["John", "sen", "Lisa"]
new_rank = int(input("enter the new rank")) - 1
name = ranking[new_rank]
print(name)
'''

'''
ranking = ["John", "sen", "Lisa"]
name = input("enter the name")
rank = ranking.index(name) + 1
print(rank)
'''
'''
waiting_list = ["sen", "ben", "john"]
waiting_list.sort()
for index, item in enumerate(waiting_list):
    row = f"{index + 1}. {item.capitalize()}"
    print(row)
    print(index + 1, item)

for index, j in enumerate("abcd"):
    print(f"typing {j*5}")
    print(j)

filenames = ["dcument", "report", "presentation"]
for index, filenames in enumerate(filenames):
    print(f"{index}-{filenames.capitalize()}.txt")

ips = ['100.122.133.105', '100.122.133.111']
User_number = int(input("enter the index number"))
message = f"you chose {ips[User_number]}"
print(message)

temperature = [float(1.234), int(100), str("hello")]
print(type(temperature))
print(temperature)
'''

'''
menu = ["pasta", "pizza", "salad"]
my_choice = int(input("enter your choice"))
output = f"your choice{menu[my_choice]}"
for index, j in enumerate(menu):
    print(f"{index}-{j}")
print(output)


names = ["nanda", "usha", "udi", "rithika"]
#for index, names in enumerate(names):
   # print(index, names)
select_name = int(input("enter your choice"))
output = names[select_name]
print(output)

buttons = [('John', 'Sen', 'Morro'), ('Lin', 'Ajay', 'Filip')]
for first, second, third in buttons:
    print(first, second, third)
'''
'''
contents = ["all the vegeatables need to be sliced.",
            "the house needs to be cleand and swap properly.",
            "the kitchen to be built bigger and larger"]

filenames = ["data.txt", "reports.txt", "presentations.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"./files/{filename}", "w")
    file.write(content)

#with open('./files/data.txt', 'w') as file:
#    file.write('snail')
#    file.close()
'''
'''
newname = input("enter new name")
file = open('./files/data.txt', 'r')
oldmembers = file.readlines()
file.close()

oldmembers.append(newname + "\n")

file = open('./files/data.txt', 'w')
oldmembers = file.writelines(oldmembers)
file.close()
'''

'''
filenames = ["reports.txt", "presentations.txt"]
for filename in filenames:
    file = open(filename, 'w')
    file.write('hello')
    file.close()

filenames = ['a.txt', 'b.txt', 'c.txt']
for filename in filenames:
    file = open(f"./files/{filename}", 'r')
    content = file.read()
    print(content)
    
'''

'''
# list comprehension
filenames = ["1.doc", "1.report", "1.presentation"]
filename = [filename.replace(".", "-") + '.txt' for filename in filenames]
print(filename)

names = ["john smith", "jay santi", "eva kuki"]
name = [name.title() for name in names]
print(name)

usernames = ["john 1990", "alberta1970", "magnola2000"]
username = [len(username) for username in usernames]
print(username)

user_entries = ['10', '19.1', '20']
user_entry = [float(user_entry) for user_entry in user_entries]
print(user_entry)

user_entries = ['10', '19.1', '20']
user_entry = [float(user_entry) for user_entry in user_entries]
print(sum(user_entry))

temperatures = [10, 12, 14]
temperatures = [str(item) + '\n' for item in temperatures]
file = open("file.txt", 'w')
file.writelines(temperatures)

numbers = [10.1, 12.3, 14.7]
numbers = [int(item) for item in numbers]
print(numbers)

'''
'''
with open("../files/data.txt", 'r') as file:
    print(file.read())

'''
'''
date = input("enter today's date: ")
mood = input("rate your today's meed from 1 to 10")
thoughts = input("lets write your feeling:\n")

with open(f"./journal/{date}.txt", 'w') as file:
    file.write(mood + 2 * '\n')
    file.write(thoughts)
'''

'''
with open("../files/a.txt", 'r') as file:
    print(file.read())
    content = file.read()
    print(len(content))
'''

'''
# PW with list
password = input("enter new password")

result = []

if len(password) >= 8:
    result.append(True)
else:
    result.append(False)

digit = False
for i in password:
    if i.isdigit():
        digit = True

result.append(digit)

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True

result.append(uppercase)

print(result)

if all(result) is True:
    print("Strong password")
else:
    print("Weak password")

'''

'''
# PW with dictionary
password = input("enter new password")

result = {}

if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True

result["digit"] = digit

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True

result["upper-case"] = uppercase

print(result)
print(result.values())

if all(result.values()) is True:
    print("Strong password")
else:
    print("Weak password")

'''

'''
try:
    width = float(input("enter rectangle width: "))
    length = float(input("enter rectangle length: "))

    if width == length:
        exit('width and length are equal')

    area = width * length
    print(area)
except ValueError:
     print("Please enter a number")
'''

'''
#function with data in a file
def get_average():
    with open("files/data_temperature", 'r') as file:
        data = file.readlines()

    values = data[1:]
    values = [float(i) for i in values]

    average_local = sum(values) / len(values)
    return average_local


average = get_average()
print(average)

'''
'''
feet_inches = input("enter feet and inches: ")

def convert(feet_inches):
    split = feet_inches.split(" ")
    feet = float(split[0])
    inches = float(split[1])

    meters = feet * 0.3048 + inches * 0.0254
    return meters

result = convert(feet_inches)
if result < 1:
    print("kids cant use the ride")
else:
    print("kids is APPROVED")
'''

'''
from Bonus_examples.Bonus_function import split #function defined in "Bonus_function.py" file
from Bonus_examples.Bonus_function import convert

feet_inches = input("enter feet and inches: ")

splits = split(feet_inches)

result = (convert(splits['feet'], splits['inches']))

print(f"{splits['feet']} feet and {splits['inches']}inches are equal to {result} ")

if result < 1:
    print("kids cant use the ride")
else:
    print("kids is APPROVED")
'''

import json

with open("../files/question.json", 'r') as file:
    content = file.read()

data = json.loads(content)


for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index + 1,"-", alternative)
    user_choice = int(input("enter your answer: "))
    question["user_choice"] = user_choice

score = 0

for index, question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]:
        score = score + 1
        result = "correct Answer"
    else:
        result = "wrong Answer"

    message = f"{index+1} - {result}, your answer: {question['user_choice']},  correct answer: {question['correct_answer']}"
    print(message)

print(data)
print(score,'/',len(data))




























