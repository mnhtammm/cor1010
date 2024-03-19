#random numbers:

import random
import numpy as np

number = random.randint(1, 20)
print(number)

listofrandomnumbers = []
for i in range(100):
    x = random.randint(1, 20)
    listofrandomnumbers.append(x)

print(listofrandomnumbers)

list2 = [random.randint(1,20) for i in range (100)]
print(list2)
print("length of list 2 is", len(list2))

total = 0
for number in listofrandomnumbers:
    total = total + number
print("total: ", total)

totalsum = sum(list2)
print("total: ", total, totalsum)



# npnumber = np.random.