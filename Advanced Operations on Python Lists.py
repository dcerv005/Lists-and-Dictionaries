import time

#Task 1

def squareNumbers (n):
    squaredList = []
    start_time = time.time()
    squared = [(x+1)**2 for x in range(n)]
    end_time= time.time()
    squaredtime= end_time-start_time
    print(squaredtime)
    return squared

    
#O(n)




print(squareNumbers(4))

#Task 2

istVar = ['a','b','c','d']
def reverse(list, i, j):
    start_time= time.time()
    sublist= list[i:j+1]
    r=sublist[::-1]
    end_time= time.time()
    reversedtime= end_time-start_time
    print(reversedtime)
    print(r)

reverse(istVar, 1, 3)
#O(n)

#Task 3
list1=['Hello', 'World', 'Alphabet']
list2=[1, 2, 3]
def sortlist(list1, list2):
    list1.sort()
    list2.sort()
    list1.extend(list2)
    print(list1)

sortlist(list1, list2)
#O(n*log(n))
