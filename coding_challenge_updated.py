def lokesh(n, j):

    lis = j[:]
    j.sort(key = lambda x: x[1])
    i = 0

    while i < len(j) - 1:
        if j[i][1] > j[i+1][0]:
            if j[i][2] > j[i+1][2]:
                j.pop(i+1)
            elif j[i][2] < j[i+1][2]:
                j.pop(i)
            else:
                j.pop(i+1)
        else:
            i += 1
    
    totalsum = 0
    tempsum = 0
    for x in lis:
        totalsum += x[2]
    
    for y in j:
        tempsum += y[2]
    
    return [len(lis) - len(j), totalsum - tempsum]


n = int(input("Please enter number of jobs:"))
jobs_list = []

for _ in range(n):
    print("Enter Start Time")
    start_time = int(input())
    print("Enter End Time")
    end_time = int(input())
    print("Enter earning")
    earning = int(input())

    jobs_list.append([start_time, end_time, earning])

result = lokesh(n, jobs_list)
print(result)




# testcase1 = [[900 ,1030, 100], [1000, 1200, 500], [1100, 1200, 300]]
# testcase2 = [[900, 1000, 250], [945, 1200, 550], [1130, 1500, 150]]
# testcase3 = [[900, 1030, 100], [1000, 1200, 100], [1100, 1200, 100]]

# result1 = lokesh(testcase1)
# result2 = lokesh(testcase2)
# result3 = lokesh(testcase3)

# if result1 == [2, 400]:
#     print("Test Case Passed")
# else:
#     print("Test Case Failed")

# if result2 == [2, 400]:
#     print("Test Case Passed")
# else:
#     print("Test Case Failed")

# if result3 == [1, 100]:
#     print("Test Case Passed")
# else:
#     print("Test Case Failed")