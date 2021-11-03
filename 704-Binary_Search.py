# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 18:53:34 2021

@author: Huiying Sabrina Wang

704. Binary Search
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 

Constraints:

1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.
"""
def search(nums, target: int) -> int:
    left=0
    right=len(nums)
    
    while left<right:
        mid=int((left+right)/2)
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            left=mid+1
        else:
            right=mid
    return -1

print(search([-1, 0, 3, 5, 9, 12], 9))
print(search([-1,0,3,5,9,12], 2))

"""
Time Complexity: O(log N)
Space Complexity: O(1)
"""