"""
Given an integer array nums, move all 0's to the end 
of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

- Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

- Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1

Source from: LeetCode 

# Results: 
Runtime: 640 ms, faster than 31.83% of Python3 online submissions for Squares of a Sorted Array.
Memory Usage: 14.6 MB, less than 39.28% of Python3 online submissions for Squares of a Sorted Array.
"""


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i, num in enumerate(nums):
            if num == 0:
                count += 1
        
        for i in range(count):
            nums.remove(0)

        for i in range(count):
            nums.append(0)
        
        return nums
    def moveZeroes_20250902(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastNonZeroValue = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lastNonZeroValue] = nums[i]
                lastNonZeroValue += 1
        for i in range(lastNonZeroValue, len(nums)):
            nums[i] = 0