#gpa = float(input("what is applicant gpa?"))
#inst_app = input("is the applicant institute is appoved?")

#if gpa >= 3.7:
#    if inst_app == "yes"":
 ##      print("the applicant qualify for loan")
   # else:
    #    print("institute not approved hence NO loan")
#else:
 #   print("the GAP is less so NO loan")

'''
marks = int(input("enter the student mark"))

if marks >= 90:
     print("the mark" + str(marks) + "grade A")
else:
     if marks >= 80:
         print("the mark" + str(marks) + "grade B")
     else:
         if marks >= 70:
             print("the mark" + str(marks) + "the student is passed")
         else:
             print("the student failed")
'''

'''
from random import randint
one2ten = randint(1, 10)

if one2ten == 1:
    print("roman symbol = to " + str(one2ten) + " is I")
elif one2ten == 2:
    print("roman symbol = to " + str(one2ten) + " is II")
elif one2ten == 3:
    print("roman symbol = to " + str(one2ten) + " is III")
elif one2ten == 4:
    print("roman symbol = to " + str(one2ten) + " is IV")
elif one2ten == 5:
    print("roman symbol = to " + str(one2ten) + " is V")
elif one2ten == 6:
    print("roman symbol = to " + str(one2ten) + " is VI")
elif one2ten == 7:
    print("roman symbol = to " + str(one2ten) + " is VII")
elif one2ten == 8:
    print("roman symbol = to " + str(one2ten) + " is VIII")
elif one2ten == 9:
    print("roman symbol = to " + str(one2ten) + " is IX")
else:
    print("roman symbol = to " + str(one2ten) + " is X")
'''

#while loop
'''
counter = 10

while counter != 0:
    print(counter)
    counter -= 1
    '''
'''
#sum of numbers of positive integers
pos_int = int(input("Enter a positive integer: "))
initial_int = pos_int
added = 0
while pos_int > 0:
    added += pos_int
    pos_int -= 1

print(initial_int)
print(added)

'''
#for loop
'''
word = "hello all"
for letter in word:
    print(letter)
'''

'''
user_str = input("please enter the word")
count = 0
for char in user_str:
    count += 1
print(user_str)
print(count)
'''
'''#range
one_input = range(7)
for number in one_input:
    print(number)
'''
'''
for number in range(1, 51):
    if number % 3 == 0 and number % 5 == 0:
        print("number divisibler by 3&5")
    elif number % 3 == 0:
        print("number divisibel by 3")
    elif number % 5 == 0:
        print("number divisible by 5")

    else:
        print(number)
'''
'''
#print("thINK".islower())
print("-".join(["one", "two", "three", "four", "five"]))
print("eggs,milk,butter".split(", "))

mixed_case = "I am learning coding"
print(mixed_case.isupper())
print(mixed_case.upper())
print(mixed_case.lower())
print(mixed_case.istitle())
print("I Am Good".istitle())
print(mixed_case.startswith("I"))
print(mixed_case.endswith("I"))
print(mixed_case.split())
print(mixed_case.rjust(50))
print(mixed_case.ljust(50) + "how much space")
print(mixed_case.rjust(25, "#"))
print(mixed_case.ljust(30, "$") + "how much space")
print(mixed_case.center(30, "%"))

print("Good boy".replace("Good", "Bad"))

three_input = range(20, 1, -3)
for number in three_input:
    print(number)

'''
'''
user_string = input("please enter a string")
reversed = ""
for item in range(len(user_string) - 1, -1, -2):
    reversed += user_string[item]

print(reversed)
print(len(user_string))
'''
'''
str_1 = "james Bond is 007"
str_2 = "When the moon hits your eye like a big pizza pie, that's amore!"
str_3 = "Anyway, like I was sayin', shrimp is the fruit of the sea. You can barbecue it, boil it, broil it, bake it, \
saute it. Dey's uh, shrimp-kabobs, shrimp creole, shrimp gumbo. Pan fried, deep fried, stir-fried. There's pineapple \
shrimp, lemon shrimp, coconut shrimp, pepper shrimp, shrimp soup, shrimp stew, shrimp salad, shrimp and potatoes, \
shrimp burger, shrimp sandwich. That- that's about it."

def word_counter(words):
    spaces_and_letters = ""
    word_count = 1
    for i in words:
        if i.isalnum() or i.isspace() or i == "-" or i == "'":
            spaces_and_letters += i
    for j in spaces_and_letters:
        if j == " ":
            word_count += 1
    return word_count

print(word_counter(str_1))
print(word_counter(str_2))
print(word_counter(str_3))
'''
'''
string_1 = "I am Nanda and i have a family"
def word_counter(words):
    spaces = ""
    word_count = 1
    for item in words:
        if item.isspace():
            #spaces += item
            word_count += 1
    return word_count
print(word_counter(string_1))

string_2 = input("please enter a string")
def word_counter(word):
    special = "-"
    word_count = 0
    for item in word:
        if item == "-":
            word_count += 1
    return word_count
print(word_counter(string_2))

'''
'''
#format
name = input("please enter your name")
age = input("please enter your age")
place = input("please enter your place")

print("{} is the name{},  and lived in {}".format(name, age, place))
'''

