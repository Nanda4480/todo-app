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



