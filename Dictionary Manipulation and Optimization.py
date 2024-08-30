import time

#Task1


def merge_dict(dict1, dict2):
    start_time= time.time()
    dict1.update(dict2)
    end_time= time.time()

    total_time=end_time-start_time
    print("Time to run", total_time)
    print(dict1)
#O(n)

#Task 2


def merge_dict_intercept(dict1, dict2):
    start_time = time.time()
    mergedDict={}

    for i in dict1:
        if i in dict2:
            mergedDict[i]=[]
            mergedDict[i].append(dict1[i])
            mergedDict[i].append(dict2[i])
    end_time= time.time()
    total_time=end_time-start_time
    print("Time to run", total_time)
    print(mergedDict)

#O(n)

#Task 3


def count_frequency(list):
    start_time = time.time()
    dict5={}

    for i in list:
        if i in dict5:
            dict5[i] += 1
        else:
            dict5[i]=1
    end_time = time.time()
    total_time=end_time-start_time
    print("Time to run", total_time)
    print(dict5)
#O(n)

dict1= {'a': 1, 'b': 2}
dict2={'c':3, 'd': 4}

dict3= {"Fantasy": "Harry potter", "Comedy": "Tropic Thunder", "Adventure": "Zathura" }
dict4= {"Sci-Fi": "Star Wars", "Comedy": "Scary Movie", "Adventure": "Mr. Deeds"}

list = [1, 1, 1, 2, 3, 3, 3, 3, 3, 4, 2, 4, 5, 3, 3, 4, 1, 6, 8, 9, 8, 8, 7, 0, 9, 8]

merge_dict_intercept(dict3, dict4)
merge_dict(dict1, dict2)
count_frequency(list)
