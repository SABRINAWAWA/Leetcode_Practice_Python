# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 19:07:59 2021

@author: Huiying Sabrina Wang
278. First Bad Version
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example 1:

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
Example 2:

Input: n = 1, bad = 1
Output: 1
"""

"""
version list: [1, 2, 3, 4, 5]
bad version = 4
R1: left=1; right=5; mid=3;
if isBadVersion(mid)==false, ==> move right ==> left=mid+1
left=4, right=5, mid=4
if isBadVersion(mid)==true, ==> move left ==>right=mid
"""
def isBadVersion(n):
    return n==1

def firstBadVersion(n):
    """
    :type n: int
    :rtype: int
    """
    left=1
    right=n
    while left<right:
        mid=int((left+right)/2)
        if isBadVersion(mid):
            right=mid
        else:
            left=mid+1
    return left

#print(firstBadVersion(5))
print(firstBadVersion(1))

"""
time complexity: O(log N)
space complexity: O(1)
"""