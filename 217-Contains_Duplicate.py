# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 20:15:08 2021

@author: Huiying Sabrina Wang

217. Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true


"""
def containsDuplicate(nums) -> bool:
    thisset=set(nums)
    return len(thisset)<len(nums)

print(containsDuplicate([1,2,3,1]))
print(containsDuplicate( [1,2,3,4]))
print(containsDuplicate( [1,1,1,3,3,4,3,2,4,2]))