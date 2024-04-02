import numpy as np

longString = "Oi xin chao ca nha tam buon ngu qua ca nha co thay buon ngu khong nhi sao hom nay no co the buon ngu den nhu vay duoc co chu."

print( len(longString) )

#compute the number of characters in longString

count = 0

for string in longString:
        count += 1

print("number of characters: ",count)

uniqueCharacters = []
letterSet = []
for string in longString:
        if string not in uniqueCharacters:
                uniqueCharacters.append(string)
                letterSet.append(string)


print("uniqueCharacters: ", len(uniqueCharacters), uniqueCharacters)
print("uniqueSet: ", len(letterSet), letterSet)

letterList = []
for elem in letterSet:
        letterList.append(elem)

letterList2 = list(letterSet)
print(letterList)
print(letterList2)