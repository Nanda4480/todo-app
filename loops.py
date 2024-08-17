'''
count = 0
while count < 7:
    print(count, "thankyou baba")
    count += 1
'''

'''
number = 1235678

while number > 0:
    reminder = number % 10
    number = number // 10
    print(reminder)
'''
'''
#multiplecation table
n = int(input("Enter a number: "))
counter = 1
while counter <= 10:
    product = n * counter
    print(n, 'x' ,counter, '=' ,product)
    counter += 1
'''
'''
#no of digits in a number
number = int(input("Enter a number: "))
counter = 0
while number > 0:
    number = number//10
    counter += 1
print('no of digits', counter)
'''

'''
#sum of the digits in a number
number = int(input("Enter a number: "))
sum = 0
while number > 0:
    reminder = number % 10
    number = number // 10
    sum += reminder
print('sum of dights: ',sum)
'''
'''
#reverse the number
number = int(input("Enter a number: "))
rev = 0
while number > 0:
    reminder = number % 10
    number = number // 10
    rev = rev * 10 + reminder
print(rev)
'''
''''
#check if number is Palindrome
number = int(input("Enter a number: "))
new_number = number
rev = 0
while number > 0:
    reminder = number % 10
    number = number // 10
    rev = rev * 10 + reminder
if new_number == rev:
    print("palindrome")
else:
    print("not palindrome")
'''
'''
#find sum of given numbers
number_of_no= int(input("Enter number of numbers: "))

sum = 0
count = 0
while count < number_of_no:
    number = int(input("Enter a number: "))
    sum += number
    count += 1
print(sum)
'''
'''
#sum of positive & negative numbers
number_of_number = int(input("Enter number of number: "))
Psum = 0
Nsum = 0
count = 0

while count < number_of_number:
    number = int(input("Enter a number: "))
    if number > 0:
        Psum = Psum + number
    else:
        Nsum = Nsum + number
    count += 1
print(Psum)
print(Nsum)
'''
'''
#find maximum number - incorrect code
number_of_numbers = int(input("Enter number of numbers: "))
max = 0
count = 0
while count < number_of_numbers:
    number = int(input("Enter a number: "))
    if number > max:
        max = number
    count += 1

print(max)
'''
'''
#find maximum number - correct coding
number_of_numbers = int(input("Enter number of numbers: "))
count = 0
max = int(input("Enter a number: "))
while count < number_of_numbers:
    number = int(input("Enter a numbers: "))
    if number > max:
        max = number
    count += 1
    
print(max)
'''
'''
#convert decimal to binary

number = int(input("Enter a number: "))

bin = ''
while number > 0:
    reminder = number % 2
    number = number // 2
    bin = str(reminder) + bin
print(bin)
'''
#guess a number between 1 -10
import random
number = random.randint(1, 10)

guess = 0
while guess != number:
    guess = int(input("Guess a number: "))
    if guess < number:
        print("Too low")
    elif guess > number:
        print("Too high")
    else:
        print("Guess right")
print(number)


