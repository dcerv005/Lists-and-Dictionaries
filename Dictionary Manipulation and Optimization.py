#Task1

dict1= {'a': 1, 'b': 2}
dict2={'c':3, 'd': 4}

dict1.update(dict2)

print(dict1)

#Task 2

dict3= {"Fantasy": "Harry potter", "Comedy": "Tropic Thunder", "Adventure": "Zathura" }
dict4= {"Sci-Fi": "Star Wars", "Comedy": "Scary Movie", "Adventure": "Mr. Deeds"}

mergedDict={}

for i in dict3:
    if i in dict4:
        mergedDict[i]=[]
        mergedDict[i].append(dict3[i])
        mergedDict[i].append(dict4[i])

print(mergedDict)



#Task 3

list = [1, 1, 1, 2, 3, 3, 3, 3, 3, 4, 2, 4, 5, 3, 3, 4, 1, 6, 8, 9, 8, 8, 7, 0, 9, 8]

dict5={}

for i in list:
    if i in dict5:
        dict5[i] += 1
    else:
        dict5[i]=1

print(dict5)