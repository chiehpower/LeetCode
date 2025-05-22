"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 
Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Spiral Matrix.
        Memory Usage: 19.20 MB, less than 20.98% of Python3 online submissions for Spiral Matrix.
        """
        def findleft():
            res = -1
            left, right = 0, len(nums) - 1
            while left <= right:
                med = (right + left) // 2
                if nums[med] < target:
                    left = med + 1
                else:
                    if nums[med] == target:
                        res = med
                    right = med - 1
            return res 

        def findright():
            res = -1 
            left, right = 0, len(nums) - 1
            while left <= right:
                med = (right + left) // 2
                if nums[med] > target:
                    right = med - 1
                else:
                    if nums[med] == target:
                        res = med
                    left = med + 1
            return res
        return [findleft(), findright()]

        
