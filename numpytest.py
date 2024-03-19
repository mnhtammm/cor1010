import numpy as np

print('my numpy version: ', np.__version__)

n = np.random.randint(1, 20)
list = []
for i in range(1000000):
    n = np.random.randint(1,20)
    list.append(n)
print("list: ", list)
