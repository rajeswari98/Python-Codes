'''
Given a 2-D String array of student-marks find the student with the highest average and output his average score. If the average is in decimals, floor it down to the nearest integer.

Example 1:
----------
Input:  [{"Bob","87"}, {"Mike", "35"},{"Bob", "52"}, {"Jason","35"}, {"Mike", "55"}, {"Jessica", "99"}]
Output: 99
Explanation: Since Jessica's average is greater than Bob's, Mike's and Jason's average.
'''
import math


def maxAvgScore(scores):
    maxAvg = -math.inf
    if not scores:
        return maxAvg
    grades = {}
    
    for name, score in scores:
        if name not in grades:
            grades[name] = [0,0]
        grades[name][0] += int(score)
        grades[name][1] += 1
    # print(grades, maxAvg)
    
    for val in grades.values():
        maxAvg = max(maxAvg, val[0]//val[1])
    
    return maxAvg


# scores = [("Bob","87"), ("Mike", "35"),("Bob", "52"), ("Jason","35"), ("Mike", "55"), ("Jessica", "99")]
scores = [["Bob","100"], ["Charles", "30"],["Bob", "20"], ["Marie", "80"]]
print(math.floor(maxAvgScore(scores)))