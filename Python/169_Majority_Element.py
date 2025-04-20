"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3

Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
 

Follow-up: Could you solve the problem in linear time and in O(1) space?
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Runtime: 13 ms, faster than 19.69% of Python3 online submissions for Summary Ranges.
        Memory Usage: 19.47 MB, less than 19.94% of Python3 online submissions for Summary Ranges.
        """
        number = {}
        for i in nums:
            if i not in number:
                number[i] = 1
            else:
                number[i] += 1
        key = max(number, key=number.get)
        return key

    