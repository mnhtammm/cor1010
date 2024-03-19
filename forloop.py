

names = ["Tam", "Dau", "Pk", "Tom", "Hanh", "Hoa"]

print( names[0] )
print( names[1] )

names.append("Bang Chan")

print(names)

second_names = ["Felix"] + names
print(second_names)

print("-------")
for item in names:
    print(item + " alo? em a? nho anh khong?")
print("Finished.")

print("--------")

for string in second_names:
    print("alo? " + string + " a? Nho anh khong? Nho a? Lam gi day?")
    print(string[0] + " kho vai l")
    for c in string:
        print(c)
print("Finished.")

for k in [0, 1, 2, 3, 4, 5, 6]:
    print(k, names[k])

# hundnames = [ f"name_{i}" for i in range(100) ]
# print(hundnames)

for k in range(len(names)):
    print(k, names[k])

for k in range(7):
    print(k, names[k])