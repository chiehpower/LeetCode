"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Example 3:

Input: nums = [1,0,1,2]
Output: 3
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Runtime: 490 ms, faster than 5.01% of Python3 online submissions for Summary Ranges.
        Memory Usage: 31.76 MB, less than 96.64% of Python3 online submissions for Summary Ranges.
        """
        new = sorted(nums)
        if len(nums) == 1:
            return 1
        elif len(nums) == 0:
            return 0

        max_value = 1
        current = 1
        total = len(new)
        for i in range(1, total):

            if new[i] == new[i-1]:
                continue


            if (new[i] - 1) == new[i-1]:
                current += 1
                if current >= max_value:
                    max_value = current
            else:

                current = 1
        return max_value

    def optimalLongestConsecutive(self, nums: List[int]) -> int:
        new_nums = set(nums)
        longest = 0
        if len(new_nums) == 1:
            return 1
        elif len(new_nums) == 0:
            return 0

        for num in new_nums:
            if num - 1 not in new_nums:
                current = num
                streak = 1

                while current + 1 in new_nums:
                    current += 1
                    streak += 1

                longest = max(streak, longest)
        return longest
