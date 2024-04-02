import numpy as np

d = {"a": 0, "b": 1, "c": 2}

keyvalue = dict()

print(d)

for key, value in d.items():
    #print(key,value)
    print(f"{key} : {value}")

print(d['a'], d['c'])

d['a'] += 10
d['c'] += 20
print(d['a'], d['c'])

kv = { 10: 0, 20: 1, 30: "hello"}
print("keys: ", kv.keys())
print("values: ", kv.values())

string = "this is a string."

def getUniqueLetters(filename):
    uniqueletters = set()
    with open(filename, "r", encoding='utf-8') as filehandler:
        n = 0
        while True:
            line = filehandler.readline()
            if not line:
                break
            n += 1
            for letter in line:
                if letter not in uniqueletters:
                    uniqueletters.add(letter)