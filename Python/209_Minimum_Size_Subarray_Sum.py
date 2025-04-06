"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. 
If there is no such subarray, return 0 instead.

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104
"""
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        Runtime: 7 ms, faster than 92.13% of Python3 online submissions for Summary Ranges.
        Memory Usage: 28.43 MB, less than 11.07% of Python3 online submissions for Summary Ranges.

        Slide window方式
        盡量讓end能走就走，每走一個就加進total裡面
        當total >= target的時候，就代表可以開始縮小slide window的大小，因此增加start的範圍
        不過當start增加的時候，total也要減去nums[start]的值
        同時也要更新min_len的值
        """
        total, start, end = 0, 0, 0
        min_len = float('inf')

        for end in range(len(nums)):
            
            total += nums[end]

            while total >= target:
                min_len = min(min_len, end - start + 1)
                total -= nums[start]
                start += 1

        if min_len != float('inf'):
            return min_len
        else:
            return 0