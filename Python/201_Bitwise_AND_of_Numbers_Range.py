"""
Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: left = 5, right = 7
Output: 4
Example 2:

Input: left = 0, right = 0
Output: 0
Example 3:

Input: left = 1, right = 2147483647
Output: 0

Constraints:

0 <= left <= right <= 231 - 1
"""
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        """
        Runtime: 1 ms, faster than 82.91% of Python3 online submissions for Summary Ranges.
        Memory Usage: 17.75 MB, less than 36.70% of Python3 online submissions for Summary Ranges.
        """
        shift = 0
        # 主要是記錄總共移動了幾次可以找到left and right的共同前綴
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1

        return left << shift

