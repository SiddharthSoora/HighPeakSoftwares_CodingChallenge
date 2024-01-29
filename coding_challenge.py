#intuition - lokesh chooses the highest paying job in a particular timeframe
# the same intuition continues for every interval of time and skips the intervals which are overlapping
# with the one paying the highest amount.


def lokeshearnings(j):
    # Sort the jobs based on end times

    newjob = sorted(j, key = lambda i:i[2]) #check if list sorted according to earnings is the same as original list

    if newjob == j:
        lokesh = 0
        res1 = 0
        res2 = 0
        prev = 0
    
        for job in j:
            st, et, earn = job
        
            # Check if the current job overlaps with the previous one
            if st >= prev:
                lokesh += earn
                prev = et
            else:
                res1 += 1
                res2 += earn
    
        return [res1, res2]
        
    else:
        j.sort(key = lambda i:i[2])
        lokesh = 0
        res1 = 0
        res2 = 0
        prev = 0
    
        for job in j[::-1]:
            st, et, earn = job
        
            # Check if the current job overlaps with the previous one
            if st >= prev:
                lokesh += earn
                prev = et
            else:
                res1 += 1
                res2 += earn
    
        return [res1, res2]


#testcases
testcase1 = [[900 ,1030, 100], [1000, 1200, 500], [1100, 1200, 300]]
testcase2 = [[900, 1000, 250], [945, 1200, 550], [1130, 1500, 150]]
testcase3 = [[900, 1030, 100], [1000, 1200, 100], [1100, 1200, 100]]

result1 = lokeshearnings(testcase1)
result2 = lokeshearnings(testcase2)
result3 = lokeshearnings(testcase3)

if result1 == [2, 400]:
    print("Test Case Passed")
else:
    print("Test Case Failed")

if result2 == [2, 400]:
    print("Test Case Passed")
else:
    print("Test Case Failed")

if result3 == [1, 100]:
    print("Test Case Passed")
else:
    print("Test Case Failed")