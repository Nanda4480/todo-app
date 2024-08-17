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
'''

'''
#continue statement in loop
count = 0
while count < 10:
    number = int(input("Enter a number: "))
    if number % 3 == 0:
        continue
    print(number)
    count += 1
'''

'''
#use pass statement
count = 0
while count < 10:
    number = int(input("Enter a number: "))
    if number % 3 == 0:
        pass
    else:
        print(number)
    count += 1
'''
'''
#for loop
number = int(input("Enter a number: "))
for count in range(1, 11):
    print(number, 'X', count,'=', number*count)
    '''
'''
#factorial
number = int(input("Enter a number: "))

fact = 1
for count in range(1, number+1):
    fact = fact * count
print(count, fact, end=' ')
'''
'''
#print n terms of AP series- arithmetic series

a = int(input("Enter start number: "))
d = int(input("Enter difference: "))
n = int(input("Enter number of terms: "))

for term in range(a, a+n*d, d):
    print(term)
'''
'''
#fibonacci series

n = int(input("Enter no of terms : "))
a = 0
b = 1
for item in range(n):
    print(a)
    c = a + b
    a = b
    b = c
'''
'''
#factors of a number
n = int(input("Enter no of terms : "))

for item in range(1, n+1):
    if n % item == 0:
        print(item)
'''

#check prime number
count = 0
n = int(input("Enter no of terms : "))
for item in range(1, n+1):
    if n % item == 0:
        count += 1
if count == 2:
    print('prime')
else:
    print('not prime')








