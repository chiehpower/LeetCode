"""
Given an integer array nums, return an array answer such that answer[i] 
is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity? 
(The output array does not count as extra space for space complexity analysis.)
"""


class Solution:
    def productExceptSelf(self, nums):
        """
        Runtime: 262 ms, faster than 84.99% of Python3 online submissions for Product of Array Except Self.
        Memory Usage: 22.9 MB, less than 10.40% of Python3 online submissions for Product of Array Except Self.
        """
        total = len(nums)
        res_left = [1 for i in range(total)]
        # Left
        for i in range(1, total):
            res_left[i] = res_left[i-1] * nums[i-1]
        
        # Right
        res_right = [1 for i in range(total)]
        for i in range(-2, -total-1, -1):
            res_right[i] = res_right[i+1] * nums[i+1]
        
        # Combine
        res = [1 for i in range(total)]
        for i in range(total):
            res[i] = res_left[i] * res_right[i]
        return res
            
            
if __name__ == '__main__':
    Solution = Solution()

    nums = [1,2,3,4]
    result = Solution.productExceptSelf(nums)
    print(f"My ans is: {result}, Ans: [24,12,8,6]")
        
    nums = [-1,1,0,-3,3]
    result = Solution.productExceptSelf(nums)
    print(f"My ans is: {result}, Ans: [0,0,9,0,0]")