"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

Source from: LeetCode 
"""
import time

class Solution:
    def twoSum(self, nums, target):
        res = []
        if len(nums) >= 2:
            a = len(nums)
            for i in range(a):
                for j in range(i+1,a):
                    sum_number = nums[i] + nums[j]
                    if sum_number == target:
                        return [i,j]
        
start = time.time()
Solution = Solution()

inputs = [1, 3, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]
target = 18

result = Solution.twoSum(inputs, target)
print(result)

print("Time :", time.time() - start)
