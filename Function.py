'''
def greet():
    message = "hello- world!"
    new_meaasage = message.capitalize()
    return new_meaasage


greeting = greet()
print(greeting)

def greet(message):
    new_meaasage = message.capitalize()
    return new_meaasage

user_input = input("enter your message")
greeting = greet(user_input)
print(greeting)

user_input2 = input("enter your DOB")
dob = greet(user_input2)
print(dob)
'''

'''
def average(numbers):
        if not numbers:
            return 0
        return sum(numbers) / len(numbers)


numbers = [1,2,3,4,5]
print(average(numbers))


name = input("enter your name")
def greet(name):
    return name.capitalize()

print(f"hi {greet(name)}")
'''

'''
string1 = "hi"
string2 = "hello"

def convert(string1, string2):
    text = string1 + string2
    return text

print(convert(string1, string2))

def speed(distance, time):
    return distance / time

print(speed(120, 60))

'''
'''
# import files using glob fultion
import glob
myfiles = glob.glob("files/*.txt")

for data in myfiles:
    with open (data, 'r') as file:
      print(file.read())
'''

'''
#import csv files
import csv
with open ("files/weather.csv", 'r') as file:
    data = list(csv.reader(file))

city = input("enter your city: ")
print(data)
for row in data[1:]:
    if row[0] == city:
        print(row[1])
'''
'''
import shutil
shutil.make_archive("all", "zip", "files")
'''

'''
# search in google
import webbrowser
user_input = input("Enter search term: ").replace(" ", "+")
webbrowser.open("https://www.google.com/search?q=" + user_input)
'''

def doller_add(money):
    return '$' + str(money)

money = 15
print(doller_add(money))











