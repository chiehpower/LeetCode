"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Greedy Algorithm
        Runtime: 48 ms, faster than 22.24% of Python3 online submissions for Summary Ranges.
        Memory Usage: 18.37 MB, less than 95.75% of Python3 online submissions for Summary Ranges.
        """
        max_reach = 0
        for i in range(len(nums)):
            if i > max_reach:
                # If the current index is greater than the maximum reachable index, return False
                return False
            # Update the maximum reachable index
            max_reach = max(max_reach, i + nums[i])
        return True