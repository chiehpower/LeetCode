"""
Given a binary array nums and an integer k, return the maximum 
number of consecutive 1's in the array if you can flip at most k 0's.


Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length
"""
class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        Reference: https://leetcode.com/problems/max-consecutive-ones-iii/solutions/1793625/python-3-very-typical-sliding-window-hashmap-problem/?envType=study-plan-v2&envId=leetcode-75
        """
        l = 0
        ans = 0
        count = {0: 0, 1: 1}
        
        for r, num in enumerate(nums):

            count[num] += 1
            
            while count[0] > k:
                count[nums[l]] -= 1
                l += 1 
            

            new_size = r - l + 1
            ans = max(ans, new_size)
        return ans