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

# class Solution:
#     """08/01/2020 00:56"""
#     def twoSum(self, nums, target):
#         res = []
#         if len(nums) >= 2:
#             a = len(nums)
#             for i in range(a):
#                 for j in range(i+1,a):
#                     sum_number = nums[i] + nums[j]
#                     if sum_number == target:
#                         return [i,j]


# class Solution:
#     """09/02/2022 21:39"""
#     def twoSum(self, nums, target):
#         """
#         Runtime: 7103 ms, faster than 7.82% of Python3 online submissions for Two Sum.
#         Memory Usage: 15 MB, less than 76.35% of Python3 online submissions for Two Sum.
#         """
#         for i in range(len(nums)):
#             if nums[i] == 0:
#                 pass
#             for j in range(i+1, len(nums)):
#                 sum = nums[i] + nums[j]
#                 if sum > target: continue
#                 elif sum < target: continue
#                 else:
#                     return [i, j]
        
# class Solution:
#     """09/02/2022 21:39"""
#     def twoSum(self, nums, target):
#         """
#         Runtime: 792 ms, faster than 34.85% of Python3 online submissions for Two Sum.
#         Memory Usage: 14.8 MB, less than 99.57% of Python3 online submissions for Two Sum.
#         """
#         for i in range(len(nums)):
#             b = target - nums[i]
#             remain = nums[i+1:]
#             if b in remain:
#                 return [i, remain.index(b)+i+1]

class Solution(object):
    """09/03/2022 13:32"""
    def twoSum(self, nums, target):
        """
        Runtime: 133 ms, faster than 40.45% of Python3 online submissions for Two Sum.
        Memory Usage: 15.2 MB, less than 49.63% of Python3 online submissions for Two Sum.
        """
        record = {}
        for a in range(len(nums)):
            b = target - nums[a]
            if b in record:
                return [record[b], a]
            else:
                record[nums[a]] = a 

class Solution(object):
    """24/03/2023 23:58"""
    def twoSum(self, nums, target):
        """
        Runtime: 64 ms, faster than 69.98% of Python3 online submissions for Two Sum.
        Memory Usage: 15.2 MB, less than 16.37% of Python3 online submissions for Two Sum.

        記錄"補數"，如果這個補數沒出現，就記錄當下的數值，未來當下的這個數值nums[i]可能會成為別人的補數。
        """
        seen = {}
        for i in range(len(nums)):
            res = target - nums[i] 
            if res not in seen:
                seen[nums[i]] = i
            else:
                return [seen[res], i]

    def twoSum_20250330(self, nums, target):
        """
        Runtime: 297 ms, faster than 33.79% of Python3 online submissions for Two Sum.
        Memory Usage: 18.10 MB, less than 99.66% of Python3 online submissions for Two Sum.
        """
        total = len(nums)
        if total == 2:
            return [0, 1]

        first_order = 0
        for i in nums:
            remain = target - i
            if remain not in nums[first_order + 1:]:
                first_order += 1
                continue
            else:
                for j in range(first_order + 1, total):
                    if remain == nums[j]:
                        return [first_order, j]
                first_order += 1

start = time.time()
Solution = Solution()

## 1
inputs = [1, 3, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]
target = 18

result = Solution.twoSum(inputs, target)
print(result) # Answer: [2,7]

print("Time :", time.time() - start)

## 2
inputs = [2, 7, 11, 15]
target = 9

result = Solution.twoSum(inputs, target)
print(result)  # Answer: [0,1]

## 3
inputs = [3, 2, 4]
target = 6

result = Solution.twoSum(inputs, target)
print(result) # Answer: [1,2]

## 4 
inputs = [2, 7, 11, 15]
target = 18 

result = Solution.twoSum(inputs, target)
print(result)  # Answer: [1,2]


## 5
inputs = [3, 3]
target = 6

result = Solution.twoSum(inputs, target)
print(result)  # Answer: [0,1]

## 6 
inputs = [0, 4, 3, 0]
target = 0
result = Solution.twoSum(inputs, target)
print(result)  # Answer: [0,3]

## 7
inputs = [-1, -2, -3, -4, -5]
target = -8
result = Solution.twoSum(inputs, target)
print(result)  # Answer: [2,4]


