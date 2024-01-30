# intuition - if there is an overlap among two consecutive jobs, then the job with lesser earning of the two will be eliminated.
# if the two earnings are equal, the job with an earlier end time will be eliminated.
# the jobs and earnings remaining after lokesh is done choosing, will be the difference of the original list and the new list hence formed.


def lokesh(n, j):

    lis = j[:]
    j.sort(key = lambda x: x[1])   # sorting the list according to their end times
    i = 0

    # iterating through the list, 2 jobs at a time
    while i < len(j) - 1:
        if j[i][1] > j[i+1][0]:      # checking if there is an overlap
            if j[i][2] > j[i+1][2]:  # removing the job with lesser earning
                j.pop(i+1)
            elif j[i][2] < j[i+1][2]:
                j.pop(i)
            else:
                j.pop(i+1)
        else:
            i += 1
    
    totalsum = 0   # this variable contains the total amount of earnings available originally
    tempsum = 0    # this variable contains the total amount of earnings taken by lokesh
    for x in lis:
        totalsum += x[2]
    
    for y in j:
        tempsum += y[2]
    
    return [len(lis) - len(j), totalsum - tempsum]


n = int(input("Please enter number of jobs:"))
if n >= 100:
    print("Can only input less than 100 jobs")
    n = int(input())

jobs_list = []

for _ in range(n):
    print("Enter Start Time")
    start_time = int(input())
    if start_time > 2359:
        print("Please enter a valid start time. Must be only between 00:00 and 23:59")
        start_time = int(input("Enter valid start time"))

    print("Enter End Time")
    end_time = int(input())
    if end_time > 2359:
        print("Please enter a valid end_time. Must be only between 00:00 and 23:59")
        end_time = int(input("Enter valid end time"))
        
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