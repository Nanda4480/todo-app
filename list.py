'''
print(list("nanda"))

checked_list = [1, 2, 3, 4, 5]
print(1 in checked_list)
print(8 not in checked_list)
print(5 not in checked_list)
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

