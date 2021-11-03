# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 19:46:54 2021

@author: Huiying Sabrina Wang

977 Squares of a sorted array

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.

"""
"""
nums=[-4, -1, 0, 3, 10]
squared_nums=[16,1,0,9,100]
after sorting, [0,1,9,16,100]
"""
def sortedSquares(nums):
    left=0
    right=len(nums)-1
    squared_nums=[0]*(len(nums))
     
    for i in range(len(nums)-1, -1, -1):
        if abs(nums[left])<abs(nums[right]):
            square=nums[right]
            right-=1
        else:
            square=nums[left]
            left+=1
        squared_nums[i]=square*square
    return squared_nums

print(sortedSquares([-4,-1,0,3,10]))
print(sortedSquares( [-7,-3,2,3,11]))

"""
time complexity: O(log N)
space complexity: O(N)
"""