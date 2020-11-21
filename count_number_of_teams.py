'''
https://leetcode.com/problems/count-number-of-teams/
There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

    Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
    A team is valid if:  (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).

Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

 

Example 1:

Input: rating = [2,5,3,4,1]
Output: 3
Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 

Example 2:

Input: rating = [2,1,3]
Output: 0
Explanation: We can't form any team given the conditions.

Example 3:

Input: rating = [1,2,3,4]
Output: 4
'''


def numTeams(rating):
    n = len(rating)
    if n < 3:
        return 0
    
    g = [0] * n # <- Greater count
    s = [0] * n # <- Smaller count
    res = 0 # <- number of teams
    
    # For each soldier, we search the next greater and smaller
    for i in range(n - 1):
        for j in range(i + 1, n):
            if rating[j] > rating[i]: 
                g[i] += 1
            else:
                s[i] += 1
    
    # Now, we looking for the "last number" . If rating[i] < rating[j] then g[j] are the following possible numbers
    #                                       .    rating[i] > rating[j]      s[j] 
    for i in range(n - 2):
        for j in range(i + 1, n):
            if rating[j] > rating[i]:
                res += g[j]
            else:
                res += s[j]
    
    return res

print(numTeams([1,2,3,4]))