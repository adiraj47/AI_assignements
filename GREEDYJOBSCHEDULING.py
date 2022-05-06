def printjobschedule(array, t):
    m = len(array)
    
    for j in range(m):
        for q in range(m - 1 - j):
            if array[q][2] < array[q + 1][2]:
                array[q], array[q + 1] = array[q + 1], array[q]
    res = [False] * t
    
    job = ['-1'] * t
    for q in range(len(array)):
        
        for q in range(min(t - 1, array[q][1] - 1), -1, -1):
            if res[q] is False:
                res[q] = True
                job[q] = array[q][0]
                break
    print(job)

array = [['a',2, 30],
       ['b', 1, 3],
       ['c', 3, 5],
       ['d', 4, 20],
       ['e', 3, 18],
       ['f', 1, 2],
       ['g',1, 6]]
print("Maximum profit sequence of jobs is- ")
printjobschedule(array, 4)
