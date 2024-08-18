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
#find user id and domain name from the email address
email = input("enter your favorite email: ")
atrate = email.find('@') #this find method will show the index of @
print('user id:', email[0:atrate])
print('domain id:', email[atrate+1:])



