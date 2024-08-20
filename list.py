'''
print(list("nanda"))

checked_list = [1, 2, 3, 4, 5]
print(1 in checked_list)
print(8 not in checked_list)
print(5 not in checked_list)
'''
'''
#index
index_exp = [["wood"], [1,2,3], [11,22,33], ["thank"]]
print(index_exp[0])
print(index_exp[3])
print(index_exp[2][2])

negative = [1, 2, 3, 4, 5]
print(negative[-2])
print(negative[-0])
print(negative[-5])

mixed = [False, "true", 3.33, "i am good"]
print(mixed[2] + 6.66)
print(mixed[-3] + "bad", [3])

sliced = [11, 22, 33, 44, 55, 66]
print(sliced[:2])
print(sliced[::2])
print(sliced[::-1])
print(sliced[1::2])
print(sliced[1:3])

example = ["thank", "good", "ok"]
print(example)
example[0] = "very"
print(example)
'''
'''
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list1[-1::-2])
list1[0:3] = [11,22,33]
print(list1)

l1 = [1,2,3]
l2 = [4,5,6]
l4 = ['a','b','c']
l3 = l1+l2+l4
print(l3)
l3.extend(['x', 'y', 'z'])
print(l3)
l1 = l1 * 3
print(l1)

#iterating a list
for item in range(len(l3)):
    print(l3[item])

for item in range(len(l3)-1,-1,-1):
    print(l3[item])

i=0
while i < len(l3):
    print(l3[i])
    i+=1
'''
'''
#list methods
list1 = [1, 2, 3, 4, 5]
list1.append('a')
print(list1)
list1.extend(['b','c'])
print(list1)
list1.extend(['xyz'])
print(list1)
list1.insert(8, 'ddd')
print(list1)
list5= list1.copy()
print('new', list5)
list5.pop() #delete the last list item
print(list5)

list5.pop(0) #with idex
print(list5)

list5.remove('ddd') # remove the item directly
print(list5)

list6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l7 = list6.index(3)
print(l7)
list6.sort(reverse=True)
print(list6)

l8 = ['dd','ss', 'gg', 'AA']
l8.sort()
print(l8)
l8.sort(key=str.lower)
print(l8)
'''
'''
l1 = []
for items in range(10):
    l1.append(items)
print(l1)


l2 = [item**2 for item in range(10)]
print(l2)

l3 = [x for x in (10, 5, 7, 8, 12) if x % 2 == 0]
print(l3)

l4 = [x.lower() for x in 'PytHon']
print(l4)

l5 = [x for x in 'dsfhkdsf%%4#$$11df' if x.isalpha()]
print(l5)

data = input('enter the names: ')
l6 = data.split()
print(data)
type(data)
print(type(data))
'''
'''
#matrix
a = [[1,2,3],[4,5,6],[7,8,9]]
b = [[9,8,7],[6,5,4],[3,2,1]]

c = []
for i in range(len(a)):
    s = []
    for j in range(len(a[0])):
        s.append(a[i][j] + b[i][j])
    c.append((s))
print(c)
'''
'''
#calculate salary, weekly working hours in a list

work_hours = input('enter the work hours, sepeparated by spaace:')
work_hours = work_hours.split()
work_hours = [int(x) for x in work_hours]

wage = int(input('enter the wage:'))
print(f"salary is : {sum(work_hours) * wage}")
'''
#removing the duplicates in a list






