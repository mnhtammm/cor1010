filename = "pg1342.txt"
# filename = "num.txt"

#f2 = open("prog1.py", "r")
#n = 0
#while True: #repeat forever
#    line = f2.readline()
#    if not line:
#        break #get out of the while.loop
#    n += 1
#    print(n, line)

# 1. make a list of unique letters
uniqueletters = []
filehandler = open(filename, "r", encoding='utf-8') # w= write, r= read

n = 0
u = []
while True:
    line = filehandler.readline()
    if not line:
        break
    n += 1
    for letter in line:
        if letter not in u:
            u.append(letter)
    # print(n, line)
    # if n>3:
    #    break
# filehandler.close()
# print(n, len(u), u)
print(f"Total {n} lines from {filename}: {len(uniqueletters)} letters in the set {uniqueletters}")

#make a list of unique letters
#count each letter, going through the txt file from the beginning