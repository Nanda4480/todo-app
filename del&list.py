'''
names = ["nanda", "usha", "udi", "rithi", "et cetra"]
del names[2:3]
print(names)
del names[1]
print(names)
names.remove("et cetra")
print(names)
names.append("soma")
print(names)
names.insert(2, "pammi")
print(names)
names.sort()
print(names)
names.sort(reverse=True)
print(names)
names.reverse()
print(names)

name = ["nanda", "usha", "udi", "rithi", "et cetra"]
newname = name.pop()
print(name)
print(newname)
newname = name.pop(3)
print(newname)
'''
#copy module - deepcopy

import copy
ex_1 = [1, 2, 3]
ex_2 = copy.deepcopy(ex_1)
print(ex_1)
print(ex_2)


