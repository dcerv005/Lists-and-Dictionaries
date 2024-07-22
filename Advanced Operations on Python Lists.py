import time

#Task 1

def squareNumbers (n):
    squaredList = []
    start_time = time.time()
    for i in range(n):
        squaredList.append((i+1)**2)
    end_time= time.time()
    squaredtime= end_time-start_time
    print(squaredtime)
    return squaredList

    
#O(n)




print(squareNumbers(4))

#Task 2

istVar = ['a','b','c','d']
start_time= time.time()
sublist= istVar[1:3]
r=sublist[::-1]
end_time= time.time()
reversedtime= end_time-start_time
print(reversedtime)
print(r)


#Task 3

list1=['Hello', 'World', 'Alphabet']

list2=[1, 2, 3]

list1.sort()
list2.sort()
list1.extend(list2)
print(list1)