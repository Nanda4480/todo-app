'''
s1 = 'hello world'
for x in s1:
    print(x)

for i in range(0, len(s1)):
    print(s1[i])

for i in range(len(s1)-1,-1,-1):
    print(s1[i])
'''

'''
s1 = 'bghiamporcd'
ss = sorted(s1)
print(ss)
'''

'''
food = input("enter your favorite food ")
price = input("enter your favorite price ")

print(len(food)+len(price))
dash = '-' * (30-len(food)+len(price))
print(food+dash+price)
'''
#check the pw are correct
'''
passkey = "secret"
password = input("enter your password ")
if password == passkey:
    print('password is ok')
else:
    print('password is wrong')
'''
'''
#check the pw case match
pass1 = input("enter your favorite password ")
pass2 = input("confirm password ")
if pass1 == pass2:
    print('password is ok')
else:
    if pass1.casefold() == pass2.casefold():
        print('check the lette cases')
    else:
        print('wrong passkey, try again')
'''
'''
#display credit card number with ****
card_no = input("enter your favorite card number ")

display_no = card_no[15::]

star = '*' * 4 + ' '
print(star + star + star + display_no)
'''

'''
#find user id and domain name from the email address
email = input("enter your favorite email: ")
atrate = email.find('@') #this find method will show the index of @
print('user id:', email[0:atrate])
print('domain id:', email[atrate+1:])
'''
'''
#check a strig is palindrome
string1 = input("enter your favorite string ")
rev = string1[::-1]
print(rev)
if string1 == rev:
    print('string is palindrome')
else:
    print('string is not palindrome')

'''
'''
#convert the string into palindrome
string1 = input("enter your favorite string ")
rev = string1[::-1]
print(rev)
print(string1+rev)
'''
'''
#find day month and year from a date
date = input("Enter the date fowwing format dd/mm/yyyy")
date_split=date.split('/')
print(date_split)
day = date_split[0]
month = date_split[1]
year = date_split[2]
print('day: ',day,'month:', month,'year:', year)
'''
'''
#check two strings are anagram

s1 = input("enter string1 ")
s2 = input("enter string2 ")

if len(s1) != len(s2):
    print('not anagram')
else:

    for letter in s1:
        if letter not in s2:
            print('not anagram')
            break
    else:
        print('anagram')
'''
'''
#Rearrange : lowercase then uppercase
string = 'dsfdAAdfsTHKGF'
lower = ''
upper = ''
for letters in string:
    if letters.islower():
        lower += letters
    else:
        upper += letters

print(lower+upper)
'''
'''
#remove punctuations in a string
punctuation = "!@#$%^&*()[]{}:;',./?|"
string = input("enter string with punctuation ")
word = ''
sp_letters = ''
for letter in string:
    if letter in punctuation:
        sp_letters += letter
    else:
        word += letter
print(word, '----', sp_letters)
'''

'''
#print functions
a=10
b='nanda'
c='learn'
print(a,b,c,sep='-')
print(a)
print(b)
print(c)
print(a, end='#')
print(b, end='#')
print(c, end='\n')
#formated printing
x=22
y=7
z=x/y
print('division of {0}, and {1} is{2}'.format(x,y,z))
print(f"division of {x} and {y} is{z}")
'''
