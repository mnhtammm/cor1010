import numpy as np

tamxinh = np.random.randint(0, 10, size=20)
print(tamxinh)

# to make a group of cac so khac nhau

unique = []
for number in tamxinh:
    if number in unique:
        pass
    else:
        unique.append(number)

print("unique: ", unique)
#
unique2 = list() #[]
for number in tamxinh:
    if number not in unique2:
        unique2.append(number)

print("unique2: ", unique2)
#
myList = []
mylist2 = []
# set, dict
uniqueSet = set()
for num in tamxinh:
    uniqueSet.add(num)

print(uniqueSet)
for elem in uniqueSet:
    print(elem, end=' ')
print()