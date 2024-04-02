filename = "pg1342.txt"

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

print(f"Total {n} lines from {filename}: {len(uniqueletters)} letters in the set {uniqueletters}")

# 2. count each letter, going through the txt file from the beginning

#2.1 initialize the dictionary
counts = {}
for letter in uniqueletters:
    counts[letter] = 0
print(counts)

with open(filename, "r", encoding='utf-8') as file:
    n = 0
    while True:
        line = file.read()
        if not line:
            break
        n += 1

        for letter in line:
            counts[letter] += 1

        if n == 1:
            break            

for key, value in counts.items():
    if value > 0:
        print(key, ":", value)