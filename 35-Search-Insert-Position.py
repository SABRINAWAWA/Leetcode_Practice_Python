# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 19:27:56 2021

@author: Huiying Sabrina Wang

35. Search Insert Position
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
Example 4:

Input: nums = [1,3,5,6], target = 0
Output: 0
Example 5:

Input: nums = [1], target = 0
Output: 0
"""
"""
Case 1: [1, 3, 5, 6], target=5
left=1, right=6. mid=3
mid<target ==> left=3, right=6, mid=5
mid==target. return mid
"""
def searchInsert(nums, target: int) -> int:
    left=0
    right=len(nums)-1
    while left<=right:
        mid=int((left+right)/2)
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return left
print(searchInsert([1, 3, 5,6], 2))