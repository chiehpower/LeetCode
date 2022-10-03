"""
Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, 
try coding another solution using the divide and conquer approach, which is more subtle.
"""

class Solution:
    def maxSubArray(self, nums):
        """
        https://leetcode.com/problems/maximum-subarray/discuss/20396/Easy-Python-Way
        
        Runtime: 1585 ms, faster than 34.55% of Python3 online submissions for Maximum Subarray.
        Memory Usage: 28.6 MB, less than 10.46% of Python3 online submissions for Maximum Subarray.
        """
        if len(nums) == 1: return nums[0]
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums) 
            
if __name__ == '__main__':
    
    Solution = Solution()

    nums = [-2,1,-3,4,-1,2,1,-5,4]

    result = Solution.maxSubArray(nums)
    print(f"My ans is: {result}, Ans = 6\n")

    nums = [1]
    
    result = Solution.maxSubArray(nums)
    print(f"My ans is: {result}, Ans = 1\n")
        
    nums = [5,4,-1,7,8]
    
    result = Solution.maxSubArray(nums)
    print(f"My ans is: {result}, Ans = 23\n")
    
    nums = [-2, 1]
    
    result = Solution.maxSubArray(nums)
    print(f"My ans is: {result}, Ans = 1\n")