''''
import FreeSimpleGUI as sg

# Prepare the widgets for the left column
left_column_content = [[sg.Text('Left 1')],
                       [sg.Text('Left 2')]]

# Prepare the widgets for the right column
right_column_content = [[sg.Text('Right 1')],
                        [sg.Text('Right 2')]]

# Construct the Column widgets
left_column = sg.Column(left_column_content)
right_column = sg.Column(right_column_content)

# Construct the layout
layout = [[left_column, right_column]]

# Construct and display the window
window = sg.Window('Columns', layout)
window.read()
window.close()

'''
'''
while True:
    password = input("Enter password")

    while password != "pass1":
        password = input("enter password: ")

print("pw is correct")

'''
'''
usernames = ["nanda", "usha", "udi"]
for usernames in usernames:
    print(usernames)
'''

'''
number1 = int(input("please enter your first number"))
number2 = int(input("please enter your second number"))

if number1 - number2 >0:
    print(number1-number2)
else:
    print(number2-number1)
'''

'''
number= int(input("please enter your number"))
if number % 2 == 0:
    print("even")
else:
    print("odd")
'''

'''
age = int(input("please enter your age"))
if age > 18:
    print("eligible for vote")
else:
    print("not eligible for vote")
'''

'''
marks = int(input("please enter your marks"))
if marks >= 0 and marks <= 100:
    print("valid marks")
else:
    print("invalid marks")
'''

'''
gender = input("please enter your gender")
if gender == "m" or gender == "M":
    print("male")
elif gender == "f" or gender == "F":
    print("female")
else:
    print("invalid gender")
'''

'''
age = int(input("please enter your age"))
if age >=18 and age <=60:
    print("eligible age")
else:
    print("not eligible age")
'''

'''
math = int(input("please enter your math"))
physics = int(input("please enter your physics"))
chemistry = int(input("please enter your chemistry"))

if math >= 45 and physics >= 45 and chemistry >= 45:
    print("pass")
else:
    print("fail")
    '''
'''
user = input("please enter your name")
if user == "john" or user == "smith":
    print("admin")
else:
    print("not admin")
'''
'''
letter = input("please enter your letter")
if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
    print("vowel")
else:
    print("not vowel")
    '''

'''
john = float(input("please enter john age"))
smith = float(input("please enter smith age"))
ajay = float(input("please enter ajay age"))

if john > smith and john > ajay:
    print("john is eldest")
elif smith > john and smith > ajay:
    print("smith is elder")
else:
    print("ajay elder")
    '''

'''
bill_amount = float(input("please enter bill amount: "))
if bill_amount <= 1000:
    bill_amount = bill_amount * 0.9
elif bill_amount < 1000 and bill_amount <= 5000:
    bill_amount = bill_amount * 0.8
elif bill_amount < 5000 and bill_amount <= 10000:
    bill_amount = bill_amount * 0.7
else:
    bill_amount = bill_amount * 0.5
print(bill_amount)
'''

'''
year = int(input("please enter year"))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("leap year")
else:
    print("not leap year")
    '''

