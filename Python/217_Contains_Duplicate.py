"""
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
 
Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

class Solution:
    def containsDuplicate(self, nums):
        """
        Runtime: 672 ms, faster than 62.02% of Python3 online submissions for Contains Duplicate.
        Memory Usage: 26.1 MB, less than 27.30% of Python3 online submissions for Contains Duplicate.
        """
        if len(nums) == 1:
            return False
        if len(nums) != len(set(nums)):
            return True
        else:
            return False


if __name__ == "__main__":
    Solution = Solution()

    nums = [1, 2, 3, 1]
    result = Solution.containsDuplicate(nums)
    print(f"My ans is: {result}\n, Ans: True")

    nums = [1, 2, 3, 4]
    result = Solution.containsDuplicate(nums)
    print(f"My ans is: {result}\n, Ans: False")
    
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    result = Solution.containsDuplicate(nums)
    print(f"My ans is: {result}\n, Ans: True")


